from flask import jsonify, request, render_template, url_for, redirect
from ..models.AddBrushWaveCut import Brush
from bson.objectid import*

def AddBrushWaveCut():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        allBrushWaveCut= {'name': name, 'price': price}
        Brush.AddBrushWaveCut(allBrushWaveCut)
        if ('form submission success'):
            # Form submission success
         return redirect (url_for('styless.getBrush'))
    else: 
     return render_template('AddBrushWaveCut.html')
 
def getBrush():
     if request.method == 'GET':
          getBrush = []
          for i in Brush.getBrush(getBrush): 
            getBrush.append(i)     
     return render_template("BrushWaveCuts.html" , x=getBrush)
 
def delete_BrushWaveCut():
    if request.method == 'POST':
        BrushWaveCut_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        BrushWaveCut_id= ObjectId(BrushWaveCut_id)
        # Delete the record from the collection
        result = Brush.delete_BrushWaveCut(BrushWaveCut_id)
        if result.deleted_count == 1:
            return redirect (url_for('styless.getBrush'))
        else:
            return 'Record not found or could not be deleted.'
        
def Edit_BrushWaveCut():
    if request.method == 'POST':
        BrushWaveCut_id = request.form.get("id") 
        name = request.form.get("name")
        price = request.form.get("price")
        BrushWaveCut_id = ObjectId(BrushWaveCut_id)
        result = Brush.Edit_BrushWaveCut(BrushWaveCut_id, name, price,)

        if result.modified_count == 1:
            return redirect(url_for('styless.getBrush'))
        else:
            return 'Failed to update the BrushWaveCut.'
    return render_template('BrushWaveCut.html')

def Edit_BrushWaveCut1():
    if request.method == 'POST':
        BrushWaveCut_id = request.form.get('update_id') 
        name = request.form.get("name") 
        price = request.form.get("price")  
        return render_template('EditBrushWaveCut.html', name=name, price=price, BrushWaveCut_id=BrushWaveCut_id)
    



