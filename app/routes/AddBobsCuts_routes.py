from flask import Blueprint
from ..controllers import AddBobCuts_controllers

app = Blueprint('style', __name__)



app.route('/AddBobCuts', methods=["POST", "GET"])(AddBobCuts_controllers.Add_Bob_Cuts)

app.route("/BobCuts", methods=["POST", "GET"])(AddBobCuts_controllers.getBob)

app.route('/delete_BobCuts', methods=['POST'])(AddBobCuts_controllers.delete_BobCuts)

app.route('/EditBobCuts', methods=['POST'])(AddBobCuts_controllers.Edit_BobCuts)

app.route('/Edit_BobCuts1', methods=['POST'])(AddBobCuts_controllers.Edit_BobCuts1)

