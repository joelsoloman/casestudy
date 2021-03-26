from flask_restful import Resource
from flask import request, abort
from User.auth import check_token
from User.model import UserModel
from User.schema import userModelSchema
from User import db, api, app
import jwt
import datetime


class UserLogin(Resource):

    """
        URI for User Login and Token Generation
    """

    def post(self):
        current_username = request.json['username']
        current_password = request.json['password']
        called_user = UserModel.query.filter_by(username=current_username).first()
        if called_user is None:
            return "Inavlid Username", 404
        elif current_password == called_user.password:
            token = jwt.encode({'public_id': called_user.user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return token
        else:
            return "Invalid Password", 400


class UserRegistration(Resource):

    """
        URI for User Registration
    """

    def post(self):
        errors = userModelSchema.validate(request.json)
        if errors:
            abort(400, str(errors))
        try:
            new_user = UserModel(email=request.json['email'], 
                name=request.json['name'], username=request.json['username'], password=request.json['password'],
                address=request.json['address'], state=request.json['state'], country=request.json['country'],
                pan=request.json['pan'], contactNo=request.json['contactNo'], dob=request.json['dob'],
                account_type=request.json['account_type'])

            db.session.add(new_user)
            db.session.commit()
            return f"Congratulations {request.json['name']}! Your Account was created", 201

        except:
            return "User Already Exists", 400


def get_current_user_from_token(userId):

    """
        Call the Authentication function to obtain the UserModel
    """

    logged_in_user = check_token()

    if logged_in_user.user_id != userId:
        abort(403, "Not Your Profile")

    return logged_in_user


class UserUpdate(Resource):

    """
        URI for viewing and Editing User Details
    """

    # View own User
    def get(self, userId):

        called_user = get_current_user_from_token(userId)
        return userModelSchema.jsonify(called_user)

    # Edit own User
    def put(self, userId):

        called_user = get_current_user_from_token(userId)

        errors = userModelSchema.validate(request.json)
        if errors:
            abort(400, str(errors))

        try:
            called_user.email = request.json['email']
            called_user.name = request.json['name']
            called_user.username = request.json['username']
            called_user.password = request.json['password']
            called_user.address = request.json['address']
            called_user.state = request.json['state']
            called_user.country = request.json['country']
            called_user.pan = request.json['pan']
            called_user.contactNo = request.json['contactNo']
            called_user.dob = request.json['dob']
            called_user.account_type = request.json['account_type']

            db.session.commit()
            return userModelSchema.jsonify(called_user)

        except:
            return 'Credentials already Exists', 400


api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserUpdate, '/users/<int:userId>')
