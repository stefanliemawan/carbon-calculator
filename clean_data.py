import pandas as pd

footprint_by_item_df = pd.read_excel(
    io="./datasets/Consumption_emissions_March_21_final_accessible_rev.xls", 
    sheet_name="Conversion_factors_2018",
    header=1,
    usecols="B:E"
)

footprint_by_item_df.rename(columns={"Unnamed: 1" : "Item"}, inplace=True)

footprint_by_item_df["Item"] = footprint_by_item_df["Item"].apply(lambda x: " ".join(x.split(" ")[1:]))

footprint_by_item_df.to_csv("./clean_datasets/footprint_by_item.csv", index=False)
