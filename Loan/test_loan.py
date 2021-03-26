from unittest import mock
from Loan.model import LoanModel
from User.model import UserModel
from Loan import app


test_user_object = UserModel(account_type="test",
    address="test",
    contactNo=9761348520,
    country="test",
    dob="test",
    email="test@test.com",
    name="test",
    pan="TEST1234",
    password="12345678",
    state="test",
    username="test",
    )

test_loan = {
    "loan_type": "TestLoan",
    "loan_amount": 4,
    "date": "test",
    "rate_of_interest": 15.00,
    "duration": 15,
    "user_id": 1
}

test_loan_object = LoanModel(loan_amount=5, loan_type='TestLoan', date='test', rate_of_interest=15, duration=15, user_id=1)

tester = app.test_client()


""" ---- POST LOAN --- """


# Create a Duplicate Loan that Causes Invalid Data
@mock.patch("Loan.views.check_token")
@mock.patch("Loan.views.db.session.commit", side_effect=Exception())
def test_400_post_loan(mocked_object, mocked_commit):
    test_loan['loan_name'] = ""
    response = tester.post('/loans/', json=test_loan)
    status = response.status_code
    assert status == 400


# Create a Loan with Valdiations Errors
@mock.patch("Loan.views.check_token")
def test_400_post_loan_validation(mocked_object):
    test_loan['loan_name'] = ""
    response = tester.post('/loans/', json=test_loan)
    status = response.status_code
    assert status == 400


""" ---- GET LOAN ---- """


# No Permission due to Different User
@mock.patch("Loan.views.check_token")
def test_403_get_Loan(mocked_object):
    response = tester.get('/loans/1')
    status = response.status_code
    assert status == 403


# No Such Loan Found Test
@mock.patch("Loan.views.check_token")
def test_404_get_Loan(mocked_object):
    response = tester.get('/loans/99')
    status = response.status_code
    assert status == 404
