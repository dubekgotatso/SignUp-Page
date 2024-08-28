from flask import Blueprint
from ..controllers import AddFadeWaveCut_controllers



app = Blueprint('styles', __name__)


app.route('/AddFadeWaveCut', methods=["POST" , "GET"])(AddFadeWaveCut_controllers.AddFadeWaveCut)

app.route("/FadeWaveCut", methods=["POST", "GET"] )(AddFadeWaveCut_controllers.getCut)

app.route('/delete_FadeWaveCut', methods=['POST'])(AddFadeWaveCut_controllers.delete_FadeWaveCut)

app.route('/EditFadeWaveCut', methods=["POST", "GET"])(AddFadeWaveCut_controllers.Edit_FadeWaveCut)

app.route('/Edit_FadeWaveCut1', methods=['POST'])(AddFadeWaveCut_controllers.Edit_FadeWaveCut1)

