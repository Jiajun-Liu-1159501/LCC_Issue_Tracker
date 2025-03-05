from flask import Blueprint, render_template

"""
Defines route handlers for rendering HTML pages in a Flask web application.

This class sets up a Flask Blueprint named "page" and maps various URL paths
to their respective HTML templates for user authentication, issue tracking,
and user management.
"""

page: Blueprint = Blueprint("page", __name__)

@page.get("/login")
def login_page() -> str:
    """
    Renders the login page.
    
    Returns:
        str: The rendered HTML content of the login page.
    """
    return render_template("login.html")

@page.get("/register")
def register_page() -> str:
    """
    Renders the user registration page.
    
    Returns:
        str: The rendered HTML content of the signup page.
    """
    return render_template("signup.html")

@page.get("/")
def home_page() -> str:
    """
    Renders the home page.
    
    Returns:
        str: The rendered HTML content of the home page.
    """
    return render_template("home.html")

@page.get("/userManage")
def user_management_page() -> str:
    """
    Renders the user management page, which provides administrative tools for managing users.
    
    Returns:
        str: The rendered HTML content of the user management page.
    """
    return render_template("user_management.html")

@page.get("/myIssues")
def my_issues_page() -> str:
    """
    Renders the "My Issues" page, displaying issues assigned to the currently logged-in user.
    
    Returns:
        str: The rendered HTML content of the "My Issues" page.
    """
    return render_template("my_issues.html")

@page.get("/allIssues")
def all_issues_page() -> str:
    """
    Renders the "All Issues" page, which displays all reported issues in the system.
    
    Returns:
        str: The rendered HTML content of the "All Issues" page.
    """
    return render_template("all_issues.html")