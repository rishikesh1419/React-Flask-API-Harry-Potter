import React from 'react'

const Modal = ({ isShowModal, person, closeModal }) => {
    if(isShowModal)
        return (
            <div className="modal-wrapper">
                <div className="modal-backdrop" />
                <div className="modal-box">
                    <h2>{person.name}</h2>
                    <button onClick={closeModal}>Close</button>
                </div>
            </div>
        )
    else return null;
}

export default Modal
