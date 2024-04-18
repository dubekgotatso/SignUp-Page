from flask import Flask, render_template, request, redirect, url_for,session
from flask_pymongo import PyMongo
from bson.objectid import *




app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/MiniProject'
mongo = PyMongo(app)
db = mongo.db

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists
        existing_user = db.signup.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            return 'Username or email already exists!'

        # Insert new user into the database
        signupdetails = {'username': username, 'email': email, 'password': password}
        db.signup.insert_one(signupdetails)
        
        # Redirect to login page or homepage
        return redirect(url_for('login'))

    # Render the signup form template
    return render_template('SignUp-Page.html')

# Login Page

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        password = request.form['password']

       
        existing_user = db.signup.find_one({'username': username, 'password': password})
        if existing_user:
            # Redirect to homepage or some other route
            return render_template("landing.html")
        else:
            # User not found, display error message
            return 'Invalid username or password'

    # Render the login form template
    return render_template('Login-Page.html')

# Booking
@app.route("/Booking", methods=["GET", "POST"])
def view_bookings():
    user_id = session.get('user_id')
    if user_id:
        bookings = mongo.db.booking.find({'user_id': ObjectId(user_id)})
        if bookings.count()== 0:
           return render_template('bookings.html', bookings=bookings)
    return render_template("bookings.html") 

@app.route("/AddBooking", methods=["GET", "POST"])
def addbooking():
  if request.method == 'POST':
      category = request.form["category"]
      time = request.form["time"]
      date = request.form["date"]
      price = request.form["price"]
      
      booking = {"category":category,"time":time,"date":date,"price":price}
      db.booking.insert_one(booking)
      if ('form submission success'):
                     return render_template("bookings.html")
      else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
               
  return render_template("Addbooking.html")



@app.route("/")
def landingPage():
    return render_template("testing.html")

@app.route("/home")
def home():
    return render_template("landing.html")

@app.route("/about")
def about():
    return render_template("about.html")




if __name__ == "__main__":
    app.run(debug=True)
