
from typing import Dict


class ArgumentError(Exception):

    def __init__(self, args: str, message: str):
        super().__init__(message)
        self._args_dict: Dict[str, str] = {}
        self._args_dict.setdefault(args, message)

    def get_error_args(self) -> Dict[str, str]:
        return self._args_dict


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