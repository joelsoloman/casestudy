import jwt
from flask import request, abort
from User.model import UserModel
from User import app

"""
    Authentication part : Decoding the token to obtain the Object
"""


def token_check(f):

    def wrapper(*args, **kwargs):
        token = None
        if 'Bearer' in request.headers:
            token = request.headers['Bearer']
        if not token:
            abort(404, "No Token Present Please Login")

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = UserModel.query.filter_by(user_id=data['public_id']).first()
        except:
            abort(400, "Invalid Token")
        return f(current_user, *args, *kwargs)
    return wrapper


@token_check
def check_token(current_user):
    return current_user
