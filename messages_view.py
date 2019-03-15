from Servlet import app
from flask import render_template, redirect, url_for, request
from messages_dao import *


@app.route('/message', methods=['GET', 'POST'])
def new_message():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        add_message(Message(title=title, content=content))
        return redirect(url_for('list_messages'))
    return render_template('messages/new_message.html')


@app.route('/message/<id>', methods=['GET', 'POST'])
def show_message(id=None):
    if request.method == 'POST':
        delete_message(id)
    message = get_message(id)
    return render_template('messages/message.html', message=message)


@app.route('/messages')
def list_messages():
    messages = get_messages()
    return render_template('messages/messages.html', messages=messages)
