import geopandas as gpd
import matplotlib.pyplot as plt

# Load the California county shapefile
shapefile_path = 'ca_county_boundaries.shx'
gdf = gpd.read_file(shapefile_path)

# Plot the county boundaries
gdf.plot(edgecolor='black', linewidth=0.5)

# Customize the plot (add title, labels, etc.)
plt.title('California County Boundaries')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)

# Show the plot
plt.show()
