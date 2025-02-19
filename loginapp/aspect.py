

from typing import Callable, List
from functools import wraps

from flask import session
from loginapp.constant.user_role import Role
from loginapp.exception.custom_error import AccessDeclinedError
from loginapp.model.data_model import User
from loginapp.session_holder import SessionHolder


def token_check(*, options: List[Role]):
    """
    Decorator to enforce role-based access control.

    This decorator checks whether the current user is authenticated and 
    possesses the required role(s) before allowing access to the decorated function.

    Args:
        options (List[Role]): A list of allowed roles for accessing the decorated function.

    Raises:
        AccessDeclinedError: If the user is not logged in, session has expired, 
                             or the user's role is not in the allowed roles.

    Returns:
        Callable: The wrapped function with access control enforced.

    Example:
        ```python
        @token_check(options=[Role.ADMIN, Role.MODERATOR])
        def admin_dashboard():
            return "Welcome to the admin panel"
        ```
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token: str = session.get('token', None)
            if token is None:
                raise AccessDeclinedError('no login information')
            if not SessionHolder.session_exists():
                raise AccessDeclinedError('no login information expires')
            current_login: User = session.get('user')
            if options is None or len(options) == 0:
                return func(*args, **kwargs)
            if current_login.get_role_enum() not in options:
                raise AccessDeclinedError('this operation is not allowed')
            return func(*args, **kwargs)
        return wrapper
    return decorator


def current_user(*, id_func: Callable[[], str]):
    """
    Decorator to ensure that a user can only access their own resources.

    This decorator retrieves the current user's session and verifies that
    the user ID matches the expected ID provided by `id_func`.

    Args:
        id_func (Callable[[], str]): A function that returns the expected user ID.

    Raises:
        AccessDeclinedError: If the user is not logged in or is trying to access 
                             another user's data.

    Returns:
        Callable: The wrapped function with user ownership validation.

    Example:
        ```python
        @current_user(id_func=lambda: request.form.get('user_id'))
        def update_profile():
            return "Profile updated"
        ```
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(id_func())
            token: str = session.get('token', None)
            if token is None:
                raise AccessDeclinedError('no login information')
            current_login: User = session.get('user')
            if current_login.user_id != id_func():
                raise AccessDeclinedError('this operation is not allowed')
            return func(*args, **kwargs)
        return wrapper
    return decorator