from flask import Blueprint, Response, jsonify, request, session, url_for
from loginapp.model.data_model import User
from loginapp.model.user_req_model import LoginRequest, RegisterRequest
from loginapp.services import user_service
from loginapp.session_holder import SessionHolder

auth: Blueprint = Blueprint('auth', __name__)

@auth.post('/register')
def register_endpoint() -> str:
    req: RegisterRequest = RegisterRequest.build(request)
    user_service.new_user_register(req)
    return "success"

@auth.post('/login')
def login_endpoint() -> Response:
    req: LoginRequest = LoginRequest.build(request)
    user: User = user_service.user_login(req, lambda u: SessionHolder.session_hold(session, u) and u)
    return jsonify({
        "home_page": "1234",
    }), 200

@auth.post("/logout")
def logout_endpoint() -> str:
    SessionHolder.session_evict(session, None)
    return "success"