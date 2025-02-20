
from flask import Blueprint, request, session

from loginapp.aspect import current_user, token_check
from loginapp.constant.user_role import Role
from loginapp.model.request_model import ImageResetRequest, PasswordResetRequest, UserEditRequest, UserUpdateRequest
from loginapp.services import user_service
from loginapp.session_holder import SessionHolder

user: Blueprint = Blueprint('user', __name__)

@user.get("/list")
@token_check(options = [Role.ADMIN])
def list_users_endpoint() -> str:
    user_name: str = request.args.get('user_name', type = str)
    first_name: str = request.args.get('first_name', type = str)
    last_name: str = request.args.get('last_name', type = str)
    return user_service.list_users(user_name,  first_name, last_name)

@user.post("/edit")
@current_user(id_func = lambda: request.form.get('user_id'))
def edit_profile_endpoint() -> str:
    req: UserEditRequest = UserEditRequest.build(request)
    user_service.edit_user(req, lambda u: None)
    return "success"

@user.post("/resetpwd")
@current_user(id_func = lambda: request.form.get('user_id'))
def reset_pwd_endpoint() -> str:
    req: PasswordResetRequest = PasswordResetRequest.build(request)
    user_service.password_reset(req, lambda u: SessionHolder.session_evict(session, u) and None)
    return "success"

@user.post("/resetimg")
@current_user(id_func = lambda: request.form.get('user_id'))
def reset_image_endpoint() -> str:
    req: ImageResetRequest = ImageResetRequest.build(request)
    user_service.image_reset(req)
    return "success"

@user.post("/update")
@token_check(options = [Role.ADMIN])
def update_user_endpoint() -> str:
    req: UserUpdateRequest = UserUpdateRequest.build(request)
    user_service.update_user(req, lambda u: SessionHolder.session_evict(session, u) and None)
    return "success"