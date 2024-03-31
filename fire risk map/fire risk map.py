import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt


# fxn to get color of each county
def get_color(value, vmin, vmax):
    """
    Returns a color based on the given value within the specified range [vmin, vmax].
    Red corresponds to the highest value (vmax), yellow corresponds to the lowest value (vmin),
    and orange corresponds to intermediate values.
    """
    cmap = plt.colormaps.get_cmap('YlOrRd')  # Choose a colormap (Yellow-Orange-Red)
    norm_value = (value - vmin) / (vmax - vmin)  # Normalize value to [0, 1]
    rgba_color = cmap(norm_value)
    return rgba_color

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

# Create a plot for California counties in blue
ax = california_gdf.plot(edgecolor='black', linewidth=0.5)

fire_risk_by_county = read_csv_to_dict('fire risk by county.csv')

# Loop through fire_risk_by_county and plot each county with the corresponding color
for county, value in fire_risk_by_county.items():
    if county in california_gdf['NAME'].values:
        color = get_color(value, vmin=min(fire_risk_by_county.values()), vmax=max(fire_risk_by_county.values()))
        california_gdf[california_gdf['NAME'] == county].plot(ax=ax, color=color, edgecolor='black', linewidth=1)

# Customize the plot (add title, labels, etc.)
plt.title('California Counties with Fire Risk Highlighted')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)

# Show the plot
plt.show()
