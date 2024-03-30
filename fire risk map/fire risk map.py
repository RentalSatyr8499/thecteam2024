from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

# Set up orthographic map projection
map = Basemap(projection='ortho', lat_0=45, lon_0=-100, resolution='l')

# Draw coastlines, country boundaries, and fill continents
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='coral', lake_color='aqua')

# Draw the edge of the map projection region
map.drawmapboundary(fill_color='aqua')

# Draw lat/lon grid lines every 30 degrees
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))

# Show the plot
plt.title('Contour lines over filled continent background')
plt.show()
