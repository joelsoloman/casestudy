### Bank Management System

# User Package:

**_User_** Should be able to:

1. _Register_ by creating a User
2. _Login_ with credentials
3. _Get_ his own Details
4. _Edit_ his own Details

>The User app is run by the "run.py" on port 6000

# Loan Package:

**_Logged user_** Should be able to:

1. _Create_ a Loan
2. _View_ the Created Loan or Any loan the Logged user has

>The Loan app is run by the "run_loan.py" on port 5000

## Setup

# User Application

1. Start the Virtual Environment and set flask app variable to _run.py_
2. Run the flask app with _flask run --port=6000_ command to start the User app on port 6000
3. Create an User at the URI **_"localhost:6000/register"_**
4. Login the User at the URI **_"localhost:6000/login"_**, The _token_ gets generated.
5. Use the Generated Token to get the User by providing the ID at the URI **_"localhost:6000/users/<Your_User_ID>"_**
6. Use the Generated Token to update the User by providing the ID at the URI **_"localhost:6000/users/<Your_User_ID>"_**

# Loan Application

1. Start the Virtual Environment and set flask app variable to _run-loan.py_
2. Run the flask app with _flask run_ command to start the Loan app on port 5000
3. Create the Loan for the Logged in user by providing the token at the URI **_"localhost:5000/loans/_**
4. View the Created loan for the user by providing the token and loan_id at the URI **_"localhost:5000/loans/<Your_Loan_ID>_**

>The two apps will work on Microservice basis however the Loan application requires the active token from the user application in order to allow permission to the functionality