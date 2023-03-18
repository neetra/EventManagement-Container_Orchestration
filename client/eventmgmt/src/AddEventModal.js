
import { useLocation, Link, useParams  } from "react-router-dom";
import React, { useState, useEffect } from "react";
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { EventService } from './service/EventService';
                
import { Button } from 'primereact/button';
import { Dialog } from 'primereact/dialog';
        
export default function AddEventModal(props) {
  const [products, setProducts] = useState([]);

const footerContent = (
    <div>
        <Button label="No" icon="pi pi-times"  />
        <Button label="Yes" icon="pi pi-check" />
    </div>
);
  return (
      <div className="card">
     <Dialog header="Header" visible={props.isVisible} style={{ width: '50vw' }}  footer={footerContent}>
    <p className="m-0">
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>
</Dialog>
      </div>
  );
}
      
