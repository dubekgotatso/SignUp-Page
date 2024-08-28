from flask import Blueprint
from ..controllers import review_controllers

app = Blueprint('rev', __name__)

app.route('/review', methods=['GET', 'POST'])(review_controllers.review)

app.route('/review_display', methods=['GET'])(review_controllers.review_display)