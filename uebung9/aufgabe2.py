from shapely import from_wkt
from shapely.ops import triangulate
import matplotlib.pyplot as plt

polygon = from_wkt(
    "POLYGON ((-5 -5, -5 5, 5 5, 5 -5, -5 -5), (1 -1, 4 -1, 4 1, 1 1, 1 4, -1 4, -1 1, -4 1, -4 -1, -1 -1, -1 -4, 1 -4, 1 -1))")
triangles = triangulate(polygon)

clipped_triangles = []
for triangle in triangles:
    clipped = polygon.intersection(triangle)
    if clipped.geom_type == "Polygon":
        clipped_triangles.append(clipped)

for clipped in clipped_triangles:
    x, y = clipped.exterior.coords.xy
    plt.fill(x, y, color='blue', alpha=0.2)

for clipped in clipped_triangles:
    x, y = clipped.exterior.coords.xy
    plt.plot(x, y, color='black')

plt.axis("equal")
plt.show()
