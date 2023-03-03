// fetch pokeapi versel 

const url = 'https://api-pokemon-fr.vercel.app/api/v1/pokemon/pikachu';

function getPokemon() {
    fetch(url)
        .then(response => response.json())
        .then(data => console.log(data));
        console.log(data)
}

