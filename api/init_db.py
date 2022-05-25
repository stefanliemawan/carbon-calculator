import pandas as pd
from sqlalchemy import text
import uuid

from api import engine
from utils import generate_id

emissions_per_item_df = pd.read_csv("../clean_datasets/emissions_per_item.csv")
emissions_per_item_df["item_id"] = [ generate_id("emissions_per_item", index) for index in emissions_per_item_df.index]

columns = emissions_per_item_df.columns.tolist()

columns = columns[-1:] + columns[1:-1]

emissions_per_item_df = emissions_per_item_df[columns]

emissions_per_item_df.to_sql("emissions_per_item", con=engine, index=False, if_exists="replace")

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM emissions_per_item"))
      
#     for row in result:
#         print(row)