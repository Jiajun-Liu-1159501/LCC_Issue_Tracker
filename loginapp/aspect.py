

from typing import Callable, List
from functools import wraps

from flask import session
from loginapp.constant.user_role import Role
from loginapp.constant.user_status import UserStatus
from loginapp.exception.custom_error import AccessDeclinedError
from loginapp.model.data_model import User
from loginapp.services import user_service
from loginapp.session_holder import SessionHolder


def token_check(*, options: List[Role]):
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
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token: str = session.get('token', None)
            if token is None:
                raise AccessDeclinedError('no login information')
            current_login: User = session.get('user')
            if current_login.user_id != id_func():
                raise AccessDeclinedError('this operation is not allowed')
            return func(*args, **kwargs)
        return wrapper
    return decorator