from Servlet import app
from flask import render_template


@app.route("/morse")
def morse():
    return render_template("/morse/morse.html")
