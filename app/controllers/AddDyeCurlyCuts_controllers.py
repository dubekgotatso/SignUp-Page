from flask import jsonify, request, render_template, url_for, redirect
from ..models.AddDyeCurlyCuts import Dye
from bson.objectid import*

def AddDyeCurlyCuts():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        allDyeCurlyCuts = {'name': name, 'price': price}
        Dye.AddDyeCurlyCuts(allDyeCurlyCuts)
        # Redirect to the 'getFluffy' route upon successful form submission
        return redirect(url_for('styleS.getDye'))
    else:
        return render_template('AddDyeCurlyCuts.html')
    
def getDye():
     if request.method == 'GET':
          getDye = []
          for i in Dye.getDye(getDye): 
            getDye.append(i)     
     return render_template("DyeCurlyCuts.html" , x=getDye)
 
def delete_DyeCurlyCuts():
    if request.method == 'POST':
        DyeCurlyCuts_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        DyeCurlyCuts_id= ObjectId(DyeCurlyCuts_id)
        # Delete the record from the collection
        result = Dye.delete_DyeCurlyCuts(DyeCurlyCuts_id)
        if result.deleted_count == 1:
            return redirect (url_for('styleS.getDye'))
        else:
            return 'Record not found or could not be deleted.'
        
def Edit_DyeCurlyCuts():
    if request.method == 'POST':
        DyeCurlyCuts_id = request.form.get("id") 
        name = request.form.get("name")
        price = request.form.get("price")
        DyeCurlyCuts_id = ObjectId(DyeCurlyCuts_id)
        result = Dye.Edit_DyeCurlyCuts(DyeCurlyCuts_id, name, price,)
        if result.modified_count == 1:
            return redirect(url_for('stylE.getDouble'))
        else:
            return 'Failed to update the DoubleDyeFade.'
    return render_template('DyeCurlyCuts.html')

def Edit_DyeCurlyCuts1():
    if request.method == 'POST':
        DyeCurlyCuts_id = request.form.get('update_id') 
        name = request.form.get("name") 
        price = request.form.get("price")  
    return render_template('EditDyeCurlyCuts.html', name=name, price=price, DyeCurlyCuts_id=DyeCurlyCuts_id)