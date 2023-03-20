import functools
from configparser import Error
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
import mysql.connector
from events.MySQLEventProvider import MySQLEventProvider;
import json;
from events.JSONKeys import JSONKeys;

bp = Blueprint("auth", __name__, url_prefix="/event")
mysqlprovider = MySQLEventProvider()
@bp.route("/", methods=["GET"])
def register():
    return 'hello from event'

@bp.route('/pingdb')
def pingDB() -> str:
    try:           
        version = mysqlprovider.get_sql_version()
        return { "MYSQL VERSION " : version, "Connection" : "Success"}, 200
    except Error as e:
        return "Error " + e, 400  
    
@bp.route('/events')
def get_all_events() -> str:
    try:           
        allevents = mysqlprovider.get_all_events()
        return allevents, 200
    except Error as e:
        return "Error " + e, 400     


@bp.route('/', methods=["POST"])
def add_event() -> str:
    try:      
        jsonData = request.json      
        allevents = mysqlprovider.add_event(jsonData)
        return allevents, 200
    except Error as e:
        return "Error " + e, 400       
    

@bp.route(rule="",methods=["Get"])
def get_event_by_id() -> str:
    try:      
        jsonData = request.args.get(JSONKeys.EventIdParam)      
        allevents = mysqlprovider.get_event_by_id_or_name(jsonData)
        return allevents, 200
    except Error as e:
        return "Error " + e, 400           
    

@bp.route(rule="",methods=["Delete"])
def del_event_by_id() -> str:
    try:      
        jsonData = request.args.get(JSONKeys.EventIdParam)      
        allevents = mysqlprovider.delete_event_by_id(jsonData)
        return  json.dumps({'message':'event deleted successfully'}) ,200
    except Error as e:
        return "Error " + e, 400        