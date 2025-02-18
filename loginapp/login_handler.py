from loginapp import app, get_connection
from flask import Flask, Response, flash, g, render_template, request
from mysql.connector import pooling, cursor
from model import User

@app.post("/api/login")
def login() -> str:
    user_name: str = request.form.get("user_name")
    password: str = request.form.get("password")
    cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
    cur.execute("SELECT * FROM users WHERE user_name = %s, password = %s")
    user: User = User.of(cur.fetchone())
    if user == None:
        pass
        

@app.post("/api/logout")
def logout() -> str:
    pass