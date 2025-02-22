from dataclasses import dataclass
import re
from flask import Request

from loginapp.constant.user_role import Role
from loginapp.constant.user_status import UserStatus
from loginapp.exception.custom_error import ArgumentError


@dataclass
class RegisterRequest:

    user_name: str
    password: str
    email: str
    first_name: str
    last_name: str
    location: str
    profile_image: str
    role: Role
    status: UserStatus

    def build(request: Request) -> 'RegisterRequest':
        model: RegisterRequest =  RegisterRequest(
            request.form.get('user_name'),
            request.form.get('password'),
            request.form.get('email'),
            request.form.get('first_name'),
            request.form.get('last_name'),
            request.form.get('location'),
            request.form.get('profile_image', ''),
            Role.VISIOTR,
            UserStatus.ACTIVE
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        if not self.user_name: raise ArgumentError("user_name", "not a valid user name input")
        if (not self.password) or (not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", self.password)): raise ArgumentError("password", "at least 8 chars including number and letter")
        if (not self.email) or (not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.email)): raise ArgumentError("email", "not a valid email format")
        if not self.first_name: raise ArgumentError("first_name", "not a valid first name input")
        if not self.last_name: raise ArgumentError("last_name", "not a valid last name input")
        if not self.location: raise ArgumentError("location", "not a valid location input")


@dataclass
class LoginRequest:

    user_name: str
    password: str

    @staticmethod
    def build(request: Request) -> 'LoginRequest':
        model: LoginRequest =  LoginRequest(
            request.form.get('user_name'),
            request.form.get('password')
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        if not self.user_name: raise ArgumentError("user_name", "not a valid user name input")
        if (not self.password) or (not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", self.password)): raise ArgumentError("password", "not a valid password input")


@dataclass
class UserEditRequest:

    user_id: int
    email: str
    first_name: str
    last_name: str
    location: str

    def build(request: Request) -> 'UserEditRequest':
        model: UserEditRequest = UserEditRequest(
            int(request.form.get('user_id')),
            request.form.get('email'),
            request.form.get('first_name'),
            request.form.get('last_name'),
            request.form.get('location')
        )
        model.verify()
        return model

    def verify(self) -> None:
        if (not self.email) or (not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.email)): raise ArgumentError("email", "not a valid email input")
        if not self.first_name: raise ArgumentError("first_name", "not a valid first name input")
        if not self.last_name: raise ArgumentError("last_name", "not a valid last name input")
        if not self.location: raise ArgumentError("location", "not a valid location input")


@dataclass
class UserUpdateRequest:

    user_id: int
    status: UserStatus
    role: Role

    @staticmethod
    def build(request: Request) -> 'UserUpdateRequest':
        model: UserUpdateRequest =  UserUpdateRequest(
            int(request.form.get('user_id')),
            UserStatus.of(request.form.get('status')),
            Role.of(request.form.get('role'))
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        if not self.role: raise ArgumentError("invalid user role input")
        if not self.status: raise ArgumentError("invalid user status input")


@dataclass
class PasswordResetRequest:

    user_id: int
    new_password: str

    @staticmethod
    def build(request: Request) -> 'PasswordResetRequest':
        model: PasswordResetRequest =  PasswordResetRequest(
            int(request.form.get('user_id')),
            request.form.get('new_password')
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        if (not self.new_password) or (not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", self.new_password)): raise ArgumentError("password","not a valid password input")


@dataclass
class ImageResetRequest:
    
    user_id: int
    image_content: str

    @staticmethod
    def build(request: Request) -> 'ImageResetRequest':
        model: UserUpdateRequest =  UserUpdateRequest(
            int(request.form.get('user_id')),
            request.form.get('image_content', "")
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        pass