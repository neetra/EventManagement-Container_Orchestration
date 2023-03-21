import React, { useState, useEffect } from "react";
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import {  deleteEventDetails, getAllEvents } from './service/EventService';
        

import AddEventModal from "./AddEventModal";

import {HiTrash} from 'react-icons/hi'   

import { Button } from 'primereact/button';
        
export default function EventTable() {
  const [products, setProducts] = useState([]);
  
const [modalIsOpen, setIsVisible] = useState(false);
const deleteEvent = (event) => {
  deleteEventDetails(event.id)
  window.location.reload()

}
const deleteBodyTemplate =(eventIn) =>{
  return (
 
  <HiTrash onClick={() => deleteEvent(eventIn)} />
  )
}



const onAdd = () =>{
  setIsVisible(false) 
  window.location.reload()
}
const onCloseModal = () =>{
  setIsVisible(false) 
}

const nameBodyTemplate =(event) =>{
 const eventUrl = window.location.origin + "/event/" + event.id
  return (<a href={eventUrl}>{event.Name}</a>)
}
  useEffect(() => {
    getAllEvents().then((res) =>{

    
      setProducts(res)
    })
  }, []);

  return (
    <div>
    <div><Button onClick={() => {setIsVisible(true)}} >Add New</Button></div>
      <div className="event-table">       
          <DataTable value={products} tableStyle={{ minWidth: '20rem' }}>
              
              <Column body={nameBodyTemplate} header="name"></Column>             
              <Column field="HostBy" header="HostBy"></Column>
              <Column  body={deleteBodyTemplate} header="Delete"></Column>
          </DataTable>
      </div>
    <AddEventModal onAdd={onAdd} onCloseModal={onCloseModal} modalIsOpen={modalIsOpen} />
      </div>
  );
}
      
