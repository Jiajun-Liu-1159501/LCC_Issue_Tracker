
class ArgumentError(Exception):

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class NotFoundError(Exception):

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class AccessDeclinedError(Exception):

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class OperationNotAllowedError(Exception):

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message