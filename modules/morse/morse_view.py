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
    string = request.form['output']
    date = datetime.now()
    date_string = "{0}-{1}-{2}{3}{4}".format(date.month, date.day, date.hour, date.minute, date.second)
    filename = date_string + '.wav'
    writer = Writer(filename)
    try:
        writer.write_morse_wav(string)
        flash('"{}" created with message "{}"'.format(filename, string))
    except MorseException as e:
        try:
            morse_string = translate(mode='to_code', input=string)
            writer.write_morse_wav(morse_string)
            flash('"{}" created with message "{}"'.format(filename, morse_string))
        except MorseException as e:
            flash('Message "{}" is not valid - sign "{}" unsupported'.format(string, e.sign))
        except KeyError as e:
            flash("Sign {e} not valid".format(e=e))
    return redirect(url_for('morse'))
