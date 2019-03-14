import sqlite3
from os import remove
from flask import g


DATABASE = 'database.db'
INIT_QUERY = """
    CREATE TABLE IF NOT EXISTS messages (
    id integer PRIMARY KEY,
    title text NOT NULL,
    content text
    );
"""


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


def clean_db():
    remove(DATABASE)


def init_db():
    connection = get_db()
    if connection is not None:
        execute_query(INIT_QUERY)
    else:
        raise Exception('DB init failed!')


def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def execute_select_query_with_params(query, params):
    try:
        cursor = get_db().cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)


def execute_select_query(query):
    try:
        cursor = get_db().cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)


def execute_query_with_params(query, params):
    try:
        cursor = get_db().cursor()
        cursor.execute(query, params)
        get_db().commit()
        print(f'Executing {query} with {params}')
    except sqlite3.Error as e:
        print(e)


def execute_query(query):
    try:
        cursor = get_db().cursor()
        cursor.execute(query)
    except sqlite3.Error as e:
        print(e)
