from Servlet import app
from flask import render_template

from modules.blog.blog_dao import get_blog_posts, get_blog_post


@app.route('/blog')
def show_blog():
    blog_posts = get_blog_posts()
    return render_template('blog/blog.html', blog_posts=blog_posts)


@app.route('/blog/<title>')
def show_post(title):
    post = get_blog_post(title)
    return render_template('blog/post.html', post=post)
