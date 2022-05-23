from api import db, Emissions_Per_Item

db.drop_all()
db.create_all()

rice = Emissions_Per_Item(
    index = "1.1.1.1",
    item = "Rice",
    ghg = 0.1537316273723316,
    co2 = 0.100415214957414,
    nrg = 0.02337605584822312
)

db.session.add(rice)

db.session.commit()

print(rice.item)
print(rice.ghg)

print(Emissions_Per_Item.query.all())