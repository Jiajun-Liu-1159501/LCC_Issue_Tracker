from dataclasses import dataclass
from flask import Request

from loginapp.constant.user_role import Role
from loginapp.constant.user_status import UserStatus
from loginapp.exception.custom_error import ArgumentError


@dataclass
class RegisterRequest:
    """
    Data class representing a user registration request.

    Attributes:
        user_name (str): The username of the user.
        password (str): The password for the user.
        email (str): The user's email address.
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        location (str): The user's location.
        profile_image (str): The user's profile image (optional).
        role (Role): The role assigned to the user (default: VISITOR).
        status (UserStatus): The status of the user (default: ACTIVE).
    """

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
        """
        Builds a RegisterRequest object from a Flask request.

        Args:
            request (Request): The Flask request object containing form data.

        Returns:
            RegisterRequest: A validated RegisterRequest object.
        """
        model: RegisterRequest =  RegisterRequest(
            request.form.get('user_name'),
            request.form.get('password'),
            request.form.get('email'),
            request.form.get('first_name'),
            request.form.get('last_name'),
            request.form.get('location'),
            request.form.get('profile_image', ''),
            Role.VISITOR,
            UserStatus.ACTIVE
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        """
        Validates the registration request data. Raises ArgumentError if validation fails.
        """
        if not self.user_name: raise ArgumentError("user_name", "not a valid user name input")
        if (not self.password) or (not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", self.password)): raise ArgumentError("password", "at least 8 chars including number and letter")
        if (not self.email) or (not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.email)): raise ArgumentError("email", "not a valid email format")
        if not self.first_name: raise ArgumentError("first_name", "not a valid first name input")
        if not self.last_name: raise ArgumentError("last_name", "not a valid last name input")
        if not self.location: raise ArgumentError("location", "not a valid location input")


@dataclass
class LoginRequest:
    """
    Data class representing a login request.

    Attributes:
        user_name (str): The username of the user.
        password (str): The user's password.
    """

    user_name: str
    password: str

    @staticmethod
    def build(request: Request) -> 'LoginRequest':
        """
        Builds a LoginRequest object from a Flask request.

        Args:
            request (Request): The Flask request object containing form data.

        Returns:
            LoginRequest: A validated LoginRequest object.
        """
        model: LoginRequest =  LoginRequest(
            request.form.get('user_name'),
            request.form.get('password')
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        """
        Validates the login request data. Raises ArgumentError if validation fails.
        """
        if not self.user_name: raise ArgumentError("user_name", "not a valid user name input")
        if (not self.password) or (not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", self.password)): raise ArgumentError("password", "not a valid password input")


@dataclass
class UserEditRequest:
    """
    Data class representing a user edit request.

    Attributes:
        user_id (int): The ID of the user to be updated.
        email (str): The updated email address.
        first_name (str): The updated first name.
        last_name (str): The updated last name.
        location (str): The updated location.
    """

    user_id: int
    email: str
    first_name: str
    last_name: str
    location: str

    def build(request: Request) -> 'UserEditRequest':
        """
        Builds a UserEditRequest object from a Flask request.

        Args:
            request (Request): The Flask request object containing form data.

        Returns:
            UserEditRequest: A validated UserEditRequest object.
        """
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
        """
        Validates the user edit request data. Raises ArgumentError if validation fails.
        """
        if (not self.email) or (not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", self.email)): raise ArgumentError("email", "not a valid email input")
        if not self.first_name: raise ArgumentError("first_name", "not a valid first name input")
        if not self.last_name: raise ArgumentError("last_name", "not a valid last name input")
        if not self.location: raise ArgumentError("location", "not a valid location input")


@dataclass
class UserUpdateRequest:
    """
    Data class representing a user update request.

    Attributes:
        user_id (int): The ID of the user to be updated.
        status (UserStatus): The updated user status.
        role (Role): The updated user role.
    """

    user_id: int
    status: UserStatus
    role: Role

    @staticmethod
    def build(request: Request) -> 'UserUpdateRequest':
        """
        Builds a UserUpdateRequest object from a Flask request.

        Args:
            request (Request): The Flask request object containing form data.

        Returns:
            UserUpdateRequest: A validated UserUpdateRequest object.
        """
        model: UserUpdateRequest =  UserUpdateRequest(
            int(request.form.get('user_id')),
            UserStatus.of(request.form.get('status')),
            Role.of(request.form.get('role'))
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        pass


@dataclass
class PasswordResetRequest:
    """
    Data class representing a password reset request.

    Attributes:
        user_id (int): The ID of the user whose password is being reset.
        new_password (str): The new password.
    """

    user_id: int
    new_password: str

    @staticmethod
    def build(request: Request) -> 'PasswordResetRequest':
        """
        Builds a PasswordResetRequest object from a Flask request.

        Args:
            request (Request): The Flask request object containing form data.

        Returns:
            PasswordResetRequest: A validated PasswordResetRequest object.
        """
        model: PasswordResetRequest =  PasswordResetRequest(
            int(request.form.get('user_id')),
            request.form.get('new_password')
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        """
        Validates the password reset request data. Raises ArgumentError if validation fails.
        """
        if (not self.new_password) or (not re.match(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$", self.new_password)): raise ArgumentError("password","not a valid password input")


@dataclass
class ImageResetRequest:
    """
    Data class representing a profile image reset request.

    Attributes:
        user_id (int): The ID of the user.
        image_content (str): The new profile image content.
    """
    
    user_id: int
    image_content: str

    @staticmethod
    def build(request: Request) -> 'ImageResetRequest':
        """
        Builds an ImageResetRequest object from a Flask request.

        Args:
            request (Request): The Flask request object containing form data.

        Returns:
            ImageResetRequest: A validated ImageResetRequest object.
        """
        model: UserUpdateRequest =  UserUpdateRequest(
            int(request.form.get('user_id')),
            request.form.get('image_content', "")
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        pass