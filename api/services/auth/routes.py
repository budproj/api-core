from flask import session, redirect
from api import core_oauth
from . import blueprint


@blueprint.route('/callback', methods=['GET', 'POST'])
def callback():
    token = core_oauth.auth0.authorize_access_token()  # type: ignore
    session['user'] = token
    return redirect('/')
