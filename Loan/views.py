from flask import abort, request
from flask_restful import Resource
from Loan.model import LoanModel
from User.auth import check_token
from Loan.schema import loanModelSchema
from Loan import api
from User import db


class LoanList(Resource):

    """
        URI for getting User Specific Loan
    """

    def get(self, loanId):

        logged_user = check_token()

        called_loan = LoanModel.query.filter_by(loan_id=loanId).first()
        if called_loan is None:
            abort(404, f"Loan ID: {loanId} Does Not Exist")

        if logged_user.user_id == called_loan.user_id:
            return loanModelSchema.jsonify(called_loan)
        else:
            abort(403, f"Loan ID:{loanId} Does Not Belong to you")


class LoanInit(Resource):

    """
        URI for creating User Specific Loan
    """

    def post(self):

        logged_user = check_token()

        errors = loanModelSchema.validate(request.json)
        if errors:
            abort(400, str(errors))

        try:
            current_loan = LoanModel(loan_type=request.json['loan_type'], loan_amount=request.json['loan_amount'],
                date=request.json['date'], rate_of_interest=request.json['rate_of_interest'],
                duration=request.json['duration'], user_id=logged_user.user_id)

            db.session.add(current_loan)
            db.session.commit()

            return loanModelSchema.jsonify(current_loan)

        except:
            return "Invalid Data", 400


api.add_resource(LoanList, '/loans/<loanId>')
api.add_resource(LoanInit, '/loans/')
