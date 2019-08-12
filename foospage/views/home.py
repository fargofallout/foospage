from flask import Blueprint

bp = Blueprint("home", __name__)

@bp.route("home")
def home():

	return "whatever"
