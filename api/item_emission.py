from flask import request, Blueprint

from models import Item_Emission


bp = Blueprint("item_emission", __name__, url_prefix="/item_emission")

@bp.route("/", methods=["POST"])
def calculate_item_emissions():
    data = request.json
    item_name = data["item_name"]
    price = data["price"]

    item_emission =  Item_Emission.query.filter_by(item_name=item_name).first()

    ghg_kgco2e = price * item_emission.ghg_kgco2e_per_gbp
    co2_kgco2 = price * item_emission.co2_kgco2_per_gbp
    nrg_kg_oil_equivalent = price * item_emission.nrg_kg_oil_equivalent_per_gbp

    calculated_item_emissions = {
        "ghg_kgco2e": ghg_kgco2e,
        "co2_kgco2": co2_kgco2,
        "nrg_kg_oil_equivalent": nrg_kg_oil_equivalent
    }

    return calculated_item_emissions