from flask import Blueprint, render_template, request, session, url_for
from mysql.connector import cursor
from loginapp import get_connection
from loginapp.constant.user_status import UserStatus
from loginapp.exception.custom_error import AccessDeclinedError, ArgumentError, NotFoundError
from loginapp.model.request_model import LoginRequest, RegisterRequest
from loginapp.services import user_service
from loginapp.session_holder import SessionHolder
from loginapp.model.data_model import User

auth: Blueprint = Blueprint('auth', __name__)

@auth.post('/register')
def register_endpoint() -> str:
    req: RegisterRequest = RegisterRequest.build(request)
    user_service.new_user_register(req)
    return "success"

@auth.post('/login')
def login_endpoint() -> str:
    req: LoginRequest = LoginRequest.build(request)
    user_service.user_login(req, lambda u: SessionHolder.session_hold(session, u) and u)
    return "success"

@auth.post("/logout")
def logout_endpoint() -> str:
    SessionHolder.session_evict(session, None)
    return "success"