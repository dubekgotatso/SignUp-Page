from flask import Flask, render_template, request, redirect, url_for,session
from flask_pymongo import PyMongo
from bson.objectid import *




app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/MiniProject'
mongo = PyMongo(app)
db = mongo.db


# landing page
@app.route('/')
def landing():
        return render_template("index.html")

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


#Client Signup
@app.route('/SignUp_Client', methods=['GET', 'POST'])
def signupClient():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists
        existing_user = db.SignUp_Client.find_one({'$or': [{'username': username}, {'email': email}]})
        if existing_user:
            return 'Username or email already exists!'

        # Insert new user into the database
        SignUpClientdetails = {'username': username, 'email': email, 'password': password}
        db.SignUp_Client.insert_one(SignUpClientdetails)
        
        # Redirect to login page or homepage
        return redirect(url_for('loginClient'))

    # Render the signup form template
    return render_template('SignUp_Client.html')


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


#Client Login
@app.route('/loginClient', methods=['GET', 'POST'])
def loginClient():
    if request.method == 'POST':
        # Extract form data
        username = request.form['username']
        password = request.form['password']

       
        existing_user = db.SignUp_Client.find_one({'username': username, 'password': password})
        if existing_user:
           
            return render_template('Services.html')
        else:
            # User not found, display error message
            return 'Invalid username or password'

    # Render the login form template
    return render_template('Login_Client.html')


@app.route('/AddItem', methods=["POST"])
def add_item():   
    if request.method == 'POST':
        return render_template("Addbooking.html")
    return render_template("Addbooking.html")

#Add Booking
@app.route("/Addbooking", methods=["GET", "POST"])
def Addbooking():
    if request.method == 'POST':
        Category = request.form.get("Category")
        Date = request.form.get("Date")
        Time = request.form.get("Time")
      
        booking = {"Category": Category, "Date": Date, "Time": Time}
        db.booking.insert_one(booking)
        
        if ('form submission success'):
           booking = db.booking.find()
           return render_template ("Services.html", booking=booking)
        else:
           if('form submission failed'):
               return 'form umsuccessful'
    
    return ("Success")


#Display Bookings
@app.route('/bookings', methods=["POST", "GET"])
def getBookings():
        booking = []
        for i in db.booking.find():
            booking.append(i)
        return render_template("bookings.html" , booking=booking )
        

@app.route("/Services")
def Service():
    return render_template("Services.html")

@app.route('/index')
def index():
       
       return render_template("Dashboard.html")


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
 
 
@app.route('/delete_FadeWaveCut', methods=['POST'])
def delete_FadeWaveCut():
    if request.method == 'POST':
        FadeWaveCut_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        FadeWaveCut_id = ObjectId(FadeWaveCut_id)
        # Delete the record from the collection
        result = db.FadeWaveCut.delete_one({'_id': FadeWaveCut_id})
        if result.deleted_count == 1:
            cut = []

            for i in db.FadeWaveCut.find():
                cut.append(i)
            return render_template('FadeWaveCuts.html', x=cut)
        else:
            return 'Record not found or could not be deleted.'
        
        
@app.route('/EditFadeWaveCut', methods=['POST'])
def Edit_FadeWaveCut():
    if request.method == 'POST':
        FadeWaveCut_id = request.form.get('id')  # Get the ID of the record to delete
        name = request.form.get('name')  # Get the ID of the record to delete
        price = request.form.get('price')  # Get the ID of the record to delete

        # Convert the string ID to ObjectId
        FadeWaveCut_id = ObjectId(FadeWaveCut_id)
        # Edit the record from the collection
        
        result = db.FadeWaveCut.update_one({'_id': FadeWaveCut_id},{'$set' :{'name' :name, 'price':price}})
        cut = []

        for i in db.FadeWaveCut.find():
           cut .append(i)
        return render_template('FadeWaveCuts.html', x=cut)

@app.route('/Edit_FadeWaveCut1', methods=['POST'])
def Edit_FadeWaveCut1():
    if request.method == 'POST':
        FadeWaveCut_id = request.form.get('update_id') 
        name = request.form.get('name') 
        price = request.form.get('price') 

        return render_template('EditFadeWaveCut.html', name=name, price=price, FadeWaveCut_id=FadeWaveCut_id)


@app.route('/')
def getFadeWaveCut():
    # Fetch data from the collection
    FadeWaveCut = db.FadeWaveCut.find(FadeWaveCut)
    return render_template('FadeWaveCuts.html', FadeWaveCut=FadeWaveCut)

 # Add BobCuts
 
@app.route('/AddBobCuts', methods=["POST", "GET"])
def Add_Bob_Cuts():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        
        BobCuts = { 'name': name, 'price': price}

        db.BobCuts.insert_one(BobCuts)
        if ('form submission success'):
                     return redirect (url_for('getBob'))
        else:

                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddBobCuts.html")


# Display BobCuts

@app.route("/BobCuts", methods=["POST", "GET"] )
def getBob():
     if request.method == 'GET':
          Bob = []

          for i in db.BobCuts.find():
           Bob.append(i)

     return render_template("BobCuts.html" , x=Bob )
 
 
@app.route('/delete_BobCuts', methods=['POST'])
def delete_BobCuts():
    if request.method == 'POST':
        BobCuts_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        BobCuts_id = ObjectId(BobCuts_id)
        # Delete the record from the collection
        result = db.BobCuts.delete_one({'_id': BobCuts_id})
        if result.deleted_count == 1:
            Bob = []

            for i in db.BobCuts.find():
                Bob.append(i)
            return render_template('BobCuts.html', x=Bob)
        else:
            return 'Record not found or could not be deleted.'

# Edit BobCuts
@app.route('/EditBobCuts', methods=['POST'])
def Edit_BobCuts():
    if request.method == 'POST':
        BobCuts_id = request.form.get('id')  # Get the ID of the record to delete
        name = request.form.get('name')  # Get the ID of the record to delete
        price = request.form.get('price')  # Get the ID of the record to delete

        # Convert the string ID to ObjectId
        BobCuts_id = ObjectId(BobCuts_id)
        # Edit the record from the collection
        
        result = db.BobCuts.update_one({'_id': BobCuts_id},{'$set' :{'name' :name, 'price':price}})
        Bob = []

        for i in db.BobCuts.find():
            Bob.append(i)
        return render_template('BobCuts.html', x=Bob)

@app.route('/Edit_BobCuts1', methods=['POST'])
def Edit_BobCuts1():
    if request.method == 'POST':
        BobCuts_id = request.form.get('update_id') 
        name = request.form.get('name') 
        price = request.form.get('price') 

        return render_template('EditBobCuts.html', name=name, price=price, BobCuts_id=BobCuts_id)

        
@app.route('/')
def getBobCuts():
    # Fetch data from the collection
    BobCuts = db.BobCuts.find(BobCuts)
    return render_template('BobCuts.html', BobCuts=BobCuts)

 


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
 
 # Delete BrushWaveCut
@app.route('/delete_BrushWaveCut', methods=['POST'])
def delete_BrushWaveCut():
    if request.method == 'POST':
        BrushWaveCut_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        BrushWaveCut_id = ObjectId(BrushWaveCut_id)
        # Delete the record from the collection
        result = db.BrushWaveCut.delete_one({'_id': BrushWaveCut_id})
        if result.deleted_count == 1:
            Brush= []

            for i in db.BrushWaveCut.find():
               Brush .append(i)
            return render_template('BrushWaveCuts.html', x=Brush)
        else:
            return 'Record not found or could not be deleted.'
        
        
 # Edit BrushWaveCut  
@app.route('/EditBrushWaveCut', methods=['POST'])
def Edit_BrushWaveCut():
    if request.method == 'POST':
        BrushWaveCut_id = request.form.get('id')  # Get the ID of the record to delete
        name = request.form.get('name')  # Get the ID of the record to delete
        price = request.form.get('price')  # Get the ID of the record to delete

        # Convert the string ID to ObjectId
        BrushWaveCut_id = ObjectId(BrushWaveCut_id)
        # Edit the record from the collection
        
        result = db.BrushWaveCut.update_one({'_id': BrushWaveCut_id},{'$set' :{'name' :name, 'price':price}})
        Brush = []

        for i in db.BrushWaveCut.find():
            Brush.append(i)
        return render_template('BrushWaveCuts.html', x=Brush)

@app.route('/Edit_BrushWaveCut1', methods=['POST'])
def Edit_BrushWaveCut1():
    if request.method == 'POST':
       BrushWaveCut_id = request.form.get('update_id') 
       name = request.form.get('name') 
       price = request.form.get('price') 

    return render_template('EditBrushWaveCut.html', name=name, price=price, BrushWaveCut_id=BrushWaveCut_id)


@app.route('/')
def getBrushWaveCut():
    # Fetch data from the collection
       BrushWaveCut= db.BrushWaveCut.find(BrushWaveCut)
       return render_template('BrushWaveCuts.html', BrushWaveCut=BrushWaveCut)

 
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
 
 
 # Delete DoubleDyeFade
@app.route('/delete_DoubleDyeFade', methods=['POST'])
def delete_DoubleDyeFade():
    if request.method == 'POST':
        DoubleDyeFade_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        DoubleDyeFade_id = ObjectId(DoubleDyeFade_id)
        # Delete the record from the collection
        result = db.DoubleDyeFade.delete_one({'_id': DoubleDyeFade_id})
        if result.deleted_count == 1:
            Double = []

            for i in db.DoubleDyeFade.find():
               Double .append(i)
            return render_template('DoubleDyeFade.html', x=Double  )
        else:
            return 'Record not found or could not be deleted.'
        
        
# Edit DoubleDyeFade 
@app.route('/EditDoubleDyeFade', methods=['POST'])
def Edit_DoubleDyeFade():
    if request.method == 'POST':
        DoubleDyeFade_id = request.form.get('id')  # Get the ID of the record to delete
        name = request.form.get('name')  # Get the ID of the record to delete
        price = request.form.get('price')  # Get the ID of the record to delete

        # Convert the string ID to ObjectId
        DoubleDyeFade_id = ObjectId(DoubleDyeFade_id)
        # Edit the record from the collection
        
        result = db.DoubleDyeFade.update_one({'_id': DoubleDyeFade_id},{'$set' :{'name' :name, 'price':price}})
        Double= []

    for i in db.DoubleDyeFade.find():
            Double.append(i)
    return render_template('DoubleDyeFade.html', x=Double)

@app.route('/Edit_DoubleDyeFade1', methods=['POST'])
def Edit_DoubleDyeFade1():
    if request.method == 'POST':
       DoubleDyeFade_id = request.form.get('update_id') 
       name = request.form.get('name') 
       price = request.form.get('price') 

    return render_template('EditDoubleDyeFade.html', name=name, price=price,  DoubleDyeFade_id= DoubleDyeFade_id)

        

@app.route('/')
def getDoubleDyeFade():
    # Fetch data from the collection
   DoubleDyeFade= db.DoubleDyeFade.find(DoubleDyeFade)
   return render_template('DoubleDyeFade.html', DoubleDyeFade=DoubleDyeFade)

 
 
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

     return render_template("TopDyeHairCut.html" , x=Top)
 
 
@app.route('/delete_TopDyeHairCut', methods=['POST'])
def delete_TopDyeHairCut():
    if request.method == 'POST':
        TopDyeHairCut_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        TopDyeHairCut_id = ObjectId( TopDyeHairCut_id)
        # Delete the record from the collection
        result = db. TopDyeHairCut.delete_one({'_id':  TopDyeHairCut_id})
        if result.deleted_count == 1:
            Top = []

            for i in db. TopDyeHairCut.find():
             Top.append(i)
            return render_template('TopDyeHairCut.html', x=Top )
        else:
            return 'Record not found or could not be deleted.'
        
        
        
# Edit TopDyeHairCut 
@app.route('/EditTopDyeHairCut', methods=['POST'])
def Edit_TopDyeHairCut():
    if request.method == 'POST':
        TopDyeHairCut_id = request.form.get('id')  # Get the ID of the record to delete
        name = request.form.get('name')  # Get the ID of the record to delete
        price = request.form.get('price')  # Get the ID of the record to delete

        # Convert the string ID to ObjectId
        TopDyeHairCut_id = ObjectId(TopDyeHairCut_id)
        # Edit the record from the collection
        
        result = db.TopDyeHairCut.update_one({'_id':TopDyeHairCut_id},{'$set' :{'name' :name, 'price':price}})
        Top= []

    for i in db.DoubleDyeFade.find():
            Top.append(i)
    return render_template('DoubleDyeFade.html', x=Top)

@app.route('/Edit_TopDyeHairCut1', methods=['POST'])
def Edit_TopDyeHairCut1():
    if request.method == 'POST':
       TopDyeHairCut_id = request.form.get('update_id') 
       name = request.form.get('name') 
       price = request.form.get('price') 

    return render_template('EditTopDyeHairCut.html', name=name, price=price,  TopDyeHairCut_id= TopDyeHairCut_id)

        

@app.route('/')
def getTopDyeHairCut():
    # Fetch data from the collection
        TopDyeHairCut = db. TopDyeHairCut.find( TopDyeHairCut)
        return render_template(' TopDyeHairCut.html',  TopDyeHairCut=TopDyeHairCut)
  
 
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
        
    return render_template("AddStyleCutDye.html")

#Display StyleCutDye

@app.route("/StyleCutDye", methods=["POST", "GET"] )
def getStyle():
     if request.method == 'GET':
         Style = []

         for i in db.StyleCutDye.find():
           Style.append(i)

     return render_template("StyleCutDye.html" , x=Style )
 
 
@app.route('/delete_StyleCutDye', methods=['POST'])
def delete_StyleCutDye():
    if request.method == 'POST':
        StyleCutDye_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        StyleCutDye_id = ObjectId(StyleCutDye_id)
        # Delete the record from the collection
        result = db.StyleCutDye.delete_one({'_id': StyleCutDye_id})
        if result.deleted_count == 1:
            Style = []

            for i in db.StyleCutDye.find():
               Style .append(i)
            return render_template('StyleCutDye.html', x=Style )
        else:
            return 'Record not found or could not be deleted.'
        
        
# Edit StyleCutDye
@app.route('/EditStyleCutDye', methods=['POST'])
def Edit_StyleCutDye():
    if request.method == 'POST':
        StyleCutDye_id = request.form.get('id')  # Get the ID of the record to delete
        name = request.form.get('name')  # Get the ID of the record to delete
        price = request.form.get('price')  # Get the ID of the record to delete

        # Convert the string ID to ObjectId
        StyleCutDye_id = ObjectId(StyleCutDye_id)
        # Edit the record from the collection
        
        result = db.StyleCutDye.update_one({'_id':StyleCutDye_id},{'$set' :{'name' :name, 'price':price}})
        Style=[]

    for i in db.StyleCutDye.find():
           Style.append(i)
    return render_template('StyleCutDye.html', x=Style)

@app.route('/Edit_StyleCutDye1', methods=['POST'])
def Edit_StyleCutDye1():
    if request.method == 'POST':
       StyleCutDye_id = request.form.get('update_id') 
       name = request.form.get('name') 
       price = request.form.get('price') 

    return render_template('EditStyleCutDye.html', name=name, price=price,  StyleCutDye_id= StyleCutDye_id)

        

@app.route('/')
def getStyleCutDye():
    # Fetch data from the collection
   StyleCutDye = db.StyleCutDye.find(StyleCutDye)
   return render_template('StyleCutDye.html', StyleCutDye=StyleCutDye)

 

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
        
    return render_template("AddFadeCutFluffyDye.html")

#Display FadeCutFluffyDye

@app.route("/FadeCutFluffyDye", methods=["POST", "GET"] )
def getFade():
     if request.method == 'GET':
        Fade = []

        for i in db.FadeCutFluffyDye.find():
          Fade.append(i)

     return render_template("FadeCutFluffyDye.html" , x=Fade )
 
 #Delete FadeCutFluffyDye
@app.route('/delete_FadeCutFluffyDye', methods=['POST'])
def delete_FadeCutFluffyDye():
    if request.method == 'POST':
       FadeCutFluffyDye_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
       FadeCutFluffyDye_id = ObjectId(FadeCutFluffyDye_id)
        # Delete the record from the collection
       result = db.FadeCutFluffyDye.delete_one({'_id': FadeCutFluffyDye_id})
    if result.deleted_count == 1:
            Fade  = []

            for i in db.FadeCutFluffyDye.find():
               Fade  .append(i)
            return render_template('FadeCutFluffyDye.html', x=Fade)
    else:
            return 'Record not found or could not be deleted.'
        
        
# Edit FadeCutFluffyDye
@app.route('/EditFadeCutFluffyDye', methods=['POST'])
def Edit_FadeCutFluffyDye():
    if request.method == 'POST':
        FadeCutFluffyDye_id = request.form.get('id')  # Get the ID of the record to delete
        name = request.form.get('name')  # Get the ID of the record to delete
        price = request.form.get('price')  # Get the ID of the record to delete

        # Convert the string ID to ObjectId
        FadeCutFluffyDye_id = ObjectId(FadeCutFluffyDye_id)
        # Edit the record from the collection
        
        result = db.FadeCutFluffyDye.update_one({'_id':FadeCutFluffyDye_id},{'$set' :{'name' :name, 'price':price}})
        Fade=[]

    for i in db.FadeCutFluffyDye.find():
           Fade.append(i)
    return render_template('FadeCutFluffyDye.html', x=Fade)

@app.route('/Edit_FadeCutFluffyDye1', methods=['POST'])
def Edit_FadeCutFluffyDye1():
    if request.method == 'POST':
       FadeCutFluffyDye_id = request.form.get('update_id') 
       name = request.form.get('name') 
       price = request.form.get('price') 

    return render_template('EditFadeCutFluffyDye.html', name=name, price=price,  FadeCutFluffyDye_id=FadeCutFluffyDye_id)

        

@app.route('/')
def getFadeCutFluffyDye():
    # Fetch data from the collection
   FadeCutFluffyDye = db.FadeCutFluffyDye.find(FadeCutFluffyDye)
   return render_template('FadeCutFluffyDye.html', FadeCutFluffyDye=FadeCutFluffyDye)


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
        
    return render_template("AddDyeCurlyCuts.html")

#Display DyeCurlyCuts

@app.route("/DyeCurlyCuts", methods=["POST", "GET"] )
def getDye():
     if request.method == 'GET':
        Dye = []

        for i in db.DyeCurlyCuts.find():
          Dye.append(i)

     return render_template("DyeCurlyCuts.html" , x=Dye )
 
 
@app.route('/delete_DyeCurlyCuts', methods=['POST'])
def delete_DyeCurlyCuts():
    if request.method == 'POST':
       DyeCurlyCuts_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
       DyeCurlyCuts_id = ObjectId(DyeCurlyCuts_id)
        # Delete the record from the collection
       result = db.DyeCurlyCuts.delete_one({'_id': DyeCurlyCuts_id})
    if result.deleted_count == 1:
            Dye = []

            for i in db.DyeCurlyCuts.find():
               Dye  .append(i)
            return render_template('DyeCurlyCuts.html', x=Dye)
    else:
            return 'Record not found or could not be deleted.'
        
        
        
        
# Edit DyeCurlyCuts
@app.route('/EditDyeCurlyCuts', methods=['POST'])
def Edit_DyeCurlyCuts():
    if request.method == 'POST':
        DyeCurlyCuts_id = request.form.get('id')  # Get the ID of the record to delete
        name = request.form.get('name')  # Get the ID of the record to delete
        price = request.form.get('price')  # Get the ID of the record to delete

        # Convert the string ID to ObjectId
        DyeCurlyCuts_id = ObjectId(DyeCurlyCuts_id)
        # Edit the record from the collection
        
        result = db.DyeCurlyCuts.update_one({'_id':DyeCurlyCuts_id},{'$set' :{'name' :name, 'price':price}})
        Dye=[]

    for i in db.DyeCurlyCuts.find():
           Dye.append(i)
    return render_template('StyleCutDye.html', x=Dye)

@app.route('/Edit_DyeCurlyCuts1', methods=['POST'])
def Edit_DyeCurlyCuts1():
    if request.method == 'POST':
       DyeCurlyCuts_id = request.form.get('update_id') 
       name = request.form.get('name') 
       price = request.form.get('price') 

    return render_template('EditDyeCurlyCuts.html', name=name, price=price,  DyeCurlyCuts_id= DyeCurlyCuts_id)
        

@app.route('/')
def getDyeCurlyCuts():
    # Fetch data from the collection
   DyeCurlyCuts = db.DyeCurlyCuts.find(DyeCurlyCuts)
   return render_template('DyeCurlyCuts.html', DyeCurlyCuts=DyeCurlyCuts)


 
if __name__ == "__main__":
    app.run(debug=True)
