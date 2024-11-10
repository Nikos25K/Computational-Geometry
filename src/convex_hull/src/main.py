import utils, os.path

#importing the algorithms
from algorithms.divide_and_conquer import divide_and_conquer
from algorithms.quickhull import quickhull
from algorithms.incremental import incremental
from algorithms.gift_wrapping import gift_wrapping


if __name__ == "__main__":
    # Get the algorithm number from the user
    algorithm_number = utils.get_algorithm_number()

    # Ask the user if they want to see the steps
    steps = utils.ask_user("Do you want to see the steps? (y/n): ")

    if algorithm_number != "6":
        # Choose the algorithm to execute based on the number
        algorithm = incremental if algorithm_number == "1" \
                    else gift_wrapping if algorithm_number == "2" \
                    else divide_and_conquer if algorithm_number == "3" \
                    else quickhull

    # Check if the algorithm is 3D
    is3D = True if algorithm_number == "5" else False

    # If the file does not exist, create it and write the points to it
    file = "../files/points/points.txt" if not is3D else "../files/points/points3D.txt"

    # Ask the user if they want to generate collinear points
    collinear = utils.ask_user("Do you want to generate collinear points? (y/n): ")
    if collinear:
        file = "../files/points/collinear.txt"

    # Generate the points if the file does not exist
    if not os.path.exists(file):
        if collinear:
            utils.generate_collinear_points(file)
        else:
            utils.write_points_to_file(file)

    # Read the points from the file
    points = utils.read_from_file(file)

    if algorithm_number == "6":
        # Execute all the 2D algorithms
        utils.execute_algorithm(points, incremental, steps, collinear)
        utils.execute_algorithm(points, gift_wrapping, steps, collinear)
        utils.execute_algorithm(points, divide_and_conquer, steps, collinear)
        utils.execute_algorithm(points, quickhull, steps, collinear)
    else:
        # Execute the algorithm and plot the points if wanted
        utils.execute_algorithm(points, algorithm, steps, collinear)