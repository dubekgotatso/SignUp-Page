from flask import jsonify, request, render_template, url_for, redirect
from ..models.AddFadeWaveCut import Fade
from bson.objectid import*

def AddFadeWaveCut():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        allFadeWaveCut = {'name': name, 'price': price}
        Fade.AddFadeWaveCut(allFadeWaveCut)
        if ('form submission success'):
            # Form submission success
         return redirect (url_for('styles.getCut'))
    else: 
     return render_template('AddFadeWaveCut.html')

def getCut():
     if request.method == 'GET':
          get_the_cut = []
          for i in Fade.getCut(get_the_cut): 
            get_the_cut.append(i)     
     return render_template("FadeWaveCuts.html" , x=get_the_cut)
 
def delete_FadeWaveCut():
    if request.method == 'POST':
        FadeWaveCut_id = request.form.get('delete_id')  # Get the ID of the record to delete
        # Convert the string ID to ObjectId
        FadeWaveCut_id = ObjectId(FadeWaveCut_id)
        # Delete the record from the collection
        result = Fade.delete_FadeWaveCut(FadeWaveCut_id)
        if result.deleted_count == 1:
            return redirect (url_for('styles.getCut'))
        else:
            return 'Record not found or could not be deleted.'
        
def Edit_FadeWaveCut():
    if request.method == 'POST':
        FadeWaveCut_id = request.form.get("id") 
        name = request.form.get("name")
        price = request.form.get("price")
        FadeWaveCut_id = ObjectId(FadeWaveCut_id)
        result = Fade.Edit_FadeWaveCut(FadeWaveCut_id, name, price,)
        if result.modified_count == 1:
            return redirect(url_for('styles.getCut'))
        else:
            return 'Failed to update the FadeWaveCut.'
    return render_template('FadeWaveCut.html')

def Edit_FadeWaveCut1():
    if request.method == 'POST':
        FadeWaveCut_id = request.form.get('update_id') 
        name = request.form.get("name") 
        price = request.form.get("price")  
    return render_template('EditFadeWaveCut.html', name=name, price=price, FadeWaveCut_id=FadeWaveCut_id)
        

