from datetime import datetime

from Servlet import app
from flask import render_template, request, redirect, url_for, flash
from modules.morse.morse import translate
from modules.morse.generator import Writer, MorseException


@app.route("/morse", methods=['GET', 'POST'])
def morse():
    if request.method == 'GET':
        return render_template("/morse/morse.html", message='')
    mode = request.form['mode']
    input = request.form['input']
    output = translate(mode=mode, input=input)
    return render_template("/morse/morse.html", message={"input": input, "output": output})


@app.route("/morse/wave", methods=['POST'])
def generate_wave():
    morse_string = request.form['output']
    date = datetime.now()
    date_string = "{0}-{1}-{2}-{3}".format(date.month, date.day, date.hour, date.minute)
    filename = date_string + '.wav'
    writer = Writer(filename)
    try:
        writer.write_morse_wav(morse_string)
        flash('"{}" created with message "{}"'.format(filename, morse_string))
    except MorseException as e:
        flash('Message "{}" is not valid - sign "{}" unsupported'.format(morse_string, e.sign))
    return redirect(url_for('morse'))
