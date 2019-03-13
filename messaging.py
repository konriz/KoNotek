

class Message:

    def __init__(self, title='', content='', data=None):
        if data is not None:
            self.id = data[0]
            self.title = data[1]
            self.content = data[2]
        else:
            self.title = title
            self.content = content
