class Error(Exception):
    pass


class MissingValueError(Error):

    def __init__(self, message):
        self.message = message
