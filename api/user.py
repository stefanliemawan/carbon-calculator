from flask import request, Blueprint
from werkzeug.security import check_password_hash, generate_password_hash

from main import db
from models import User, User_Emission
import utils as utils

bp = Blueprint("user", __name__, url_prefix="/user")

@bp.route("/", methods=["POST"])
def create_user():
    data = request.json

    # how to get index
    email = data["email"]
    username = data["username"]
    password = generate_password_hash(data["password"])

    user = User(email, username, password)

    db.session.add(user)
    db.session.commit()

    return str(user.user_id)