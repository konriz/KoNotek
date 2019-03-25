from Servlet import app
from flask import render_template, redirect, url_for, request, flash
import modules.log.log_controller as controller


@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        flash(controller.add_log(request.form['log']))
    else:
        message = request.args.get('msg', '')
        if len(message) > 0:
            flash(controller.add_log(message))
    return render_template('log/logs.html', logs=controller.read_log())


@app.route('/log/clean')
def clean_log():
    flash(controller.clean_log())
    return redirect(url_for('log'))
