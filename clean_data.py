import pandas as pd

emissions_per_item_df = pd.read_excel(
    io="./datasets/Consumption_emissions_March_21_final_accessible_rev.xls", 
    sheet_name="Conversion_factors_2018",
    header=1,
    usecols="B:E"
)

emissions_per_item_df.rename(
    columns={
        "Unnamed: 1" : "item"
    }, 
    inplace=True
)

emissions_per_item_df["item"] = emissions_per_item_df["item"].apply(lambda x: " ".join(x.split(" ")[1:]))

emissions_per_item_df.to_csv("./clean_datasets/emissions_per_item.csv", index=False)
