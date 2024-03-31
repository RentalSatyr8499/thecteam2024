import geopandas as gpd
import matplotlib.pyplot as plt

# Load the California county shapefile
shapefile_path = 'tl_2023_us_county.shx'
gdf = gpd.read_file(shapefile_path)

# # Display the first few rows of the GeoDataFrame
# print(gdf.head())

# # Display the column names
# print("Column names:", gdf.columns)

# # Display the unique values in the available columns
# for col in gdf.columns:
#     print(f"Unique values in column '{col}':", gdf[col].unique())

# # Assuming you have loaded the GeoDataFrame from the California county boundaries dataset
# # and it is named 'gdf'

# Check if 'Alameda' is in the 'NAME' column
alameda_exists = 'Alameda' in gdf['NAME'].values

if alameda_exists:
    print("Alameda county is present in the dataset.")
else:
    print("Alameda county is not found in the dataset.")

