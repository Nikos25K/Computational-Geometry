import random
import matplotlib.pyplot as plt
import numpy as np

#the main class for the points
class Point:
    def __init__(self, x = None, y = None):
        self.x = x
        self.y = y

    def __len__(self):
        return 2

#class for the 3D points
class Point3D:
    def __init__(self, x = None, y = None, z = None):
        self.x = x
        self.y = y
        self.z = z

    def __len__(self):
        return 3

#defining the orientation of the points
CW = -1
CCW = 1
COLINEAR = 0

#orientation predicate
def orientation_predicate(p, q, r):
    value = (q.x*r.y - r.x*q.y) - \
            (p.x*r.y - p.y*r.x) + \
            (p.x*q.y - p.y*q.x)
    if value == 0:
        return COLINEAR
    elif value > 0:
        return CW
    else:
        return CCW

# Generate 100 random points and print them to a file
def write_points_to_file(file_name):
    with open(file_name, "w") as file:

      # 85 points for 3D and 100 for 2D
      len = 100 if "3D" not in file_name else 85

      for _ in range(len):
        if "3D" in file_name:
            file.write(f"{random.uniform(0, 100)} {random.uniform(0, 100)} {random.uniform(0, 100)}\n")
        else:
            file.write(f"{random.uniform(0, 100)} {random.uniform(0, 100)}\n")

def write_collinear_to_file(file_name):
    with open(file_name, "w") as file:

        for _ in range(15):
            file.write(f"{random.uniform(0, 100)} {random.uniform(0, 100)}\n")

        # Add 5 collinear points
        x = random.uniform(0, 100)
        y = random.uniform(0, 100)
        for i in range(5):
            tmp = random.uniform(0,12)
            file.write(f"{x+tmp} {y}\n")


# Read the points from the file and return them as a list of Point or Point3D objects
def read_from_file(file_name):

    points = []
    with open(file_name, "r") as file:
        for line in file:
            # Check if the file contains 3D points or 2D points
            if "3D" in file_name:
                x, y, z = line.split()
                points.append(Point3D(float(x), float(y), float(z)))
            else:
                x, y = line.split()
                points.append(Point(float(x), float(y)))
    return points

# Function to plot the points and the convex hull
def plot2D(points, hull, final=False, algorithm=None):
    # plot all the points first
    x = [p.x for p in points]
    y = [p.y for p in points]
    plt.plot(x, y, '.b')

    # plot the points of the convex hull
    x = [p.x for p in hull]
    y = [p.y for p in hull]
    plt.plot(x, y, 'r-')

    if final:
        title = "Final Convex Hull of " + algorithm
        # plot the last edge to connect the last point to the first point
        xlast = [hull[-1].x, hull[0].x]
        ylast = [hull[-1].y, hull[0].y]
        plt.plot(xlast, ylast, 'r-')
    else:
        title = "Step in algorithm " + algorithm

    plt.title(title)
    plt.show()

def plot3D(points, hull, final=False):

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # plot all the points first
    x = [p.x for p in points]
    y = [p.y for p in points]
    z = [p.z for p in points]
    ax.scatter(x, y, z, c='b')

    # plot the points of the convex hull
    hull_points = [points[p] for p in hull.vertices]
    x = [p.x for p in hull_points]
    y = [p.y for p in hull_points]
    z = [p.z for p in hull_points]
    ax.scatter(x, y, z, c='r')

    points_3D = np.array([(p.x, p.y, p.z) for p in points])

    # Plot the hull edges
    for simplex in hull.simplices:
        x = [points_3D[i, 0] for i in simplex]
        y = [points_3D[i, 1] for i in simplex]
        z = [points_3D[i, 2] for i in simplex]
        ax.plot(x, y, z, 'r-')

    if final:
        ax.set_title("Final Convex Hull of QuickHull3D")
        # plot the last edge to connect the last point to the first point
        xlast = [hull_points[-1].x, hull_points[0].x]
        ylast = [hull_points[-1].y, hull_points[0].y]
        zlast = [hull_points[-1].z, hull_points[0].z]
        ax.plot(xlast, ylast, zlast, 'r-')
    else:
        ax.set_title("Step in QuickHull3D")

    plt.show()


# Execute the algorithm given and write the points to its file 
def execute_algorithm(points, algorithm, steps=False, collinear=False):
    # Get the name of the algorithm as a string
    algorithm_str = algorithm.__name__ if callable(algorithm) else algorithm

    # Check if there are points to plot
    if(len(points) == 0):
        print("No points to plot")
        return

    # Check if the points are 2D or 3D
    flag_3D = len(points[0]) == 3

    if not flag_3D:
        if collinear:
            file_name = f"../files/output/collinear/{algorithm_str}.txt"
        else:
            file_name = f"../files/output/non_collinear/{algorithm_str}.txt"
    else:
        file_name = f"../files/output/non_collinear/{algorithm_str}3D.txt"

    # Write the points generated to a file
    with open(file_name, "w") as file:

        # Execute the algorithm
        hull_points = algorithm(points, steps)

        if not flag_3D:
            for p in hull_points:
                file.write(f"{p.x} {p.y} \n")
        else:
            for p in hull_points:
                file.write(f"{p.x} {p.y} {p.z} \n")


# Print the help message to the user
def print_help():
    print("\nChoose an algorithm to execute:")
    print("1. Incremental")
    print("2. Gift Wrapping")
    print("3. Divide and Conquer")
    print("4. Quickhull")
    print("5. Quickhull 3D")
    print("6. All 2D algorithms")

# Get the number of the algorithm to execute
def get_algorithm_number():
    while True:
        print_help()
        algorithm_number = input("Enter the number of the algorithm you want to execute: ")
        if algorithm_number in ["1", "2", "3", "4", "5", "6"]:
            return algorithm_number
        else:
            print("Invalid input. Please enter a valid number.")

# Ask the user something and get y/n as a response
def ask_user(message):
    while True:
        response = input(message)
        if response in ["y", "Y"]:
            return True
        elif response in ["n", "N"]:
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")