import persistence

ADD_MESSAGE_QUERY = """
    INSERT INTO messages(title, content) VALUES(?,?);
"""
GET_MESSAGES_QUERY = """
    SELECT * FROM messages;
"""
GET_MESSAGE_QUERY = """
    SELECT * FROM messages WHERE id=?;
"""
DELETE_MESSAGE_QUERY = """
    DELETE FROM messages WHERE id=?;
"""


class Message:
    def __init__(self, title='', content='', data=None):
        if data is not None:
            self.id = data[0]
            self.title = data[1]
            self.content = data[2]
        else:
            self.title = title
            self.content = content


def add_message(message):
    params = (message.title, message.content)
    persistence.execute_query_with_params(ADD_MESSAGE_QUERY, params)


def get_message(id):
    message_data = persistence.execute_select_query_with_params(GET_MESSAGE_QUERY, (id,))
    if len(message_data) == 1:
        return Message(data=message_data[0])
    return None


def delete_message(id):
    params = (id,)
    persistence.execute_query_with_params(DELETE_MESSAGE_QUERY, params)


def get_messages():
    messages_data = persistence.execute_select_query(GET_MESSAGES_QUERY)
    messages = []
    for message_data in messages_data:
        messages.append(Message(data=message_data))
    return messages
