from flask import jsonify, request, render_template, url_for, redirect
from ..models.AddFadecutFluffyDye import Fluffy
from bson.objectid import*

def AddFadecutFluffyDye():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        allFadecutFluffyDye = {'name': name, 'price': price}
        Fluffy.AddFadecutFluffyDye(allFadecutFluffyDye)
        # Redirect to the 'getFluffy' route upon successful form submission
        return redirect(url_for('stylecuts.getFluffy'))
    else:
        return render_template('AddFadecutFluffyDye.html')

def getFluffy():
    if request.method == 'GET':
        getFluffy = Fluffy.getFluffy()
        return render_template("FadeCutFluffyDye.html", x=getFluffy)

def delete_FadeCutFluffyDye():
    if request.method == 'POST':
        fade_cut_fluffy_dye_id = request.form.get('delete_id')
        fade_cut_fluffy_dye_id = ObjectId(fade_cut_fluffy_dye_id)
        result = Fluffy.delete_FadeCutFluffyDye(fade_cut_fluffy_dye_id)
        if result.deleted_count == 1:
            return redirect(url_for('stylecuts.getFluffy'))
        else:
            return 'Record not found or could not be deleted.'
        
def Edit_FadeCutFluffyDye():
    if request.method == 'POST':
        FadeCutFluffyDye_id = request.form.get("id") 
        name = request.form.get("name")
        price = request.form.get("price")
        FadeCutFluffyDye_id = ObjectId(FadeCutFluffyDye_id)
        result = Fluffy.Edit_FadeCutFluffyDye(FadeCutFluffyDye_id, name, price,)

        if result.modified_count == 1:
            return redirect(url_for('stylecuts.getFluffy'))
        else:
            return 'Failed to update the FadeCutFluffyDye.'
    return render_template('FadeCutFluffyDye.html.html')

def Edit_FadecutFluffyDye1():
    if request.method == 'POST':
        FadeCutFluffyDye_id = request.form.get('update_id') 
        name = request.form.get("name") 
        price = request.form.get("price")  
    return render_template('EditFadeCutFluffyDye.html', name=name, price=price, FadeCutFluffyDye_id_id=FadeCutFluffyDye_id)
        
