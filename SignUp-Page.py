from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"]= "mongodb://localhost:27017/MiniProject"
Mongo= PyMongo(app)
db= Mongo.db


@app.route('/')
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    
    # Perform form validation here
    errors = []
    if password != confirm_password:
        errors.append("Passwords do not match")
        
    # Add more validation as needed
    
    if errors:
        return render_template('signup.html', errors=errors)
    else:
        # If form is valid, process signup logic here
        # This is where you would typically save the user to the database
        return "Signup successful"

if __name__ == '__main__':
    app.run(debug=True)



