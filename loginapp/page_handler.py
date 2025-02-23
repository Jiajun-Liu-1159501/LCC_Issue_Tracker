from flask import Blueprint, render_template


page: Blueprint = Blueprint("page", __name__)

@page.get("/login")
def login_page() -> str:
    return render_template("login.html")

@page.get("/register")
def register_page() -> str:
    return render_template("signup.html")

@page.get("/")
def home_page() -> str:
    return render_template("home.html")

@page.get("/userManage")
def user_management_page() -> str:
    return render_template("user_management.html")