import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

# fxn to read the csv file
def read_csv_to_dict(csv_filename):
    """
    Reads a CSV file and returns its content as a dictionary.
    Assumes that the CSV has two columns: the first column as keys and the second column as values.
    """
    data_dict = {}
    try:
        df = pd.read_csv(csv_filename)
        data_dict = dict(zip(df.iloc[:, 0], df.iloc[:, 1]))
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
    return data_dict
# Load the California county shapefile
shapefile_path = r'C:\Users\ychun\Downloads\tl_2023_us_county\tl_2023_us_county.shx'
gdf = gpd.read_file(shapefile_path)

# Filter the GeoDataFrame to get only the California counties (with 'STATEFP' value '06')
california_gdf = gdf[gdf['STATEFP'] == '06']

# Read fire risk data from CSV
fire_risk_by_county = read_csv_to_dict('fire risk by county.csv')

# Loop through California counties
for county_row in california_gdf.iterrows():
    county_name = county_row[1]['NAME']
    if county_name not in fire_risk_by_county:
        print(county_name)

