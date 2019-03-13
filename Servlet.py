from flask import Flask, render_template, request, url_for, redirect

from messaging import Message
from persistence import close_connection, add_message, init_db, clean_db, get_messages, get_message

app = Flask(__name__)


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


@app.route('/message/<id>')
def show_message(id=None):
    message = get_message(id)
    return render_template('message.html', message=message)


@app.route('/messages')
def list_messages():
    messages = get_messages()
    return render_template('messages.html', messages=messages)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


@app.teardown_appcontext
def close_db_connection(exception):
    close_connection(exception)
