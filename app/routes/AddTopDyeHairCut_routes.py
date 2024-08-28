from flask import Blueprint
from ..controllers import AddTopDyeHairCut_controllers

app = Blueprint('stylecut', __name__)

app.route('/AddTopDyeHairCut', methods=["POST", "GET"])(AddTopDyeHairCut_controllers.AddTopDyeHairCut)

app.route("/TopDyeHairCut", methods=["POST", "GET"] )(AddTopDyeHairCut_controllers.getTop)

app.route('/delete_TopDyeHairCut', methods=['POST'])(AddTopDyeHairCut_controllers.delete_TopDyeHairCut)

app.route('/EditTopDyeHairCut', methods=['POST'])(AddTopDyeHairCut_controllers.Edit_TopDyeHairCut)

app.route('/Edit_TopDyeHairCut1', methods=['POST'])(AddTopDyeHairCut_controllers.Edit_TopDyeHairCut1)