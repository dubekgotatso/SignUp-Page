from .. import mongo

class Bob:
     def AddBobCuts(BobCuts):
            return mongo.db.BobCuts.insert_one(BobCuts)
        
     def getBob(Bob):
         return mongo.db.BobCuts.find(Bob)
     
     def delete_BobCuts(delete_BobCuts_id):
            return mongo.db.BobCuts.delete_one({'_id': delete_BobCuts_id})
     
     def Edit_BobCuts(BobCuts_id, name, price):
        return mongo.db.BobCuts.update_one(
            {'_id': BobCuts_id},
            {'$set': {'name':name , 'price': price}}
        )