# This script runs automatically when our `loginapp` module is first loaded,
# and handles all the setup for our Flask app.
from nturl2path import url2pathname
from flask import Flask, g
from typing import Dict, Any, TypeVar
from mysql.connector import pooling, cursor
# Set up database connection.
from loginapp import connect
from loginapp.error_handler import init_error_handlers

T = TypeVar("T")

def _init_connection_pool() -> pooling.MySQLConnectionPool:
    """
    init database connection pool using args in connect.py given,
    using single database conection in mutiple threads web application environment is not thread safey
    """
    db_config: Dict[str, Any] = {
        "host": connect.dbhost,
        "port": connect.dbport,
        "user": connect.dbuser,
        "password": connect.dbpass,
        "database": connect.dbname,
        "autocommit": True
    }
    return pooling.MySQLConnectionPool(pool_name = "db_conn_pool", pool_size = 3, **db_config) # set the max db connetion to 3

connection_pool: pooling.MySQLConnectionPool = _init_connection_pool() #use pooled objects instead single connection instance

def get_connection() -> pooling.PooledMySQLConnection:
    """Gets a MySQL database connection to use while serving the current Flask
    request.

    The first time you call this during a request, a new connection will be
    allocated from the pool. After that, any additional calls to `get_db()`
    during the same request are guaranteed to return the same connection.
    
    If you only need a MySQL cursor, and not a reference to the database, you
    can just call the `get_cursor()` function. There's no need to call
    `get_db()` first.

    You don't need to manually close the connection returned by `get_db()` - it
    will be returned to the pool automatically at the end of the Flask request.
    However, you should be sure to close any cursors that you create, including
    any created by the `get_cursor()` function.

    Returns:
        A `PooledMySQLConnection` instance.
    """
    if 'db' not in g:
        g.db = connection_pool.get_connection()
    
    return g.db

def get_cursor() -> cursor.MySQLCursor:
    """Gets a new MySQL dictionary cursor to use while serving the current
    Flask request.
    
    All cursors created by this function during a single Flask request will
    belong to the same connection. You can get a reference to that connection
    at any time during the request by calling `get_db()`.
    
    Ensure that you close all cursors before the end of the Flask request.
    
    Returns:
        A new `MySQLCursor` instance.
    """
    return get_connection().cursor(dictionary = True, buffered = False)

def _close_db(exception = None) -> None:
    """Closes the MySQL database connection associated with the current Flask
    request (if any).
    
    There should be no need to call this manually: this function is called
    automatically when the application context is torn down at the end of each
    Flask request.

    Args:
        exception: The exception that terminated the Flask request, or `None`
            if the request terminated successfully.
    """
    # Get the database connection from the current application context (the one
    # that's being torn down), or `None` if there is no connection.
    db = g.pop('db', None)
    
    if db is not None:
        db.close()


# Set the "secret key" that our app will use to sign session cookies. This can
# be anything.
# 
# Anyone with access to this key can pretend to be signed in as any user. In a
# real-world project, you wouldn't store this key in your source code. To learn
# about how to manage "secrets" like this in production code, check out
# https://blog.gitguardian.com/how-to-handle-secrets-in-python/
#
# For the purpose of your assignments, you DON'T need to use any of those more
# advanced and secure methods: it's fine to store your secret key in your
# source code like we do here.

def create_app() -> Flask:
    app: Flask = Flask(__name__)
    app.secret_key = '2025COMP639S1'
    app.teardown_appcontext(_close_db)
    register_router(app)
    init_error_handlers(app)
    return app

from loginapp.auth_handler import auth
from loginapp.user_handler import user
from loginapp.issue_handler import issue

def register_router(app: Flask) -> None:
    app.register_blueprint(auth, url_prefix = '/auth')
    app.register_blueprint(user, url_prefix = '/user')
    app.register_blueprint(issue, url_prefix = '/issue')