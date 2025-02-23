
from typing import List
from flask import Blueprint, Response, jsonify, request, session

from loginapp.aspect import current_user, token_check
from loginapp.constant.user_role import Role
from loginapp.model.data_model import User
from loginapp.model.user_req_model import ImageResetRequest, PasswordResetRequest, UserEditRequest, UserUpdateRequest
from loginapp.services import user_service
from loginapp.session_holder import SessionHolder

user: Blueprint = Blueprint('user', __name__)

@user.get("/current")
@token_check(options = [])
def get_current_login() -> Response:
    user: User = SessionHolder.current_login()
    return jsonify({
        "user_info": user,
        "operations": user.get_role_enum().get_allowed_operations()
    }), 200

@user.get("/list")
@token_check(options = [Role.ADMIN])
def list_users_endpoint() -> Response:
    user_name: str = request.args.get('user_name', type = str)
    first_name: str = request.args.get('first_name', type = str)
    last_name: str = request.args.get('last_name', type = str)
    users: List[User] = user_service.list_users(user_name,  first_name, last_name)
    return jsonify({
        "data": users 
    }), 200

@user.post("/edit")
@current_user(id_func = lambda: request.form.get('user_id'))
def edit_profile_endpoint() -> Response:
    req: UserEditRequest = UserEditRequest.build(request)
    user_service.edit_user(req, lambda u: None)
    return jsonify({
        "message": "success"
    }), 200

@user.post("/resetpwd")
@current_user(id_func = lambda: request.form.get('user_id'))
def reset_pwd_endpoint() -> Response:
    req: PasswordResetRequest = PasswordResetRequest.build(request)
    user_service.password_reset(req, lambda u: SessionHolder.session_evict(session, u) and None)
    return jsonify({
        "message": "success"
    }), 200

@user.post("/resetimg")
@current_user(id_func = lambda: request.form.get('user_id'))
def reset_image_endpoint() -> Response:
    req: ImageResetRequest = ImageResetRequest.build(request)
    user_service.image_reset(req)
    return jsonify({
        "message": "success"
    }), 200

@user.post("/update")
@token_check(options = [Role.ADMIN])
def update_user_endpoint() -> Response:
    req: UserUpdateRequest = UserUpdateRequest.build(request)
    user_service.update_user(req, lambda u: SessionHolder.session_evict(session, u) and None)
    return jsonify({
        "message": "success"
    }), 200