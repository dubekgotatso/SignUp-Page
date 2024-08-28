from flask import Blueprint
from ..controllers import Addbooking_controllers

app = Blueprint('book', __name__)

app.route("/Addbooking", methods=["GET", "POST"])(Addbooking_controllers.Addbooking)

app.route("/selectedservice", methods=["GET", "POST"])(Addbooking_controllers.test)

app.route('/bookings', methods=["POST", "GET"])(Addbooking_controllers.getBookings)

app.route("/delete_booking", methods=["POST", "GET"] )(Addbooking_controllers.delete_booking)

app.route('/Editbooking', methods=['POST'])(Addbooking_controllers.Edit_booking)

app.route('/Edit_booking1', methods=['POST'])(Addbooking_controllers.Edit_booking1)