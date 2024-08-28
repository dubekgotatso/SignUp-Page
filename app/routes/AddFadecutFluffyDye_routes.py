from flask import Blueprint
from ..controllers import AddFadecutFluffyDye_controllers

app = Blueprint('stylecuts', __name__)

app.route("/AddFadeCutFluffyDye", methods=["POST", "GET"] )(AddFadecutFluffyDye_controllers.AddFadecutFluffyDye)

app.route("/FadeCutFluffyDye", methods=["POST", "GET"] )(AddFadecutFluffyDye_controllers.getFluffy)

app.route('/delete_FadeCutFluffyDye', methods=['POST'])(AddFadecutFluffyDye_controllers.delete_FadeCutFluffyDye)

app.route('/EditFadeCutFluffyDye', methods=['POST'])(AddFadecutFluffyDye_controllers.Edit_FadeCutFluffyDye)

app.route('/Edit_FadeCutFluffyDye1', methods=['POST'])(AddFadecutFluffyDye_controllers.Edit_FadecutFluffyDye1)