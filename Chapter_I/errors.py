class Error(Exception):
    pass


class IllegalCarError(Error):

    def __init__(self, message):
        self.message = message
