from datetime import datetime

from modules.persistence import sqlite_connector

ADD_MESSAGE_QUERY = """
    INSERT INTO notes(date, title, content) VALUES(?,?,?);
"""
GET_MESSAGES_QUERY = """
    SELECT * FROM notes;
"""
GET_MESSAGE_QUERY = """
    SELECT * FROM notes WHERE id=?;
"""
DELETE_MESSAGE_QUERY = """
    DELETE FROM notes WHERE id=?;
"""


class Note:
    def __init__(self, title='', content='', data=None):
        if data is not None:
            self.id = data[0]
            self.date = data[1]
            self.title = data[2]
            self.content = data[3]
        else:
            self.date = datetime.now()
            self.title = title
            self.content = content


def add_note(note):
    params = (note.data, note.title, note.content)
    sqlite_connector.execute_query_with_params(ADD_MESSAGE_QUERY, params)


def get_note(id):
    message_data = sqlite_connector.execute_select_query_with_params(GET_MESSAGE_QUERY, (id,))
    if len(message_data) == 1:
        return Note(data=message_data[0])
    return None


def delete_note(id):
    params = (id,)
    sqlite_connector.execute_query_with_params(DELETE_MESSAGE_QUERY, params)


def get_notes():
    messages_data = sqlite_connector.execute_select_query(GET_MESSAGES_QUERY)
    messages = []
    for message_data in messages_data:
        messages.append(Note(data=message_data))
    return messages
