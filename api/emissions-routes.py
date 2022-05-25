from flask import request

from api import app
from models import Emissions_Per_Item

@app.route("/", methods=["POST"])
def calculateEmissions():
    data = request.json
    item_name = data["item_name"]
    price = data["price"]

    emission =  Emissions_Per_Item.query.filter_by(item_name=item_name).first()

    ghg_kgco2e = price * emission.ghg_kgco2e_per_gbp
    co2_kgco2 = price * emission.co2_kgco2_per_gbp
    nrg_kg_oil_equivalent = price * emission.nrg_kg_oil_equivalent_per_gbp

    calculated_emissions = {
        "ghg_kgco2e": ghg_kgco2e,
        "co2_kgco2": co2_kgco2,
        "nrg_kg_oil_equivalent": nrg_kg_oil_equivalent
    }

    return calculated_emissions