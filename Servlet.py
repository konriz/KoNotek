from flask import Flask, render_template

from persistence import init_db, close_connection

app = Flask(__name__)
app.secret_key = b'secret'

import blog_view
import admin_view
import messages_view
import log_view


@app.before_first_request
def init_database():
    init_db()
    app.logger.debug('Database initialised')


@app.route('/')
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


@app.teardown_appcontext
def close_db_connection(exception):
    close_connection(exception)
