from flask import Blueprint

blueprint = Blueprint(
    'dashboard',
    __name__,
    url_prefix='/core/dashboard',
    template_folder='templates',
    static_folder='static'
)
