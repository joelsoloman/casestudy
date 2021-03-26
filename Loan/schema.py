from User import db
from Loan import ma
from marshmallow import fields
from marshmallow.validate import Length, Range, Regexp


""" 
    Declaring the Marshmallow Shema class for the Loan Model
"""


class LoanModelSchema(ma.SQLAlchemySchema):

    loan_type = fields.Str(required=True, validate=[Length(min=3), Regexp(r'^[ A-Za-z]+$', error="Invalid Loan Type")])
    loan_amount = fields.Float(required=True, validate=Range(min=1))
    date = fields.Str(required=True, validate=Length(min=3))
    rate_of_interest = fields.Float(required=True, validate=Range(min=1.0, max=100.0))
    duration = fields.Integer(required=True, validate=Range(min=1))

    class Meta:
        fields = ('loan_type', 'loan_amount', 'date', 'rate_of_interest', 'duration', 'user_id')
        include_fk = True


db.create_all()
loanModelSchema = LoanModelSchema()
