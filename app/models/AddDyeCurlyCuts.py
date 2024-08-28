from .. import mongo

class Dye:
    def AddDyeCurlyCuts (DyeCurlyCuts):
        return mongo.db.DyeCurlyCuts.insert_one(DyeCurlyCuts)
    
    def getDye(Dye):
            return mongo.db.DyeCurlyCuts.find(Dye)
        
    def delete_DyeCurlyCuts(DyeCurlyCuts_id):
        return mongo.db.DyeCurlyCuts.delete_one({'_id': DyeCurlyCuts_id}) 
    
    def Edit_DyeCurlyCuts(DyeCurlyCuts_id, name, price):
        return mongo.db.DyeCurlyCuts.update_one(
            {'_id': DyeCurlyCuts_id},
            {'$set': {'name':name , 'price': price}}
        )