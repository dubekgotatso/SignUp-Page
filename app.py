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

@app.route("/Booking", methods=["POST", "GET"] )
def getBooking():
     if request.method == 'GET':
          Booking = []

          for i in db.booking.find():
            Booking.append(i)
            
             
     
     return render_template("bookings.html" , Booking=Booking )
      
 
      

@app.route("/AddBooking", methods=["GET", "POST"])
def addbooking():
  if request.method == 'POST':
      category = request.form["category"]
      time = request.form["time"]
      date = request.form["date"]
     
      
      booking = {"category":category,"time":time,"date":date,}
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


# Add FadeWaveCut
@app.route('/AddFadeWaveCut', methods=["POST", "GET"])
def AddFadeWaveCut():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        FadeWaveCut = { 'name': name, 'price': price}

        db.FadeWaveCut.insert_one(FadeWaveCut)
        if ('form submission success'):
                     return redirect (url_for('getCut'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddFadeWaveCut.html")

#Display FadeWaveCut
@app.route("/FadeWaveCut", methods=["POST", "GET"] )
def getCut():
     if request.method == 'GET':
          cut = []

          for i in db.FadeWaveCut.find():
            cut.append(i)

     return render_template("FadeWaveCuts.html" , x=cut )


# Add BrushWaveCut

@app.route('/AddBrushWaveCut', methods=["POST", "GET"])
def AddBrushWaveCut():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        BrushWaveCut = { 'name': name, 'price': price}

        db.BrushWaveCut.insert_one(BrushWaveCut)
        if ('form submission success'):
                     return redirect (url_for('getBrush'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddBrushWaveCut.html")

# Display BrushWaveCut

@app.route("/BrushWaveCut", methods=["POST", "GET"] )
def getBrush():
     if request.method == 'GET':
          Brush = []

          for i in db.BrushWaveCut.find():
            Brush.append(i)

     return render_template("BrushWaveCuts.html" , x=Brush )
 
 
 # Add DoubleDyeFade

@app.route('/AddDoubleDyeFade', methods=["POST", "GET"])
def AddDoubleDyeFade():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        DoubleDyeFade = { 'name': name, 'price': price}

        db.DoubleDyeFade.insert_one(DoubleDyeFade)
        if ('form submission success'):
                     return redirect (url_for('getDouble'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddDoubleDyeFade.html")

# Display DoubleDyeFade

@app.route("/DoubleDyeFade", methods=["POST", "GET"] )
def getDouble():
     if request.method == 'GET':
          Double = []

          for i in db.DoubleDyeFade.find():
            Double.append(i)

     return render_template("DoubleDyeFade.html" , x=Double )
 
 # Add TopDyeHairCut
 
@app.route('/AddTopDyeHairCut', methods=["POST", "GET"])
def AddTopDyeHairCut():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        TopDyeHairCut= { 'name': name, 'price': price}

        db.TopDyeHairCut.insert_one(TopDyeHairCut)
        if ('form submission success'):
                     return redirect (url_for('getTop'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
    return render_template("AddTopDyeHairCut.html")

#Display TopDyeHairCut
@app.route("/TopDyeHairCut", methods=["POST", "GET"] )
def getTop():
     if request.method == 'GET':
          Top = []

          for i in db.TopDyeHairCut.find():
            Top.append(i)

     return render_template("TopDyeHairCut.html" , x=Top )

 # Add BobCuts
@app.route('/AddBobCuts.html', methods=["POST", "GET"])
def AddBobCuts():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        BobCuts= { 'name': name, 'price': price}

        db.BobCuts.insert_one(BobCuts)
        if ('form submission success'):
                     return redirect (url_for('getBob'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("BobCuts.html")


#Display BobCuts

@app.route("/BobCuts", methods=["POST", "GET"] )
def getBob():
     if request.method == 'GET':
         Bob = []

         for i in db.BobCuts.find():
            Bob.append(i)

     return render_template("BobCuts.html" , x=Bob )
 
 # Add StyleCutDye
@app.route('/AddStyleCutDye', methods=["POST", "GET"])
def Add_Style_Cut_Dye():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        StyleCutDye= { 'name': name, 'price': price}

        db.StyleCutDye.insert_one(StyleCutDye)
        if ('form submission success'):
                     return redirect (url_for('getStyle'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("StyleCutDye.html")

#Display StyleCutDye

@app.route("/StyleCutDye", methods=["POST", "GET"] )
def getStyle():
     if request.method == 'GET':
         Style = []

         for i in db.StyleCutDye.find():
           Style.append(i)

     return render_template("StyleCutDye.html" , x=Style )

# Add FadeCutFluffyDye
@app.route('/AddFadeCutFluffyDye', methods=["POST", "GET"])
def AddFadeCutFluffyDye():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        FadeCutFluffyDye= { 'name': name, 'price': price}

        db.FadeCutFluffyDye.insert_one(FadeCutFluffyDye)
        if ('form submission success'):
                     return redirect (url_for('getFade'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("FadeCutFluffyDye.html")

#Display FadeCutFluffyDye

@app.route("/FadeCutFluffyDye", methods=["POST", "GET"] )
def getFade():
     if request.method == 'GET':
         Fade = []

         for i in db.FadeCutFluffyDye.find():
           Fade.append(i)

     return render_template("FadeCutFluffyDye.html" , x=Fade )

# Add DyeCurlyCuts
@app.route('/AddDyeCurlyCuts', methods=["POST", "GET"])
def AddDyeCurlyCuts():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        DyeCurlyCuts= { 'name': name, 'price': price}

        db.DyeCurlyCuts.insert_one(DyeCurlyCuts)
        if ('form submission success'):
                     return redirect (url_for('getDye'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("DyeCurlyCuts.html")

#Display DyeCurlyCuts

@app.route("/DyeCurlyCuts", methods=["POST", "GET"] )
def getDyeCurlyCuts():
     if request.method == 'GET':
        Dye = []

        for i in db.DyeCurlyCuts.find():
          Dye.append(i)

     return render_template("DyeCurlyCuts.html" , x=Dye )

 
if __name__ == "__main__":
    app.run(debug=True)
