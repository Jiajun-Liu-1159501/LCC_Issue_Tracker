from loginapp import app
from loginapp.exception.custom_error import *

@app.errorhandler(ArgumentError)
def argument_error_handler(err: ArgumentError) -> str:
    pass

@app.errorhandler(NotFoundError)
def not_found_error_handler(err: NotFoundError) -> str:
    pass