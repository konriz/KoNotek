from datetime import datetime


class BlogPost:
    def __init__(self, date=datetime.now(), title='', content=''):
        self.date = date
        self.title = title
        self.content = content


def get_blog_posts():
    # TODO get this from markup files
    blog_posts = [BlogPost(title="Hi", content="Hi"), BlogPost(title="Ho", content="Ho")]
    return blog_posts
