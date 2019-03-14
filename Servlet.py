
from flask import Flask, render_template, request, url_for, redirect, flash

import message_saver
from messaging import *
from persistence import init_db, clean_db, close_connection

app = Flask(__name__)
app.secret_key = b'secret'


@app.before_first_request
def init_database():
    init_db()
    app.logger.debug('Database initialised')


@app.route('/admin')
def show_admin():
    return render_template('admin.html')


@app.route('/admin/clean')
def clean_database():
    clean_db()
    app.logger.debug('Database cleaned')
    init_database()
    return redirect(url_for('show_admin'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/message', methods=['GET', 'POST'])
def new_message():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        add_message(Message(title=title, content=content))
        return redirect(url_for('list_messages'))
    return render_template('new_message.html')


@app.route('/message/<id>', methods=['GET', 'POST'])
def show_message(id=None):
    if request.method == 'POST':
        delete_message(id)
    message = get_message(id)
    return render_template('message.html', message=message)


@app.route('/messages')
def list_messages():
    messages = get_messages()
    return render_template('messages.html', messages=messages)


@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        flash(message_saver.add_log(request.form['log']))
    else:
        message = request.args.get('msg', '')
        if len(message) > 0:
            flash(message_saver.add_log(message))
    return render_template('logs.html', logs=message_saver.read_log())


@app.route('/log/clean')
def clean_log():
    flash(message_saver.clean_log())
    return redirect(url_for('log'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


@app.teardown_appcontext
def close_db_connection(exception):
    close_connection(exception)
