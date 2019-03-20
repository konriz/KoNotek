from flask import Flask, render_template
from flask_flatpages import FlatPages, pygments_style_defs

from modules.persistence.sqlite_connector import init_db, close_connection

app = Flask(__name__)
app.config.from_pyfile('config')

pages = FlatPages(app)

import modules.blog.blog_view
import modules.admin.admin_view
import modules.messages.messages_view

# FIXME logs not working with heroku
# import modules.log.log_view


@app.before_first_request
def init_database():
    init_db()
    app.logger.debug('Database initialised')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pygments.css')
def pygmens_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


@app.teardown_appcontext
def close_db_connection(exception):
    close_connection(exception)
