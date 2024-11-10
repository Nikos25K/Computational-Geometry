import utils
import kd_tree

if __name__ == "__main__":
    # If the file does not exist, create it and write the points to it
    points = utils.create_and_read_points("points.txt")

    # Create a kd-tree with the points
    tree = kd_tree.KdTree(points, 2)

    # Create the rectangle
    rect = kd_tree.Rectangle(20, 20, 80, 80)

    # Search for the points inside the rectangle
    result = tree.search_inside_rectangle(rect)

    # Plot the points
    utils.plot_points(points, rect, result)

    # Print the points inside the rectangle to a file
    utils.print_to_file(result)