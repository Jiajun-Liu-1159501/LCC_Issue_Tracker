from dataclasses import dataclass
import re
from typing import TypeVar
from flask import Request

from loginapp.exception.custom_error import ArgumentError

LRV = TypeVar('LoginRequest')

@dataclass
class LoginRequest:

    user_name: str
    password: str

    @staticmethod
    def build(request: Request) -> LRV:
        model: LoginRequest =  LoginRequest(
            request.form.get('user_name'),
            request.form.get('password')
        )
        model.verify()
        return model
    
    def verify(self) -> None:
        if not self.user_name: raise ArgumentError("not a valid user name input")
        if not self.password: raise ArgumentError("not a valid password input")
