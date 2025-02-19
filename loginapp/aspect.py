

from typing import List
from functools import wraps

from flask import session
from loginapp.constant.user_role import Role
from loginapp.constant.user_status import UserStatus
from loginapp.exception.custom_error import AccessDeclinedError
from loginapp.model.data_model import User
from loginapp.services import user_service
from loginapp.session_holder import SessionHolder


def token_check(options: List[Role]):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            token: str = session.get('token', None)
            if token is None:
                raise AccessDeclinedError('no login information')
            current_login: User = session.get('user')
            user: User = user_service.get_user(current_login.user_id)
            if UserStatus.INACTIVE is user.get_status_enum():
                SessionHolder.session_evict(current_login)
                raise AccessDeclinedError('current user is now inactive')
            if options is None or len(options) == 0:
                return func(*args, **kwargs)
            if current_login.get_role_enum() not in options:
                raise AccessDeclinedError('this operation is not allowed')
            return func(*args, **kwargs)
        return wrapper
    return decorator