import pandas as pd

emissions_per_item_df = pd.read_excel(
    io="./datasets/Consumption_emissions_March_21_final_accessible_rev.xls", 
    sheet_name="Conversion_factors_2018",
    header=1,
    usecols="B:E"
)


emissions_per_item_df[["index", "item"]] = emissions_per_item_df["Unnamed: 1"].str.split(n=1, expand=True)

columns = emissions_per_item_df.columns.tolist()

columns = columns[-2:] + columns[1:-2]

emissions_per_item_df = emissions_per_item_df[columns]

emissions_per_item_df.rename(
    columns={
        "GHG (kgCO2e per £)": "ghg_kgco2e_per_£",
        "CO2 (kgCO2 per £)": "co2_kgco2_per_£",
        "NRG (kg oil equivalent per £)": "nrg_kg_oil_equivalent_per_£"
    }, 
    inplace=True
)

emissions_per_item_df.to_csv("./clean_datasets/emissions_per_item.csv", index=False)
