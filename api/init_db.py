import pandas as pd
from sqlalchemy import text

from api import engine

emissions_per_item_df = pd.read_csv("../clean_datasets/emissions_per_item.csv")
emissions_per_item_df.to_sql("emissions_per_item", con=engine, index=False, if_exists="replace")

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM emissions_per_item"))
      
#     for row in result:
#         print(row)