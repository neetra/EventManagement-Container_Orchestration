
import { useLocation, Link, useParams  } from "react-router-dom";
import React, { useState, useEffect } from "react";
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { EventService, getEventDetails } from './service/EventService';
import {HiTrash} from 'react-icons/hi'

import { ProgressSpinner } from 'primereact/progressspinner';
        
export default function EventDetails(props) {
  const [products, setProducts] = useState();
const {id} = useParams()
useEffect(() => {
  getEventDetails(id).then((res) =>{

  
    setProducts(res)
  })
}, []);

  return (
     
      <div className="event-details-container">
      {
        products &&
        (
        <div>
          <div>
            Id : {products.id}            
            </div>
          <div>
            Name : {products.Name}            
            </div>
            <div>
            Host By : {products.HostBy}            
            </div>
            <div>
            Description : {products.description}            
            </div>
         </div>
        )
      }
      {!products && (
        <div><ProgressSpinner /></div>
      )}
      </div>
  );
}
      
