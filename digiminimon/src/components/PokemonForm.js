import React from 'react'
import { useState } from 'react'
export default function FilmForm() {
    const [pokemon, setPokemon] = useState('')
    // const [imageActor, setImageActor] = useState('https://e7.pngegg.com/pngimages/84/165/png-clipart-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper-thumbnail.png')
    // const [imageRealisator, setImageRealisator] = useState('https://e7.pngegg.com/pngimages/84/165/png-clipart-united-states-avatar-organization-information-user-avatar-service-computer-wallpaper-thumbnail.png')

  
    const handleSubmit = async (e) => {
        e.preventDefault()

        const digimon = {pokemon}

        const response = await fetch('/api/films', {
            method:'POST',
            body: JSON.stringify(digimon),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        const json = await response.json()
        if(response.ok) {
            setPokemon('')
            console.log('new pokemon added')
        }
    }
    return (
    <form className='create' onSubmit={handleSubmit}>
        <label>Pokémon</label>
        <input 
        type='text'
        onChange={(e) => setPokemon(e.target.value)}
        value= {pokemon} 

        />
        <button type='submit'>Search a pokemon</button>
    </form>
    
  )
}
