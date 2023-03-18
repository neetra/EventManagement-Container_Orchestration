import logo from './logo.svg';
import './App.css';
import EventDetails from './EventDetails';
import EventTable from './EventTable';
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  return (

 
    <Routes>
      <Route  exact path="/" element={<EventTable />} />
      <Route path="event/:id" element={<EventDetails />} />    

    </Routes>

   
  );
}

export default App;
