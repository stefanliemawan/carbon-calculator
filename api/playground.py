from api import db
from models import Item_Emission

item_emission = Item_Emission.query.all()
print(item_emission)
