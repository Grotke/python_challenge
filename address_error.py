class InvalidAddressError(Exception):
    def __init__(self, msg, badInput = None):
        self.badInput = badInput
        self.msg = msg

    def __str__(self):
        if self.badInput:
            return "{0}: {1}".format(self.msg, self.badInput)
        return self.msg

class InvalidInputError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg