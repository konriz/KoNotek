from datetime import datetime
from Servlet import pages


class BlogPost:
    def __init__(self, date=datetime.now(), title='', content=''):
        self.date = date
        self.title = title
        self.content = content


def get_blog_posts():
    blog_posts = (p for p in pages if 'published' in p.meta)
    return blog_posts


def get_blog_post(title):
    blog_post = pages.get_or_404(title)
    return blog_post
