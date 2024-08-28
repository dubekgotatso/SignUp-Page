from .. import mongo

class Double:
      def AddDoubleDyeFade(DoubleDyeFade):
        return mongo.db.DoubleDyeFade.insert_one(DoubleDyeFade)
    
      def getDouble(Double):
            return mongo.db.DoubleDyeFade.find(Double)
        
      def delete_DoubleDyeFade(DoubleDyeFade_id):
        return mongo.db.DoubleDyeFade.delete_one({'_id': DoubleDyeFade_id}) 
      
      def Edit_DoubleDyeFade(DoubleDyeFade_id, name, price):
        return mongo.db.DoubleDyeFade.update_one(
            {'_id': DoubleDyeFade_id},
            {'$set': {'name':name , 'price': price}}
        )
        