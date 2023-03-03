import network   #import des fonction lier au wifi
import urequests	#import des fonction lier au requetes http
import utime	#import des fonction lier au temps
import ujson	#import des fonction lier aà la convertion en Json
from machine import Pin, PWM, I2C
from pico_i2c_lcd import I2cLcd

wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi

ssid = 'IIM_Private'
password = 'Creatvive_Lab_2023'

wlan.connect(ssid, password) # connecte la raspi au réseau

def equilRGB(n):
    return int(n / 255 * 15000)


ledPin = [15,14, 13, 16, 17, 18 ]
arrayTypes = {
            "Normal": (255,255,255),
            "Eau": (0,0,255),
            "Feu": (255,0,0), 
            "Plante": (0,255,0), 
            "\xc9lectrik": (255,135,0), 
            "Psy": (255,0,170),
            "Glace": ((145,145,255)),
            "Sol": (88, 69, 17),
            "Spectre": (255,0,170),
            "F\xe9e": ((255,10,140)),
            "Dragon": (88, 69, 255),
            "Combat": (205,0,180),
            "Acier": ((200,200,200)),
            "Vol": (0, 0, 17),
            "T\xe9n\xe8bre": (220,0,170),
            "Roche": ((145,145,255)),
            "Poison": (205,0,140),
            "Insecte": (120,205,0),
            }
blue = PWM(Pin(ledPin[0], mode=Pin.OUT))
green = PWM(Pin(ledPin[1], mode=Pin.OUT))
red = PWM(Pin(ledPin[2], mode=Pin.OUT))
blue2 = PWM(Pin( ledPin[3]  , mode=Pin.OUT))
green2 = PWM(Pin(ledPin[4] , mode=Pin.OUT))
red2 = PWM(Pin(ledPin[5], mode=Pin.OUT))

blue.freq(1_000)
green.freq(1_000)
red.freq(1_000)

blue2.freq(1_000)
green2.freq(1_000)
red2.freq(1_000)


# Tablette écran
i2c = I2C(0, sda=Pin(8), scl=Pin(9), freq=400000)
print(i2c.scan())
utime.sleep(1)
I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

while(True):
    pokemon = input("Quel pokemon ?" + " ")
    url = "https://api-pokemon-fr.vercel.app/api/v1/pokemon/" + pokemon
    lcd.clear()
    try:
        r = urequests.get(url) # lance une requete sur l'
        types = r.json()["types"]
        type1 = types[0]["name"] # traite sa reponse en Json pour le premier type
        type2 = ""
        # type1 = r.json()["types"][0]["name"] # traite sa reponse en Json pour le premier type
        # type2 = r.json()["types"][0]["name"][1] # traite sa reponse en Json pour le second type
        r.close() # ferme la demdittande
        if len(types) >= 2:
            type2 = types[1]["name"]
            redHue2 = arrayTypes[type2][0]
            greenHue2 = arrayTypes[type2][1]
            blueHue2 = arrayTypes[type2][2]
            blue2.duty_u16(equilRGB(blueHue2))
            red2.duty_u16(equilRGB(redHue2))
            green2.duty_u16(equilRGB(greenHue2))
        else: 
            blue2.duty_u16(0)
            red2.duty_u16(0)
            green2.duty_u16(0)
        print("Le pokemon est de type : " + " " + type1)
        redHue = arrayTypes[type1][0]
        greenHue = arrayTypes[type1][1]
        blueHue = arrayTypes[type1][2]
        blue.duty_u16(equilRGB(blueHue))
        red.duty_u16(equilRGB(redHue))
        green.duty_u16(equilRGB(greenHue))

        if pokemon == "magicarpe":
             type2 = "Dieu"
             
        lcd.move_to(0,0)
        lcd.putstr(pokemon)
        lcd.move_to(0,1)
        lcd.putstr(type1 + " " + type2)

        if type2 == "Dieu" :
                while True:
                    blue2.duty_u16(equilRGB(120))
                    red2.duty_u16(equilRGB(200))
                    green2.duty_u16(equilRGB(200))
                    utime.sleep(1)
                    blue2.duty_u16(0)
                    red2.duty_u16(0)
                    green2.duty_u16(0)
                    utime.sleep(1)
        
    except Exception as e:
        print(e)