from flask import Blueprint
from ..controllers import AddDoubleDyeFade_controllers

app = Blueprint('stylE', __name__)

app.route('/AddDoubleDyeFade', methods=["POST", "GET"])(AddDoubleDyeFade_controllers.AddDoubleDyeFade)

app.route("/DoubleDyeFade", methods=["POST", "GET"] )(AddDoubleDyeFade_controllers.getDouble)

app.route('/delete_DoubleDyeFade', methods=['POST'])(AddDoubleDyeFade_controllers.delete_DoubleDyeFade)

app.route('/EditDoubleDyeFade', methods=['POST'])(AddDoubleDyeFade_controllers.Edit_DoubleDyeFade)

app.route('/Edit_DoubleDyeFade1', methods=['POST'])(AddDoubleDyeFade_controllers.Edit_DoubleDyeFade1)