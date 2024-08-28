from .. import mongo

class Brush:
    
    def AddBrushWaveCut(BrushWaveCut):
            return mongo.db.BrushWaveCut.insert_one(BrushWaveCut)
        
    def getBrush(Brush):
            return mongo.db.BrushWaveCut.find(Brush)
        
    def delete_BrushWaveCut(delete_BrushWaveCut_id):
            return mongo.db.BrushWaveCut.delete_one({'_id': delete_BrushWaveCut_id})
        
    def Edit_BrushWaveCut(BrushWaveCut_id, name, price):
        return mongo.db.BrushWaveCut.update_one(
            {'_id': BrushWaveCut_id},
            {'$set': {'name':name , 'price': price}}
        )