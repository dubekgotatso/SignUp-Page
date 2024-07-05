from flask import jsonify, request, render_template, url_for, redirect
from ..models.user import User
from .. import mongo




# landing page
def landing():
        return render_template("index.html")



def signup():
  # Extract form data
    if request.method == 'POST':
        
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists
        existing_user = mongo.db.signup.find_one({'$or': [{'username': username}, {'email': email}]})
        
        if existing_user:
            return 'Username or email already exists!'

        # Insert new user into the database
        signupdetails = {'username': username, 'email': email, 'password': password}
       
        
        User.create_user(signupdetails)
        # Redirect to login page or homepage
        return render_template('Login-Page.html')

    # Render the signup form template
    return render_template('SignUp-Page.html')



def signupClient():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists
        existing_user = mongo.db.SignUp_Client.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            return 'Username or email already exists!'

        # Insert new user into the database
        SignUpClientdetails = {'username': username, 'email': email, 'password': password}
        mongo.db.SignUp_Client.insert_one(SignUpClientdetails)
        User.create_user(SignUpClientdetails)
        # Redirect to login page or homepage
        return redirect(url_for('loginClient'))

    # Render the signup form template
    return render_template('SignUp_Client.html')


def login():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        password = request.form['password']

       
        existing_user = mongo.db.signup.find_one({'username': username, 'password': password})
        if existing_user:
            # Redirect to homepage or some other route
            return render_template("landing.html")
        else:
            # User not found, display error message
            return 'Invalid username or password'

    # Render the login form template
    return render_template('Login-Page.html')

