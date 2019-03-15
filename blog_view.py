from Servlet import app
from flask import render_template

from blog_dao import get_blog_posts


@app.route('/blog')
def show_blog():
    blog_posts = get_blog_posts()
    return render_template('blog/blog.html', blog_posts=blog_posts)
