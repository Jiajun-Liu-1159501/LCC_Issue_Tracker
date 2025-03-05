"""
Authentication Blueprint for LoginApp

This module provides API endpoints for user authentication, including registration, login, and logout.
It utilizes Flask's Blueprint for modular routing and integrates with a session-based authentication system.

Modules:
    - flask: Provides Flask Blueprint, Response, and session management.
    - loginapp.model.data_model: Defines the User model.
    - loginapp.model.user_req_model: Contains request models for login and registration.
    - loginapp.services: Implements user-related business logic.
    - loginapp.session_holder: Manages user sessions.

Endpoints:
    - POST /register: Registers a new user.
    - POST /login: Logs in a user and starts a session.
    - POST /logout: Logs out a user and clears the session.
"""

from flask import Blueprint, Response, jsonify, request, session
from loginapp.model.data_model import User
from loginapp.model.user_req_model import LoginRequest, RegisterRequest
from loginapp.services import user_service
from loginapp.session_holder import SessionHolder

auth: Blueprint = Blueprint('auth', __name__)

@auth.post('/register')
def register_endpoint() -> str:
    """
    Handle user registration.
    
    Parses the request data, creates a new user, and stores it in the database.
    
    Returns:
        Response: JSON response indicating success or failure.
    """
    req: RegisterRequest = RegisterRequest.build(request)
    user_service.new_user_register(req)
    return jsonify({
        "message": "success",
    }), 200

@auth.post('/login')
def login_endpoint() -> Response:
    """
    Handle user login.
    
    Validates user credentials and establishes a session if authentication is successful.
    
    Returns:
        Response: JSON response indicating success or failure.
    """
    req: LoginRequest = LoginRequest.build(request)
    user: User = user_service.user_login(req, lambda u: SessionHolder.session_hold(session, u) and u)
    return jsonify({
        "message": "success",
    }), 200

@auth.post("/logout")
def logout_endpoint() -> str:
    """
    Handle user logout.
    
    Clears the user session and logs the user out.
    
    Returns:
        Response: JSON response indicating success.
    """
    SessionHolder.session_evict(session, None)
    return jsonify({
        "message": "success",
    }), 200