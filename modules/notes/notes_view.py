from Servlet import app
from flask import render_template, redirect, url_for, request
from modules.notes.notes_dao import *


@app.route('/notes')
def list_notes():
    notes = get_notes()
    return render_template('notes/notes.html', notes=notes)


@app.route('/note', methods=['GET', 'POST'])
def new_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        add_note(Note(title=title, content=content))
        return redirect(url_for('list_notes'))
    return render_template('notes/new_note.html')


@app.route('/note/<id>', methods=['GET', 'POST'])
def show_note(id=None):
    if request.method == 'POST':
        delete_note(id)
        return redirect(url_for('list_notes'))
    note = get_note(id)
    return render_template('notes/note.html', note=note)
