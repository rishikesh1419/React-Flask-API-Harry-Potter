import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './components/Header'
import CharacterGrid from './components/CharacterGrid';
import './App.css';

const App = () => {
    const [characters, setCharacters] = useState([]);
    const [isLoading, setIsLoading] = useState(true);

    useEffect(() => {
        const getChars = async () => {
            const result = await axios(`http://127.0.0.1:5000/characters`);
            setCharacters(result.data);
            setIsLoading(false);
        }

        getChars();
    }, []);

    return (
        // <Router>
            <div className="container">
                <Header />
                <CharacterGrid isLoading={ isLoading } characters={ characters } />
            </div>
        // </Router>
    );
}

export default App;
