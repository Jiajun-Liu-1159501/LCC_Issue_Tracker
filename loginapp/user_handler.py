
from typing import List
from flask import Blueprint, Response, jsonify, request, session

from loginapp.aspect import current_user, token_check
from loginapp.constant.user_role import Role
from loginapp.model.data_model import User
from loginapp.model.user_req_model import ImageResetRequest, PasswordResetRequest, UserEditRequest, UserUpdateRequest
from loginapp.services import user_service
from loginapp.session_holder import SessionHolder

# Define a Flask Blueprint for user-related endpoints, grouping related routes together
user: Blueprint = Blueprint('user', __name__)

@user.get("/current")
@token_check(options = [])
def get_current_login() -> Response:
    """
    Retrieve details of the currently logged-in user, including their information and allowed operations.
    
    This endpoint helps the frontend determine user permissions and available actions.
    
    Returns:
        Response: JSON response containing the user's information and their role-based operations.
    """
    user: User = user_service.get_user_by_id(SessionHolder.current_login().user_id, None)
    return jsonify({
        "user_info": user,
        "operations": user.get_role_enum().get_allowed_operations()
    }), 200

@user.get("/list")
@token_check(options = [Role.ADMIN])
def list_users_endpoint() -> Response:
    """
    Retrieve a list of users based on optional filters such as username, first name, and last name.
    
    Query Parameters:
        user_name (str, optional): Filter by username.
        first_name (str, optional): Filter by first name.
        last_name (str, optional): Filter by last name.
    
    Returns:
        Response: JSON response containing a list of users matching the provided filters.
    """
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
    """
    Edit user profile details, such as updating name, email, or other personal information.
    
    The request must contain a valid `user_id` in the form data.
    
    Returns:
        Response: JSON response indicating whether the operation was successful.
    """
    req: UserEditRequest = UserEditRequest.build(request)
    user_service.edit_user(req, lambda u: None)
    return jsonify({
        "message": "success"
    }), 200

@user.post("/resetpwd")
@current_user(id_func = lambda: request.form.get('user_id'))
def reset_pwd_endpoint() -> Response:
    """
    Reset user password. This operation logs the user out by evicting their session after a successful password change.
    
    The request must contain a valid `user_id` in the form data.
    
    Returns:
        Response: JSON response indicating whether the password reset was successful.
    """
    req: PasswordResetRequest = PasswordResetRequest.build(request)
    user_service.password_reset(req, lambda u: SessionHolder.session_evict(session, u) and None)
    return jsonify({
        "message": "success"
    }), 200

@user.post("/resetimg")
@current_user(id_func = lambda: request.form.get('user_id'))
def reset_image_endpoint() -> Response:
    """
    Reset user profile image.
    
    This operation allows a user to update or reset their profile picture.
    
    The request must contain a valid `user_id` in the form data.
    
    Returns:
        Response: JSON response indicating whether the image reset was successful.
    """
    req: ImageResetRequest = ImageResetRequest.build(request)
    user_service.image_reset(req)
    return jsonify({
        "message": "success"
    }), 200

@user.post("/update")
@token_check(options = [Role.ADMIN])
def update_user_endpoint() -> Response:
    """
    Update user details. This operation is restricted to administrators.
    
    This allows an admin to modify user information, such as role changes or status updates.
    
    The request must contain valid user details in the form data.
    
    Returns:
        Response: JSON response indicating whether the update was successful.
    """
    req: UserUpdateRequest = UserUpdateRequest.build(request)
    user_service.update_user(req, lambda u: SessionHolder.session_evict(session, u) and None)
    return jsonify({
        "message": "success"
    }), 200