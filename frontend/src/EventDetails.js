
import { useLocation, Link, useParams  } from "react-router-dom";
import React, { useState, useEffect } from "react";
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { EventService } from './service/EventService';
        
export default function EventDetails(props) {
  const [products, setProducts] = useState([]);
const {id} = useParams()

  return (
      <div className="card">
      Details {id}
      </div>
  );
}
      
