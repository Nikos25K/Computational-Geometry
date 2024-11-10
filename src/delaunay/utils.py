import random, os
from scipy.spatial import Delaunay, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt

# Generate 100 random points and print them to a file
def write_points_to_file(file_name):
    with open(file_name, "w") as file:
      for _ in range(25):
        file.write(f"{random.uniform(0, 100)} {random.uniform(0, 100)}\n")


# Read the points from the file and return them as a list
def read_from_file(file_name):
    points = []
    with open(file_name, "r") as file:
        for line in file:
            x, y = line.split()
            points.append((float(x), float(y)))
    return points

# Create the points file if it doesn't exist and read the points from it
def create_and_read_points(file_name):
    if not os.path.exists(file_name):
        write_points_to_file(file_name)

    return read_from_file(file_name)


# Compute the Delaunay triangulation and the Voronoi diagram
def create_Voronoi_Delaunay(points):
    triangles = Delaunay(points).simplices
    vor = Voronoi(points)
    return vor, triangles


def plot_voronoi(vor, show=True):
    # Show the Voronoi diagram
    fig = voronoi_plot_2d(vor)
    plt.title("Voronoi Diagram")
    if show:
        plt.show()
    else:
        return fig

def plot_delunay(points, triangles):
    # Delaunay Triangulation
    plt.triplot(points[:, 0], points[:, 1], triangles)
    plt.plot(points[:, 0], points[:, 1], 'o')
    plt.title("Delaunay Triangulation")
    plt.show()

def plot_voronoi_and_delaunay(vor, points, triangles):
    # Generate the Voronoi diagram
    fig = plot_voronoi(vor, show=False)

    # Delaunay Triangulation
    plt.triplot(points[:, 0], points[:, 1], triangles)
    plt.plot(points[:, 0], points[:, 1], 'o')
    plt.title("Delaunay Triangulation")
    plt.show()