from Servlet import app
from flask import render_template, request
from modules.morse.morse import translate


@app.route("/morse", methods=['GET', 'POST'])
def morse():
    if request.method == 'GET':
        return render_template("/morse/morse.html", message='')
    mode = request.form['mode']
    input = request.form['input']
    output = translate(mode=mode, input=input)

    return render_template("/morse/morse.html", message={"input": input, "output": output})
