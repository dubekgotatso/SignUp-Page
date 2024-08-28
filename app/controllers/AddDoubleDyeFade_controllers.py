from flask import jsonify, request, render_template, url_for, redirect
from ..models.AddDoubleDyeFade import Double
from bson.objectid import*

def AddDoubleDyeFade():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        allDyeCurlyCuts = {'name': name, 'price': price}
        Double.AddDoubleDyeFade(allDyeCurlyCuts)
        # Redirect to the 'getFluffy' route upon successful form submission
        return redirect(url_for('stylE.getDouble'))
    else:
        return render_template('AddDoubleDyeFade.html')
    
def getDouble():
     if request.method == 'GET':
          getDouble = []
          for i in Double.getDouble(getDouble): 
            getDouble.append(i)     
     return render_template("DoubleDyeFade.html" , x=getDouble)
 
def delete_DoubleDyeFade():
    if request.method == 'POST':
        DoubleDyeFade_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        DoubleDyeFade_id= ObjectId(DoubleDyeFade_id)
        # Delete the record from the collection
        result = Double.delete_DoubleDyeFade(DoubleDyeFade_id)
        if result.deleted_count == 1:
            return redirect (url_for('stylE.getDouble'))
        else:
            return 'Record not found or could not be deleted.'
        
def Edit_DoubleDyeFade():
    if request.method == 'POST':
        DoubleDyeFade_id = request.form.get("id") 
        name = request.form.get("name")
        price = request.form.get("price")
        DoubleDyeFade_id = ObjectId(DoubleDyeFade_id)
        result = Double.Edit_DoubleDyeFade(DoubleDyeFade_id, name, price,)
        if result.modified_count == 1:
            return redirect(url_for('stylE.getDouble'))
        else:
            return 'Failed to update the DoubleDyeFade.'
    return render_template('DoubleDyeFade.html')

def Edit_DoubleDyeFade1():
    if request.method == 'POST':
        DoubleDyeFade_id = request.form.get('update_id') 
        name = request.form.get("name") 
        price = request.form.get("price")  
    return render_template('EditDoubleDyeFade.html', name=name, price=price, DoubleDyeFade_id=DoubleDyeFade_id)

