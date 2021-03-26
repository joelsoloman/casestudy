from unittest import mock
from User import app, db
from User.model import UserModel

tester = app.test_client()

test_user = {
    "account_type": "test",
    "address": "test",
    "contactNo": "9761348520",
    "country": "test",
    "dob": "test",
    "email": "test@test.com",
    "name": "test",
    "pan": "TEST1234",
    "password": "12345678",
    "state": "test",
    "username": "test"
}

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
    username="test"
)

""" ---- POST METHOD HTTP TESTING ---- """


# Testing creating a user
@mock.patch('User.views.db.session.commit')
def test_201_create_user(mocked_commit):
    response = tester.post('/register', json=test_user)
    status = response.status_code
    assert status == 201


# Testing Creating a duplicate Answer for Failure
@mock.patch('User.views.db.session.commit', side_effect=Exception())
def test_400_create_user(mocked_error):
    response = tester.post('/register', json=test_user)
    status = response.status_code
    assert status == 400


# Testing Creating a user with Validations Errors
def test_400_create_user_validators():
    test_user['email'] = ""
    response = tester.post('/register', json=test_user)
    status = response.status_code
    assert status == 400


""" ---- GET METHOD HTTP TESTING ---- """


# Getting the User Successfully
@mock.patch('User.views.get_current_user_from_token')
def test_200_get_User(mocked_object):
    response = tester.get('/users/1')
    status = response.status_code
    assert status == 200


# Getting a User when token mismatch
@mock.patch('User.views.check_token')
def test_403_get_User(mocked_object):
    response = tester.get('/users/2')
    status = response.status_code
    assert status == 403


# Getting a User When token not present
def test_404_get_User():
    response = tester.get('user/1')
    status = response.status_code
    assert status == 404


""" ---- PUT METHOD HTTP TESTING ---- """


# Updating User Unsuccessfully By validators
@mock.patch('User.views.get_current_user_from_token')
def test_400_put_user(mocked_object):
    response = tester.put('/users/1', json=test_user)
    status = response.status_code
    assert status == 400


# Updating User Successfully
@mock.patch('User.views.get_current_user_from_token')
@mock.patch('User.views.db.session.commit')
def test_200_put_user(mocked_object, mocked_commit):
    test_user['email'] = "test@email.com"
    response = tester.put('/users/1', json=test_user)
    status = response.status_code
    assert status == 200


# Unique Constraint not Matching error leading to a 400
@mock.patch('User.views.get_current_user_from_token')
@mock.patch('User.views.db.session.commit', side_effect=Exception())
def test_400_put_user_validators(mocked_object, mocked_commit):
    response = tester.put('/users/1', json=test_user)
    status = response.status_code
    assert status == 400


""" --- LOGIN TESTING --- """


# Testing 'No such user Found' case
def test_404_user_login():
    response = tester.post('/login', json={"username": "test", "password": "12345678"})
    status = response.status_code
    assert status == 404


# Successfully Logged in
def test_200_user_login():
    db.session.add(test_user_object)
    db.session.commit()
    response = tester.post('/login', json={"username": "test", "password": "12345678"})
    status = response.status_code
    assert status == 200


# Incorrect Password Scenario
def test_400_user_login():
    response = tester.post('/login', json={"username": "test", "password": "12345687"})
    status = response.status_code
    db.session.delete(test_user_object)
    db.session.commit()
    assert status == 400
