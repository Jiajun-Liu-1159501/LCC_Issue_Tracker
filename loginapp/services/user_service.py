
from typing import Any, Callable, List
from loginapp import T, get_connection
from loginapp.constant.user_status import UserStatus
from loginapp.exception.custom_error import AccessDeclinedError, ArgumentError, NotFoundError, OperationNotAllowedError
from loginapp.model.data_model import User
from mysql.connector import cursor

from loginapp.model.user_req_model import ImageResetRequest, LoginRequest, PasswordResetRequest, RegisterRequest, UserEditRequest, UserUpdateRequest

class UserService:

    def get_user_by_id(self, user_id: int) -> User:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT * FROM users WHERE user_id = %s", [user_id])
        return User.of(cur.fetchone())
    
    def new_user_register(self, req: RegisterRequest) -> None:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT COUNT(1) as count FROM users WHERE user_name = %s;", [req.user_name])
        if cur.fetchone()['count'] != 0:
            raise ArgumentError("this user name is existing, use another instead")
        cur.execute("INSERT INTO users (user_name, password_hash, email, first_name, last_name, location, profile_image, role, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);", [req.user_name, req.password, req.email, req.first_name, req.last_name, req.location, req.profile_image, req.role.value, req.status.value])
        
    def user_login(self, req: LoginRequest, on_pass:Callable[[User], T]) -> T:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT * FROM users WHERE user_name = %s AND password_hash = %s;", [req.user_name, req.password])
        user: User = User.of(cur.fetchone())
        if user == None:
            raise AccessDeclinedError("user name or password is invalid")
        if UserStatus.INACTIVE is user.get_status_enum():
            raise AccessDeclinedError("login failed! current user is inactive")
        return on_pass(user) if on_pass is not None else None

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
        cur.execute(query_statement + "ORDER BY user_id DESC", query_args)
        return User.of_all(cur.fetchall())
    
    def edit_user(self, req: UserEditRequest, on_success: Callable[[User], T]) -> None:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("SELECT * FROM users WHERE user_id = %s", [req.user_id])
        user: User = User.of(cur.fetchone())
        if user.email == req.email and user.first_name == req.first_name and user.last_name == req.last_name and user.location == req.location:
            return on_success(user)
        update_statement: str = "UPDATE users SET "
        set_statement: List[str] = []
        update_args: List[str] = []
        if user.email != req.email:
            set_statement.append("email = %s ")
            update_args.append(req.email)
        if user.first_name != req.first_name:
            set_statement.append("first_name = %s ")
            update_args.append(req.first_name)
        if user.last_name != req.last_name:
            set_statement.append("last_name = %s ")
            update_args.append(req.last_name)
        if user.location != req.location:
            set_statement.append("location = %s ")
            update_args.append(req.location)
        update_statement += ", ".join(set_statement)
        update_args.append(req.user_id)
        cur.execute(update_statement + "WHERE user_id = %s;", update_args)
        return on_success(user) if on_success is not None else None

    def update_user(self, req: UserUpdateRequest, on_update: Callable[[User], T]) -> T:
        user: User = self.get_user_by_id(req.user_id)
        if (user.get_role_enum() is req.role) and (user.get_status_enum() is req.status):
            return
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        update_statement: str = "UPDATE users SET "
        set_statement: List[str] = []
        update_args: List[str] = []
        if user.get_role_enum() is not req.role:
            set_statement.append("role = %s ")
            update_args.append(req.role.value)
        if user.get_status_enum() is not req.status:
            set_statement.append("status = %s ")
            update_args.append(req.status.value)
        update_statement += ", ".join(set_statement)
        update_args.append(req.user_id)
        cur.execute(update_statement + "WHERE user_id = %s;", update_args)
        return on_update(user) if on_update is not None else None
    
    def password_reset(self, req: PasswordResetRequest, on_reset: Callable[[User], T]) -> T:
        user: User = self.get_user_by_id(req.user_id)
        if user.password == req.new_password:
            raise OperationNotAllowedError("cannot use the same password")
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("UPDATE users SET password = %s WHERE user_id = %s", [req.new_password, req.user_id])
        return on_reset(user) if on_reset is not None else None
    
    def image_reset(self, req: ImageResetRequest) -> None:
        cur: cursor.MySQLCursor = get_connection().cursor(dictionary = True, buffered = False)
        cur.execute("UPDATE users SET  = %s WHERE user_id = %s", [req.image_content, req.user_id])