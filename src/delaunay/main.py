import utils
import numpy as np


if __name__ == "__main__":

    # Create the points file if it doesn't exist and read the points from it
    points = utils.create_and_read_points("points.txt")
    points = np.array(points)

    # Compute the Delaunay triangulation and the Voronoi diagram
    vor, triangles = utils.create_Voronoi_Delaunay(points)

    # Show the Voronoi diagram
    utils.plot_voronoi(vor)

    # Show the Delaunay triangulation and the Voronoi diagram
    utils.plot_voronoi_and_delaunay(vor, points, triangles)

    # Delaunay Triangulation
    utils.plot_delunay(points, triangles)