import React, { useState, useEffect } from "react";
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { EventService } from './service/EventService';
        
import { Button } from 'primereact/button';
import AddEventModal from "./AddEventModal";
import Modal from 'react-modal';    
export default function EventTable() {
  const [products, setProducts] = useState([]);
const [modalIsOpen, setIsVisible] = useState(false);
  useEffect(() => {
    EventService.getProductsMini().then(data => setProducts(data));
  }, []);

  return (
    <div>
    <div><Button onClick={() => {setIsVisible(true)}} >Add New</Button></div>
      <div className="event-table">       
          <DataTable value={products} tableStyle={{ minWidth: '50rem' }}>
              <Column field="code" header="Code"></Column>
              <Column field="name" header="Name"></Column>
              <Column field="category" header="Category"></Column>
              <Column field="quantity" header="Quantity"></Column>
              <Column field='delete' header='delete'></Column>
          </DataTable>
      </div>
      <Modal
        isOpen={modalIsOpen}  
        contentLabel="Example Modal"
      >
        <h2>Hello</h2>
        <button>close</button>
        <div>I am a modal</div>
        <form>
          <input />
          <button>tab navigation</button>
          <button>stays</button>
          <button>inside</button>
          <button>the modal</button>
        </form>
      </Modal>
      </div>
  );
}
      
