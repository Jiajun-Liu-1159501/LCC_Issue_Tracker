from flask import Blueprint, render_template, request, session, url_for
from mysql.connector import cursor
from loginapp import get_connection
from loginapp.exception.custom_error import ArgumentError, NotFoundError
from loginapp.model.request_model import LoginRequest, RegisterRequest
from loginapp.session_holder import SessionHolder
from loginapp.model.data_model import User

auth: Blueprint = Blueprint('auth', __name__)

@auth.post('/register')
def register_func() -> str:
    req: RegisterRequest = RegisterRequest.build(request)
    cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
    cur.execute("SELECT COUNT(1) as count FROM users WHERE user_name = %s;", [req.user_name])
    if cur.fetchone()['count'] != 0:
        raise ArgumentError("this user name is existing, use another instead")
    cur.execute("INSERT INTO users (user_name, password_hash, email, first_name, last_name, location, profile_image, role, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", [req.user_name, req.password, req.email, req.first_name, req.last_name, req.location, req.profile_image, req.role.value, req.status.value])
    return "success"

@auth.post('/login')
def login_func() -> str:
    req: LoginRequest = LoginRequest.build(request)
    cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
    cur.execute("SELECT * FROM users WHERE user_name = %s AND password_hash = %s;", [req.user_name, req.password])
    user: User = User.of(cur.fetchone())
    if user == None:
        raise NotFoundError("user name or password is invalid")
    SessionHolder.session_hold(session, user)
    return "success"

@auth.post("/logout")
def logout_func() -> str:
    SessionHolder.session_evict(session, None)
    return "success"