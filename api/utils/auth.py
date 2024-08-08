from functools import wraps
import jwt
import base64

from flask import abort, request, session, url_for
from sqlalchemy.orm import joinedload
from api import core_oauth, core_db
from api.models.db import DB_MAP
from api.models.db.team import Team
from api.models.db.user import User


SCOPES = ['company', 'team', 'owns']


class PermissionController:
    '''Controller to check if user has minimum permissions to selected entity

    Attributes:
        sub: authz_sub as on database
        model: entity model as defined on models.DB_MAP
        entity_id: id to search for on table column `id`
    '''

    def __init__(self, sub: str, entity: str, entity_id: str):
        '''Initializes controller with user sub and entity

        Args:
            sub: authz_sub as on database
            entity: entity table name
            entity_id: id to search for on table column `id`
        '''
        self.entity_id = entity_id
        self.model = DB_MAP[entity]
        self.sub = sub

    def verify(self, scope: str) -> bool:
        '''Verifies if current user has permission to access entity
        based on scope

        Args:
            scope: auth scope in 'entity:action:scope'

        Returns:
            True if user has permission
        '''
        if scope == 'owns':
            return self._user_owns_entity()
        if scope == 'team':
            return self._user_team_owns_entity()
        if scope == 'company':
            return self._user_company_owns_entity()
        return False

    def _user_owns_entity(self) -> bool:
        '''Verifies if current entity has owner_id as the user id'''
        cur_user: User | None = core_db.session.query(
            User
        ).filter_by(
            authz_sub=self.sub
        ).one()
        cur_obj = core_db.session.query(
            self.model).filter_by(id=self.entity_id).one()

        return cur_user.id == cur_obj.owner_id

    def _user_team_owns_entity(self) -> bool:
        '''Verifies if current entity has team_id as the user team id'''
        cur_user: User | None = core_db.session.query(User).filter_by(
            authz_sub=self.sub
        ).options(
            joinedload(User.teams),
        ).one()
        cur_obj = core_db.session.query(
            self.model).filter_by(id=self.entity_id).one()

        for team in cur_user.teams:
            if team.id == cur_obj.team_id:
                return True
        return False

    def _user_company_owns_entity(self) -> bool:
        '''Verifies if current entity has team.company_id
        as the user company id'''
        cur_user: User | None = core_db.session.query(User).filter_by(
            authz_sub=self.sub
        ).options(
            joinedload(User.teams),
            joinedload(User.teams).joinedload(Team.company),
        ).one()
        cur_obj = core_db.session.query(self.model).filter_by(
            id=self.entity_id
        ).one()

        for team in cur_user.teams:
            if team.company.id == cur_obj.team.company.id:
                return True
        return False


def requires_auth(permission=None):
    '''
    Use on routes that require a valid session, otherwise it aborts with a 403
    '''
    def _decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            user = session.get('user')
            print(user)
            if user is None:
                return core_oauth.auth0.authorize_redirect(  # type: ignore
                    redirect_uri=url_for('auth.callback', _external=True)
                )
            if permission is not None:
                # Get user permissions
                granted_permissions = []
                for p in user['userinfo']["'https://api.getbud.co'/permissions"]:
                    if p.startswith(permission):
                        granted_permissions.append(p)
                granted_scope = ''
                for scope in SCOPES:
                    if f'{permission}:{scope}' in granted_permissions:
                        granted_scope = scope
                        break
                entity, _ = permission.split(':')
                entity_id_param = f'{entity.replace('-', '_')}_id'

                controller = PermissionController(
                    user['userinfo']['sub'], entity, kwargs[entity_id_param])
                if not controller.verify(granted_scope):
                    return abort(403)

            return f(*args, **kwargs)
        return wrapper
    return _decorator
