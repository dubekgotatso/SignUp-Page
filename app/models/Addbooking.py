from .. import mongo

class Book:
    
    def Addbooking(booking):
        return mongo.db.booking.insert_one(booking)

    def getBookings():
        return mongo.db.booking.find()

    def EditBooking(booking_id, categories, date, time):
        return mongo.db.booking.update_one(
            {'_id': booking_id},
            {'$set': {'categories': categories, 'date': date, 'time': time}}
        )
        
    def delete_booking(delete_booking_id):
        return mongo.db.booking.delete_one({'_id': delete_booking_id})