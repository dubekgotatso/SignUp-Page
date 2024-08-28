from .. import mongo

class Style:
    
    def AddStyleCutDye(style_cut_dye):
        return mongo.db.StyleCutDye.insert_one(style_cut_dye)

   
    def getStyle():
        return mongo.db.StyleCutDye.find()

  
    def delete_StyleCutDye(style_cut_dye_id):
        return mongo.db.StyleCutDye.delete_one({'_id': style_cut_dye_id})
    
    def Edit_StyleCutDye(StyleCutDye_id, name, price):
        return mongo.db.StyleCutDye.update_one(
            {'_id': StyleCutDye_id},
            {'$set': {'name':name , 'price': price}}
        )