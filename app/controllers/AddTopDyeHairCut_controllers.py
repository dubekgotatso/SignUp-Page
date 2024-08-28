from flask import jsonify, request, render_template, url_for, redirect
from ..models.AddTopDyeHairCut import Top
from bson.objectid import*

def AddTopDyeHairCut():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        top_dye_haircut = {'name': name, 'price': price}
        Top.addTopDyeHairCut(top_dye_haircut)
        # Redirect to the next page (e.g., 'getTop')
        return redirect(url_for('stylecut.getTop'))
    else:
        return render_template('AddTopDyeHairCut.html')

def getTop():
    top_dye_haircuts = list(Top.getTopDyeHairCuts())
    return render_template("TopDyeHairCut.html", x=top_dye_haircuts)

def delete_TopDyeHairCut():
    if request.method == 'POST':
        top_dye_haircut_id = request.form.get('delete_id')
        top_dye_haircut_id = ObjectId(top_dye_haircut_id)
        result = Top.deleteTopDyeHairCut(top_dye_haircut_id)
        if result.deleted_count == 1:
            return redirect(url_for('stylecut.getTop'))
        else:
            return 'Record not found or could not be deleted.'
        
def Edit_TopDyeHairCut():
    if request.method == 'POST':
        TopDyeHairCut_id = request.form.get("id") 
        name = request.form.get("name")
        price = request.form.get("price")
        TopDyeHairCut_id = ObjectId(TopDyeHairCut_id)
        result = Top.Edit_TopDyeHairCut(TopDyeHairCut_id, name, price,)
        if result.modified_count == 1:
            return redirect(url_for('stylecut.getTop'))
        else:
            return 'Failed to update the StyleCutDye.'
    return render_template('TopDyeHairCut.html')

def Edit_TopDyeHairCut1():
    if request.method == 'POST':
        TopDyeHairCut_id = request.form.get('update_id') 
        name = request.form.get("name") 
        price = request.form.get("price")  
        return render_template('EditTopDyeHairCut.html', name=name, price=price, TopDyeHairCut_id=TopDyeHairCut_id)       