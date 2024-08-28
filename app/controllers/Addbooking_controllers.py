from flask import jsonify, request, render_template, url_for, redirect
from ..models.Addbooking import Book
from bson.objectid import*



def Addbooking():
    if request.method == 'POST':
        categories = request.form.get("categories")
        date = request.form.get("date")
        time = request.form.get("time")
      
        booking = {"categories": categories, "date": date, "time": time}
        result = Book.Addbooking(booking)
        
        if result.inserted_id:
            return redirect(url_for('book.getBookings'))
        else:
            return 'Form submission failed.'
    
    return "Success"


def test():
    return render_template("Addbooking.html")

def getBookings():
    booking = []
    if request.method == 'GET':
        for i in Book.getBookings():
            booking.append(i)
        return render_template("bookings.html", booking=booking)

def Edit_booking():
    if request.method == 'POST':
        booking_id = request.form.get("booking_id") 
        categories = request.form.get("categories")
        date = request.form.get("date")
        time = request.form.get("time")
        booking_id = ObjectId(booking_id)
        result = Book.EditBooking(booking_id, categories, date, time)
        if result.modified_count == 1:
            return redirect(url_for('book.getBookings'))
        else:
            return 'Failed to update the booking.'
    return "Success"

def Edit_booking1():
    if request.method == 'POST':
        booking_id = request.form.get('booking_id') 
        categories = request.form.get("categories") 
        date = request.form.get("date")  
        time = request.form.get("time") 
        return render_template('Editbooking.html', categories=categories, date=date, time=time, booking_id=booking_id)

def delete_booking():
    if request.method == 'POST':
        booking_id = request.form.get('delete_id')
        booking_id = ObjectId(booking_id)
        result = Book.delete_booking(booking_id)
        if result.deleted_count == 1:
            return redirect(url_for('book.getBookings'))
        else:
            return 'Record not found or could not be deleted.'