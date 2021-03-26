from User import db

"""
    Declaring the model class for the Loan Model for the DB
"""


class LoanModel(db.Model):

    __tablename__ = 'loan_model'

    loan_id = db.Column(db.Integer, primary_key=True)
    loan_type = db.Column(db.String(50), nullable=False)
    loan_amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(50), nullable=False)
    rate_of_interest = db.Column(db.Float, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.ForeignKey('user_model.user_id'))
    user_model = db.relationship("UserModel", backref='loan_model')

    def __init__(self, loan_type, loan_amount, date, rate_of_interest, duration, user_id):
        self.loan_amount = loan_amount
        self.loan_type = loan_type
        self.date = date
        self.rate_of_interest = rate_of_interest
        self.duration = duration
        self.user_id = user_id
