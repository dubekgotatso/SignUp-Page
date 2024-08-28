from flask import jsonify, request, render_template, url_for, redirect
from ..models.AddBobCuts import Bob
from bson.objectid import*

def Add_Bob_Cuts():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price'] 
        allBobCuts = { 'name': name, 'price': price}
        Bob.AddBobCuts(allBobCuts)
        if ('form submission success'):
                     return redirect (url_for('style.getBob'))
        else:
                  if ('form submission failed'):
                   return 'form unsuccessful'
        
    return render_template("AddBobCuts.html")

def getBob():
     if request.method == 'GET':
          getBob = []
          for i in Bob.getBob(getBob): 
            getBob.append(i)     
     return render_template("BobCuts.html" , x=getBob)
 
def delete_BobCuts():
    if request.method == 'POST':
        BobCuts_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        BobCuts_id = ObjectId(BobCuts_id)
        # Delete the record from the collection
        result = Bob.delete_BobCuts(BobCuts_id)
        if result.deleted_count == 1:
            return redirect (url_for('style.getBob'))
        else:
            return 'Record not found or could not be deleted.'
        
def Edit_BobCuts():
    if request.method == 'POST':
        BobCuts_id = request.form.get("id") 
        name = request.form.get("name")
        price = request.form.get("price")
        BobCuts_id = ObjectId(BobCuts_id)
        result = Bob.Edit_BobCuts(BobCuts_id, name, price,)
        if result.modified_count == 1:
            return redirect(url_for('style.getBob'))
        else:
            return 'Failed to update the BobCuts.'
    
    return render_template('BobCuts.html')

def Edit_BobCuts1():
    if request.method == 'POST':
        BobCuts_id = request.form.get('update_id') 
        name = request.form.get("name") 
        price = request.form.get("price")  
        return render_template('EditBobCuts.html', name=name, price=price, BobCuts_id=BobCuts_id)