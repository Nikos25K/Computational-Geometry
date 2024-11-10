from scipy.spatial import ConvexHull
import numpy as np
from utils import plot2D, plot3D

def quickhull(points, steps=False):
    if len(points[0]) != 2 and len(points[0]) != 3:
        raise ValueError("Points must be 2D or 3D")

    # Check if the points are 2D or 3D
    flag_3D = len(points[0]) == 3

    # Convert the points to the format that ConvexHull expects
    if not flag_3D:
        hull_points = np.array([[point.x, point.y] for point in points])
    else:
        hull_points = np.array([[point.x, point.y, point.z] for point in points])

    hull_points = ConvexHull(hull_points)

    # Plot the steps if the user wants to see them
    # Convert the hull points to the original format to plot
    if not flag_3D:
        hull_points = [points[p] for p in hull_points.vertices]
        if steps:
            plot2D(points, hull_points, True, "Quickhull")
    else:
        if steps:
            plot3D(points, hull_points, True)

        # Convert the hull points to the original format to print in file
        hull_points = [points[p] for p in hull_points.vertices]

    return hull_points