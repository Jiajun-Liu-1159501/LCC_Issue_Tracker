from xml.dom import NotFoundErr
from loginapp import app, get_connection
from flask import Flask, Response, flash, g, render_template, request, session
from mysql.connector import pooling, cursor
from model import User

@app.post("/api/login")
def login() -> str:
    user_name: str = request.form.get("user_name")
    password: str = request.form.get("password")
    cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
    cur.execute("SELECT * FROM users WHERE user_name = %s AND password = %s", [user_name, password])
    user: User = User.of(cur.fetchone())
    if user == None:
        raise NotFoundErr()
    session.setdefault('user', user)
    return render_template(user.get_role_enum().get_home_page())
        

@app.post("/api/logout")
def logout() -> str:
    pass