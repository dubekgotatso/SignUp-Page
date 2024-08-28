from flask import Blueprint
from ..controllers import AddBrushWaveCut_controllers

app = Blueprint('styless', __name__)

app.route("/AddBrushWaveCut", methods=["POST", "GET"] )(AddBrushWaveCut_controllers.AddBrushWaveCut)

app.route("/BrushWaveCut", methods=["POST", "GET"] )(AddBrushWaveCut_controllers.getBrush)

app.route("/delete_BrushWaveCut", methods=["POST", "GET"] )(AddBrushWaveCut_controllers.delete_BrushWaveCut)

app.route('/EditBrushWaveCut', methods=['POST'])(AddBrushWaveCut_controllers.Edit_BrushWaveCut)

app.route('/Edit_BrushWaveCut1', methods=['POST'])(AddBrushWaveCut_controllers.Edit_BrushWaveCut1)