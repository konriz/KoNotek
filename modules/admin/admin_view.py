from Servlet import app
from flask import render_template, redirect, url_for
from modules.persistence.sqlite_connector import clean_db, init_db


@app.route('/admin')
def show_admin():
    return render_template('admin/admin.html')


@app.route('/admin/clean')
def clean_database():
    clean_db()
    app.logger.debug('Database cleaned')
    init_db()
    app.logger.debug('Database initialised')
    return redirect(url_for('show_admin'))
