import sqlite3
from os import remove
from flask import g

from messaging import Message

DATABASE = 'database.db'
INIT_QUERY = """
    CREATE TABLE IF NOT EXISTS messages (
    id integer PRIMARY KEY,
    title text NOT NULL,
    content text
    );
"""
ADD_MESSAGE_QUERY = """
    INSERT INTO messages(title, content) VALUES(?,?);
"""
GET_MESSAGES_QUERY = """
    SELECT * FROM messages;
"""
GET_MESSAGE_QUERY = """
    SELECT * FROM messages WHERE id=?;
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
        execute_query(connection, INIT_QUERY)
    else:
        raise Exception('DB init failed!')


def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def add_message(message):
    params = (message.title, message.content)
    execute_query_with_params(get_db(), ADD_MESSAGE_QUERY, params)


def get_messages():
    messages_data = execute_select_query(get_db(), GET_MESSAGES_QUERY)
    messages = []
    for message_data in messages_data:
        messages.append(Message(data=message_data))
    return messages


def get_message(id):
    message_data = execute_select_query_with_params(get_db(), GET_MESSAGE_QUERY, (id,))
    if len(message_data) == 1:
        return Message(data=message_data[0])
    return None


def execute_select_query_with_params(connection, query, params):
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)


def execute_select_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(e)


def execute_query_with_params(connection, query, params):
    try:
        cursor = connection.cursor()
        cursor.execute(query, params)
        connection.commit()
        print(f'Executing {query} with {params}')
    except sqlite3.Error as e:
        print(e)


def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
    except sqlite3.Error as e:
        print(e)
