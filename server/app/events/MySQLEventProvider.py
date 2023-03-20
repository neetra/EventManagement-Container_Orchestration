from configparser import Error
from tabnanny import check
from typing import Tuple
import mysql.connector 
from MySQLHelper import closeMysqlconnection, createConnection
from datetime import datetime
import config
from mysql.connector.cursor import MySQLCursorDict, MySQLCursorPrepared
import uuid
from events.JSONKeys import JSONKeys;
class MySQLEventProvider():   
   


    def get_sql_version(self, eventInventoryDbConnection= None):
        
        try:     
            eventInventoryDbConnection = createConnection()        
           
            
            my_cursor = eventInventoryDbConnection.cursor()
            
            query = "SELECT version()"
        
            
            my_cursor.execute(query)
            
            results = my_cursor.fetchone()
            if(results is None):
                return None

                         
            return results["version()"]               
        except mysql.connector.Error as err:
            print (err)     
        finally:
            closeMysqlconnection(eventInventoryDbConnection)                   
        
        return None



    def add_event(self, eventData, eventInventoryDbConnection=None):
        try:
            eventInventoryDbConnection = createConnection()     #established connection between your database   
            result =  None

            with eventInventoryDbConnection.cursor() as my_cursor:     
                eventId = uuid.uuid4().hex
                sql = "insert into events (id, name, HostBy, Description) values (%s, %s, %s, %s);"
                val = (eventId, eventData[JSONKeys.EventNameParam], eventData[JSONKeys.EventHostByParam], eventData[JSONKeys.EventDescriptionParam])
                my_cursor.execute(sql, val)

                eventInventoryDbConnection.commit()

            return self.get_event_by_id_or_name(eventId)                
        except mysql.connector.Error as err:
            return err.msg
        except Error as e:
            return e
        finally:
            closeMysqlconnection(eventInventoryDbConnection)     
        
    
    def get_event_by_id_or_name(self, eventId, isName = False,eventInventoryDbConnection= None):
        try: 
            
            eventInventoryDbConnection = createConnection()     #established connection between your database   
            result =  None
            with eventInventoryDbConnection.cursor() as my_cursor:              
                
                    query = """SELECT * from events where id=%s"""
    
                    my_cursor.execute(query, (eventId,))

                    result = my_cursor.fetchone()                 
        
              
           
            return result                
        except mysql.connector.Error as err:
            print (err)
        finally:
            closeMysqlconnection(eventInventoryDbConnection)         
        
        return None


    def delete_event_by_id(self, eventId,eventInventoryDbConnection= None):
        try:             
            eventInventoryDbConnection = createConnection()    #established connection between your database   
           

            with eventInventoryDbConnection.cursor() as my_cursor:   
                
                    query = """DELETE from events where id = %s"""    
                    my_cursor.execute(query, eventId)                                           
                    eventInventoryDbConnection.commit()  
                          
        except mysql.connector.Error as err:
            return err.msg
        except Error as e:
            return e
        finally:
            closeMysqlconnection(eventInventoryDbConnection)           
        
        return None 

    def get_all_events(self, eventInventoryDbConnection=None):
        try: 
            
            eventInventoryDbConnection = createConnection()     #established connection between your database   
            result =  None   

            with eventInventoryDbConnection.cursor() as my_cursor:   
                
                    query = """SELECT * from events"""

    
                    my_cursor.execute(query)

                    result = my_cursor.fetchall()                            
            
            return result                
        except mysql.connector.Error as err:
            return err.msg
        except Error as e:
            return e
        finally:
            closeMysqlconnection(eventInventoryDbConnection)                 
