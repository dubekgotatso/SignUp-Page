from flask import Blueprint
from ..controllers import user_controllers



app = Blueprint('user', __name__)


app.route('/')(user_controllers.landing)

app.route('/signup', methods=['POST', 'GET'])(user_controllers.signup)

app.route('/login', methods=['GET', 'POST'])(user_controllers.login)

app.route('/SignUp_Client', methods=['GET', 'POST'])(user_controllers.signupClient)

app.route('/loginClient', methods=['GET', 'POST'])(user_controllers.loginClient)

app.route("/home", methods=['GET', 'POST'])


