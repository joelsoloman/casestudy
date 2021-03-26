from User import db

#  User Model

"""
    Declaring the model class for the User Model for the DB
"""


class UserModel(db.Model):

    __tablename__ = 'user_model'

    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False)
    state = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    pan = db.Column(db.String(50), unique=True, nullable=False)
    contactNo = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(50), nullable=False)
    account_type = db.Column(db.String(50), nullable=False)

    def __init__(self, email, name, username, password, address, state, country, pan, contactNo, dob, account_type):
        self.email = email
        self.name = name
        self.username = username
        self.password = password
        self.address = address
        self.state = state
        self.country = country
        self.pan = pan
        self.contactNo = contactNo
        self.dob = dob
        self.account_type = account_type
