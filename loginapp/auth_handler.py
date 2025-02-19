from flask import Blueprint, render_template, request, session, url_for
from mysql.connector import cursor
from loginapp import get_connection
from loginapp.model.request_model import LoginRequest
from loginapp.session_holder import SessionHolder
from loginapp.model.data_model import User

auth: Blueprint = Blueprint('auth', __name__)

@auth.post('/register')
def register_func() -> str:
    pass

@auth.post('/login')
def login_func() -> str:
    req: LoginRequest = LoginRequest.build(request)
    cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
    cur.execute("SELECT * FROM users WHERE user_name = %s AND password_hash = %s", [req.user_name, req.password])
    user: User = User.of(cur.fetchone())
    SessionHolder.session_hold(session, user)
    return session['token']

@auth.post("/logout")
def logout_func() -> str:
    SessionHolder.session_evict(session, None)
    return render_template(url_for(""))