import pandas as pd

from main import engine, db
import utils as utils

db.drop_all()

item_emissions_df = pd.read_csv("../clean_datasets/item_emissions.csv")
item_emissions_df["item_id"] = [ utils.generate_id("item_emissions", index) for index in item_emissions_df.index]

columns = item_emissions_df.columns.tolist()

columns = columns[-1:] + columns[1:-1]

item_emissions_df = item_emissions_df[columns]

item_emissions_df.to_sql("item_emissions", con=engine, index=False, if_exists="replace")

db.create_all()
db.session.commit()