
import { useLocation, Link, useParams  } from "react-router-dom";
import React, { useState, useEffect } from "react";
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { addEventDetails } from './service/EventService';
import Modal from 'react-modal';               
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
import { InputText } from 'primereact/inputtext';
  
export default function AddEventModal(props) {

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [hostBy, setHostBy] = useState("");

  const setNameField = (e) =>{
    setName(e.target.value)
  }
  const addEvent =() =>{
    const postEventObj = {
        eventName : name,
        eventDescription : description,
        eventHostBy : hostBy
    }

    addEventDetails(postEventObj)
    props.onAdd()
  }
  return (
    <Modal
    isOpen={props.modalIsOpen}  
    contentLabel="Example Modal"
  >
    <div id="add-event-modal-title">Title</div>
    <div id='add-event-modal-body'>
 
 <div>
      <div>Name</div>
      <InputText value={name} onChange={(e)=> setNameField(e)} />
      </div>

      <div>
      <div>Description</div>
      <InputText value={description} onChange={(e)=> setDescription(e.target.value)} />
      </div>
      <div>
      <div>HostBy</div>
      <InputText value={hostBy} onChange={(e)=> setHostBy(e.target.value)} />
      </div>
     
    </div>
 
    <div id='add-event-modal-footer'>
      <Button  onClick={addEvent}>Add</Button>
      <Button onClick={props.onCloseModal}>Close</Button>
    </div>
  </Modal>
  );
}
      
