from shapely import from_wkt
import matplotlib.pyplot as plt

shapes = (
    from_wkt("POINT(0 0)"),
    from_wkt("LINESTRING(0 0,1 1,1 2)"),
    from_wkt("POLYGON((0 0,4 0,4 4,0 4,0 0),(1 1, 2 1, 2 2, 1 2,1 1))"),
    from_wkt("MULTILINESTRING((0 0,1 1,1 2),(2 3,3 2,5 4))"),
    from_wkt("MULTIPOLYGON(((0 0,4 0,4 4,0 4,0 0),(1 1,2 1,2 2,1 2,1 1)),((-1 -1,-1 -2,-2 -2,-2 -1,-1 -1)))"),
    from_wkt("GEOMETRYCOLLECTION(POINT(2 3),LINESTRING(2 3,3 4))")
)


def plot_shape(shape):
    if shape.geom_type == "Point":
        plt.plot(shape.x, shape.y, "o")
    elif shape.geom_type == "LineString":
        x = [x for x, y in shape.coords]
        y = [y for x, y in shape.coords]
        plt.plot(x, y, "-")
    elif shape.geom_type == "Polygon":
        x, y = shape.exterior.xy
        plt.plot(x, y, "-")
    else:
        for geom in shape.geoms:
            plot_shape(geom)


for shape in shapes:
    print(
        f"type={shape.geom_type}, area={shape.area:.1f}, length={shape.length:.1f}")
    plot_shape(shape)


plt.show()
