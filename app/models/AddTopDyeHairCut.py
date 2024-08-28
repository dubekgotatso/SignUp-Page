from .. import mongo

class Top:
    
    def addTopDyeHairCut(top_dye_haircut):
        return mongo.db.TopDyeHairCut.insert_one(top_dye_haircut)

    
    def getTopDyeHairCuts():
        return mongo.db.TopDyeHairCut.find()

    
    def deleteTopDyeHairCut(top_dye_haircut_id):
        return mongo.db.TopDyeHairCut.delete_one({'_id': top_dye_haircut_id})  
    
    def Edit_TopDyeHairCut(TopDyeHairCut_id, name, price):
        return mongo.db.TopDyeHairCut.update_one(
            {'_id': TopDyeHairCut_id},
            {'$set': {'name':name , 'price': price}}
        ) 