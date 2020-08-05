import React from 'react'

const CharacterItem = ({ character, showModal }) => {
    return (
        <div className="card">
            <div className="card-inner">
                <div className="card-front">
                    <h1>{ character.name }</h1>
                </div>
                <div className="card-back">
                    <ul>
                        <li><h3>Species: { character.species }</h3></li>
                        <li><h3>House: { character.house ? character.house : "Unknown" }</h3></li>
                    </ul>
                    <button className="details-button" onClick={ showModal.bind(this, character._id) }>Details</button>
                </div>
            </div>
        </div>
    )
}

export default CharacterItem
