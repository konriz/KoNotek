from Servlet import app
from flask import render_template


@app.route('/experiments/')
def experiments():
    return render_template('experiments.html')
