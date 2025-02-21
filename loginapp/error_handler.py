from flask import Flask, Response, jsonify
from loginapp.exception.custom_error import *


def init_error_handlers(app: Flask) -> None:

    @app.errorhandler(ArgumentError)
    def argument_error_handler(error: ArgumentError) -> Response:
        return jsonify({
            "err": error.get_error_args()
        }), 400
    
    @app.errorhandler(UnauthorizedError)
    def unauthorized_error_handler(error: UnauthorizedError) -> Response:
        return jsonify({
            "err": error.message
        }), 401

    @app.errorhandler(NotFoundError)
    def not_found_error_handler(error: NotFoundError) -> Response:
        return jsonify({
            "err": error.message
        }), 404
    
    @app.errorhandler(AccessDeclinedError)
    def declined_error_handler(error: AccessDeclinedError) -> Response:
        return jsonify({
            "err": error.message
        }), 403
    
    @app.errorhandler(Exception)
    def unknown_error_handler(error: Exception) -> Response:
        print(error)
        return jsonify({
            "err": "service unavilable"
        }), 500