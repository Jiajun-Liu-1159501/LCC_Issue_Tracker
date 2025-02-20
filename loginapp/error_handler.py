from flask import Flask
from loginapp.exception.custom_error import *


def init_error_handlers(app: Flask) -> None:

    @app.errorhandler(ArgumentError)
    def argument_error_handler(error: ArgumentError) -> str:
        return error.message

    @app.errorhandler(NotFoundError)
    def not_found_error_handler(error: NotFoundError) -> str:
        return error.message
    
    @app.errorhandler(Exception)
    def unknown_error_handler(error: Exception) -> str:
        return error