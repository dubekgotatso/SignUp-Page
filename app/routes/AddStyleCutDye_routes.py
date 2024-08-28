from flask import Blueprint
from ..controllers import AddStyleCutDye_controllers

app = Blueprint('styl', __name__)

app.route('/AddStyleCutDye', methods=["POST", "GET"])(AddStyleCutDye_controllers.Add_Style_Cut_Dye)

app.route("/StyleCutDye", methods=["POST", "GET"] )(AddStyleCutDye_controllers.getStyle)

app.route('/delete_StyleCutDye', methods=['POST'])(AddStyleCutDye_controllers.delete_StyleCutDye)

app.route('/EditStyleCutDye', methods=['POST'])(AddStyleCutDye_controllers.Edit_StyleCutDye)

app.route('/Edit_StyleCutDye1', methods=['POST'])(AddStyleCutDye_controllers.Edit_StyleCutDye1)