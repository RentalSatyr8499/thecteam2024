import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

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
def read_csv_to_dict(csv_filename, valueColumn):
    """
    Reads a CSV file and returns its content as a dictionary.
    valueColumn represents the name of the header of the column in the CSV that will become the values in the dictionary.
    """
    data_dict = {}
    try:
        df = pd.read_csv(csv_filename)
        data_dict = dict(zip(df["County"], df[str(valueColumn)]))
    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
    return data_dict

def color_counties(colorVals: dict):
    '''
    Given a dictionary with county names as the keys and floats as the values, this fxn colors the counties using get_color.
    '''
    # Loop through fire_risk_by_county and plot each county with the corresponding color
    for county, value in colorVals.items():
        if county in california_gdf['NAME'].values:
            color = get_color(value, vmin=min(fireRiskByCounty[2].values()), vmax=max(fireRiskByCounty[2].values()))
            california_gdf[california_gdf['NAME'] == county].plot(ax=ax, color=color, edgecolor='black', linewidth=1)

# create geodataframe
shapefile_path = r'C:\Users\ychun\Downloads\tl_2023_us_county\tl_2023_us_county.shx'
gdf = gpd.read_file(shapefile_path)
california_gdf = gdf[gdf['STATEFP'] == '06']

# Read data from the updated CSV file with columns for different years
years = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]  # Add more years as needed
fireRiskByCounty = []
for i in years: 
    fireRiskByCounty.append(read_csv_to_dict('fire risk by county.csv', i))

# Initialize the plot
fig, ax = plt.subplots(figsize=(10, 10))
california_gdf.plot(ax=ax, edgecolor='black', linewidth=0.5)


color_counties(fireRiskByCounty[8])
plt.title(2030)

# Add a colorbar
cax = make_axes_locatable(ax).append_axes("right", size="5%", pad=0.05)
mappable = plt.cm.ScalarMappable(cmap='YlOrRd', norm=plt.Normalize(vmin=min(fireRiskByCounty[2].values()), vmax=max(fireRiskByCounty[2].values())))
plt.colorbar(mappable, cax)

# Show the animation
plt.savefig(r'C:\Users\ychun\Documents\workspace\2030.png')
plt.show()
