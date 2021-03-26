from User import ma, db
from marshmallow import fields
from marshmallow.validate import Length, Email, Regexp

#   User Schema

"""
    Declaring the Marshmallow Shema class for the Loan Model
"""


class UserModelSchema(ma.SQLAlchemySchema):

    email = fields.Str(required=True, validate=Email())
    name = fields.Str(required=True, validate=[Length(min=3), Regexp(r'^[ A-Za-z]+$', error="Invalid Name")])
    username = fields.Str(required=True, validate=Length(min=3))
    password = fields.Str(required=True, validate=Length(min=8))
    address = fields.Str(required=True, validate=Length(min=3))
    state = fields.Str(required=True, validate=[Length(min=3), Regexp(r'^[ A-Za-z]+$', error="Invalid State")])
    country = fields.Str(required=True, validate=[Length(min=3), Regexp(r'^[ A-Za-z]+$', error="Invalid Country")])
    pan = fields.Str(required=True, validate=Length(min=8))
    contactNo = fields.Str(required=True, validate=[Length(equal=10), Regexp(r'^[0-9]+$', error="Invalid Contact Number")])
    dob = fields.Str(required=True, validate=Length(min=3))
    account_type = fields.Str(required=True, validate=[Length(min=3), Regexp(r'^[ A-Za-z]+$', error="Invalid Account Type")])

    class Meta:
        fields = ('email', 'name', 'username', 'password', 'address', 'state', 'country', 'pan', 'contactNo', 'dob', 'account_type')

#   Corresponding Schema Objects


db.create_all()
userModelSchema = UserModelSchema()
