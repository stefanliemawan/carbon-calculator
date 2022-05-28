from flask import request, Blueprint
from datetime import datetime

from models import User_Emission, Item_Emission

bp = Blueprint("user_emission", __name__, url_prefix="/user_emission")

@bp.route("/", methods=["POST"])
def create_user_emission():
    data = request.json
    
    user_id = data["user_id"]
    items = data["items"]
    datetime = datetime.now()

    for item in items:
        item_name = item["item_name"]
        price = item["price_gbp"]

        # Item_Emission.query.filter_by(item_name=item_name)

    # calculate emission for every item, then return dictionary
    # interface