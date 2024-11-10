import random, os
import matplotlib.pyplot as plt

# Generate 100 random points and print them to a file
def write_points_to_file(file_name):
    with open(file_name, "w") as file:
      for _ in range(100):
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


# Plot the points (those inside the rectangle will be shown in red)
def plot_points(points, rect, result):
    # Plot the rectangle
    plt.plot([rect.x1, rect.x2, rect.x2, rect.x1, rect.x1], \
             [rect.y1, rect.y1, rect.y2, rect.y2, rect.y1], 'g-')

    # Plot the points
    for point in points:
        plt.plot(point[0], point[1], 'bo')

    # Plot the points inside the rectangle
    for point in result:
        plt.plot(point[0], point[1], 'ro')

    plt.title("Points inside the rectangle")
    plt.show()

def print_to_file(result):
    with open("result.txt", "w") as file:
        for point in result:
            file.write(f"{point[0]} {point[1]}\n")