import pandas as pd

footprint_by_item_df = pd.read_excel(
    io="./datasets/Consumption_emissions_March_21_final_accessible_rev.xls", 
    sheet_name="Conversion_factors_2018",
    header=1,
    usecols="B:E"
)

footprint_by_item_df[["Index", "Item"]] = footprint_by_item_df["Unnamed: 1"].str.split(n=1, expand=True)

columns = footprint_by_item_df.columns.tolist()

columns = columns[-2:] + columns[1:-2]

footprint_by_item_df = footprint_by_item_df[columns]

footprint_by_item_df.to_csv("./clean_datasets/footprint_by_item.csv", index=False)