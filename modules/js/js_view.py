from Servlet import app
from flask import render_template


@app.route('/js')
def js_index():
    return render_template('/js/index.html')


@app.route('/js/redirect')
def js_redirect():
    return render_template('/js/redirect.html')
