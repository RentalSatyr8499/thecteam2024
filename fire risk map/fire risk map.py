import geopandas as gpd
import matplotlib.pyplot as plt

# Load the California county shapefile
shapefile_path = r'C:\Users\ychun\Downloads\tl_2023_us_county\tl_2023_us_county.shx'
gdf = gpd.read_file(shapefile_path)

# Plot the county boundaries
gdf.plot(edgecolor='black', linewidth=0.5)

# Customize the plot (add title, labels, etc.)
plt.title('California County Boundaries with Alameda County Highlighted')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.grid(True)

# Show the plot
plt.show()
