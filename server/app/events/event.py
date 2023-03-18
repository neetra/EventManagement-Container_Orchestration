import functools

from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash
import mysql.connector
import json;

bp = Blueprint("auth", __name__, url_prefix="/event")

@bp.route("/", methods=("GET", "POST"))
def register():
    return 'hello from event'


def test_table():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'devopsroles'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM events')
    results = [name for ( name) in cursor]
    cursor.close()
    connection.close()
    return results

@bp.route('/pingDB')
def index() -> str:
    return json.dumps({'test_table': test_table()})

@bp.route('/pingDB2')
def index() -> str:
    return json.dumps({'test_table': 'tmep'})