from .. import mongo

class Fluffy:
   
    def AddFadecutFluffyDye(fadecut_fluffy_dye):
        return mongo.db.FadecutFluffyDye.insert_one(fadecut_fluffy_dye)

   
    def getFluffy():
        return mongo.db.FadecutFluffyDye.find()

   
    def delete_FadeCutFluffyDye(fade_cut_fluffy_dye_id):
        return mongo.db.FadecutFluffyDye.delete_one({'_id': fade_cut_fluffy_dye_id})   
    
    def Edit_FadeCutFluffyDye(FadeCutFluffyDye_id, name, price):
        return mongo.db.FadecutFluffyDye.update_one(
            {'_id': FadeCutFluffyDye_id},
            {'$set': {'name':name , 'price': price}}
        )   