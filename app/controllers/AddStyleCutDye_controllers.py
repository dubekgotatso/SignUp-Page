from flask import jsonify, request, render_template, url_for, redirect
from ..models.AddStyleCutDye import Style
from bson.objectid import*

def Add_Style_Cut_Dye():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        allStyleCutDye = {'name': name, 'price': price}
        Style.AddStyleCutDye(allStyleCutDye)
        # Redirect to the 'getStyle' route upon successful form submission
        return redirect(url_for('styl.getStyle'))
    else:
        return render_template('AddStyleCutDye.html')

def getStyle():
    if request.method == 'GET':
        getStyle = Style.getStyle()
        return render_template("StyleCutDye.html", x=getStyle)

def delete_StyleCutDye():
    if request.method == 'POST':
        style_cut_dye_id = request.form.get('delete_id')
        style_cut_dye_id = ObjectId(style_cut_dye_id)
        result = Style.delete_StyleCutDye(style_cut_dye_id)
        if result.deleted_count == 1:
            return redirect(url_for('styl.getStyle'))
        else:
            return 'Record not found or could not be deleted.'
        
        
def Edit_StyleCutDye():
    if request.method == 'POST':
        StyleCutDye_id = request.form.get("id") 
        name = request.form.get("name")
        price = request.form.get("price")
        StyleCutDye_id = ObjectId(StyleCutDye_id)
        result = Style.Edit_StyleCutDye(StyleCutDye_id, name, price,)
        if result.modified_count == 1:
            return redirect(url_for('styl.getStyle'))
        else:
            return 'Failed to update the StyleCutDye.'
    return render_template('StyleCutDye.html')

def Edit_StyleCutDye1():
    if request.method == 'POST':
        StyleCutDye_id = request.form.get('update_id') 
        name = request.form.get("name") 
        price = request.form.get("price")  
        return render_template('EditStyleCutDye.html', name=name, price=price, StyleCutDye_id=StyleCutDye_id)