import geopandas as gpd
import matplotlib.pyplot as plt

# Load the California county shapefile
shapefile_path = r'C:\Users\ychun\Downloads\tl_2023_us_county\tl_2023_us_county.shx'
gdf = gpd.read_file(shapefile_path)

# Filter the GeoDataFrame to get only the California counties (with 'STATEFP' value '06')
california_gdf = gdf[gdf['STATEFP'] == '06']

# Create a plot for California counties in blue
ax = california_gdf.plot(edgecolor='black', linewidth=0.5)

# Filter the GeoDataFrame to get only the Alameda county
alameda_gdf = california_gdf[california_gdf['NAME'] == 'Alameda']

# Plot the Alameda county in red (if it exists in the filtered dataset)
if not alameda_gdf.empty:
    alameda_gdf.plot(ax=ax, color='red', edgecolor='black', linewidth=1)

# Customize the plot (add title, labels, etc.)
plt.title('California County Boundaries with Alameda County Highlighted')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)

# Show the plot
plt.show()
