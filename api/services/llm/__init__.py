from flask import Blueprint

blueprint = Blueprint(
    'llm',
    __name__,
    url_prefix='/llm',
    template_folder='templates',
    static_folder='static'
)
