from flask import Blueprint
from ..controllers import AddDyeCurlyCuts_controllers

app = Blueprint('styleS', __name__)

app.route('/AddDyeCurlyCuts', methods=["POST", "GET"])(AddDyeCurlyCuts_controllers.AddDyeCurlyCuts)

app.route("/DyeCurlyCuts", methods=["POST", "GET"] )(AddDyeCurlyCuts_controllers.getDye)

app.route('/delete_DyeCurlyCuts', methods=['POST'])(AddDyeCurlyCuts_controllers.delete_DyeCurlyCuts)

app.route('/EditDyeCurlyCuts', methods=['POST'])(AddDyeCurlyCuts_controllers.Edit_DyeCurlyCuts)

app.route('/Edit_DyeCurlyCuts1', methods=['POST'])(AddDyeCurlyCuts_controllers.Edit_DyeCurlyCuts1)