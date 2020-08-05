import React from 'react'
import CharacterItem from './CharacterItem';

const CharacterGrid = ({ isLoading, characters }) => {
    return isLoading ? (<h1>Loading...</h1>) : <section className="cards">
        { characters.map(character => (
            <CharacterItem key={character._id} character={character} />
        )) }
    </section>;
}

export default CharacterGrid
