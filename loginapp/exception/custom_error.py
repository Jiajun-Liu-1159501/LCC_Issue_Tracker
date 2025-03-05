from typing import Dict


class ArgumentError(Exception):
    """
    Exception raised for invalid arguments.

    Attributes:
        args (str): The name of the argument that caused the error.
        message (str): A description of the error.
    """

    def __init__(self, args: str, message: str):
        super().__init__(message)
        self._args_dict: Dict[str, str] = {}
        self._args_dict.setdefault(args, message)

    def get_error_args(self) -> Dict[str, str]:
        """
        Returns a dictionary containing the argument name and corresponding error message.

        Returns:
            Dict[str, str]: The dictionary of argument errors.
        """
        return self._args_dict


class NotFoundError(Exception):
    """
    Exception raised when a requested resource is not found.

    Attributes:
        message (str): A description of the error.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class AccessDeclinedError(Exception):
    """
    Exception raised when access to a resource is declined.

    Attributes:
        message (str): A description of the error.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class UnauthorizedError(Exception):
    """
    Exception raised when a user is not authorized to perform an action.

    Attributes:
        message (str): A description of the error.
    """
    
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class OperationNotAllowedError(Exception):
    """
    Exception raised when an operation is not allowed.

    Attributes:
        message (str): A description of the error.
    """

    def __init__(self, message: str):
        super().__init__(message)
        self.message = message