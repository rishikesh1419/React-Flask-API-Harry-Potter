import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Header from './components/Header'
import CharacterGrid from './components/CharacterGrid';
import Modal from './components/Modal';
import './App.css';

const App = () => {
    const [characters, setCharacters] = useState([]);
    const [isLoading, setIsLoading] = useState(true);
    const [isShowModal, setIsShowModal] = useState(false);
    const [person, setPerson] = useState({});

    useEffect(() => {
        const getChars = async () => {
            const result = await axios(`http://127.0.0.1:5000/characters`);
            setCharacters(result.data);
            setIsLoading(false);
        }

        getChars();
    }, []);

    const showModal = async (id) => {
        const result = await axios(`http://127.0.0.1:5000/characters/${id}`);
        setPerson(result.data[0]);
        setIsShowModal(true);
        document.body.style.overflow="hidden";
    }

    const closeModal = () => {
        setPerson({});
        setIsShowModal(false);
        document.body.style.overflow="auto";
    }

    return (
        // <Router>
            <div className="container">
                <Header />
                <CharacterGrid isLoading={ isLoading } characters={ characters } showModal={ showModal } />
                <Modal isShowModal={isShowModal} person={person} closeModal={closeModal} />
            </div>
        // </Router>
    );
}

export default App;
