from flask import Blueprint

blueprint = Blueprint(
    'auth',
    __name__,
    url_prefix='/core/auth',
    template_folder='templates',
    static_folder='static'
)
