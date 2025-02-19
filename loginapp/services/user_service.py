
from typing import Any, List
from flask import session
from loginapp import get_connection
from loginapp.constant.user_status import UserStatus
from loginapp.exception.custom_error import AccessDeclinedError, ArgumentError, NotFoundError
from loginapp.model.data_model import User
from mysql.connector import cursor

from loginapp.model.request_model import LoginRequest, RegisterRequest
from loginapp.session_holder import SessionHolder

class UserService:

    def get_user_by_id(self, user_id: id) -> User:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT * FROM users WHERE user_id = %s", [user_id])
        return User.of(cur.fetchone())
    
    def new_user_register(self, req: RegisterRequest) -> None:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT COUNT(1) as count FROM users WHERE user_name = %s;", [req.user_name])
        if cur.fetchone()['count'] != 0:
            raise ArgumentError("this user name is existing, use another instead")
        cur.execute("INSERT INTO users (user_name, password_hash, email, first_name, last_name, location, profile_image, role, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", [req.user_name, req.password, req.email, req.first_name, req.last_name, req.location, req.profile_image, req.role.value, req.status.value])
        
    def user_login(self, req: LoginRequest) -> str:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT * FROM users WHERE user_name = %s AND password_hash = %s;", [req.user_name, req.password])
        user: User = User.of(cur.fetchone())
        if user == None:
            raise NotFoundError("user name or password is invalid")
        if UserStatus.INACTIVE is user.get_status_enum():
            raise AccessDeclinedError("login failed! current user is inactive")
        SessionHolder.session_hold(session, user)

    def list_users(self, user_name: str, first_name: str, last_name: str) -> List[User]:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        query_statement: str = "SELECT * FROM users "
        where_statement: List[str] = []
        query_args: List[Any] = []
        if any(s for s in [user_name, first_name, last_name]):
            query_statement += "WHERE "
            if user_name: 
                where_statement.append("user_name LIKE %s ")
                query_args.append(f"%{user_name}%")
            if first_name:
                where_statement.append("first_name LIKE %s ")
                query_args.append(f"%{first_name}%")
            if last_name:
                where_statement.append("last_name LIKE %s ")
                query_args.append(f"%{last_name}%")
            query_statement += "AND ".join(where_statement)
        cur.execute(query_statement, query_args)
        return User.of_all(cur.fetchall())