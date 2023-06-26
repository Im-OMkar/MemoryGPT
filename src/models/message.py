class UserMessage(object):
    def __init__(self, message, type, userData):
        self.message = message
        self.type = type
        self.userData = userData

    class UserData(object):
        def __init__(self, user_name):
            self.user_name = user_name

    def __init__(self, revision):
        self.revision = revision
