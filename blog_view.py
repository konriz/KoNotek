from Servlet import app
from flask import render_template


@app.route('/blog')
def show_blog():
    return render_template('blog/blog.html')
