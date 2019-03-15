from Servlet import app
from flask import render_template, redirect, url_for, request, flash
from log_controller import *


@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        flash(add_log(request.form['log']))
    else:
        message = request.args.get('msg', '')
        if len(message) > 0:
            flash(add_log(message))
    return render_template('log/logs.html', logs=read_log())


@app.route('/log/clean')
def clean_log():
    flash(clean_log())
    return redirect(url_for('log'))
