import {HiTrash} from 'react-icons/hi'
import axios from 'axios'
import { BASEURL } from './config'

export async function getAllEvents() {

const url = BASEURL + "/events"
const resp =  await axios.get(url)
return resp.data
}

export async function getEventDetails(eventId) {

    const url = BASEURL + "?eventId=" + eventId
    const resp =  await axios.get(url)
    return resp.data
    }

    export async function deleteEventDetails(eventId) {

        const url = BASEURL + "?eventId=" + eventId
        const resp =  await axios.delete(url)
        return resp.data
        }
    

    
export async function addEventDetails(eventObj) {

    const url = BASEURL
    const resp =  await axios.post(url, eventObj)
    return resp.data
    }