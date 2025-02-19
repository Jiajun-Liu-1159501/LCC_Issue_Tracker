
from flask import Blueprint, request

from loginapp.aspect import token_check
from loginapp.constant.user_role import Role
from loginapp.services import user_service

user: Blueprint = Blueprint('user', __name__)

@user.get("/list")
@token_check([Role.ADMIN])
def fetch_users() -> str:
    user_name: str = request.args.get('user_name', type = str)
    first_name: str = request.args.get('first_name', type = str)
    last_name: str = request.args.get('last_name', type = str)
    return user_service.list_users(user_name,  first_name, last_name)