from .. import mongo

class Fade:
    
        def AddFadeWaveCut(FadeWaveCut):
            return mongo.db.FadeWaveCut.insert_one(FadeWaveCut)
    
        def getCut(Cut):
            return mongo.db.FadeWaveCut.find(Cut)
    
        def delete_FadeWaveCut(FadeWaveCut_id):
            return mongo.db.FadeWaveCut.delete_one({'_id': FadeWaveCut_id})
    
        def Edit_FadeWaveCut(FadeWaveCut_id, name, price):
            return mongo.db.FadeWaveCut.update_one(
            {'_id': FadeWaveCut_id},
            {'$set': {'name':name , 'price': price}}
        ) 
        
        