import shortuuid

from models import *

def generate_id(tablename, index):
    match tablename:
        case "emissions_per_item":
            prefix = "epi"
        case "users":
            prefix = "usr"
        case "user_emissions":
            prefix = "uem"

    uid = shortuuid.uuid()

    id = f"{prefix}{uid}{index}"

    return id