from flask import request, Blueprint
from datetime import datetime

from models import User_Emission


bp = Blueprint("user_emission", __name__, url_prefix="/user_emission")


@bp.route("/", methods=["POST"])
def create_user_emission():
    data = request.json
    
    user_id = data["user_id"]
    items_and_price = data["items"]
    datetime = datetime.now()

    # calculate emission for every item, then return dictionary
    