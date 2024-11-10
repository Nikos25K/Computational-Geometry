from utils import orientation_predicate, CCW, plot2D

# Graham Scan Algorithm
def incremental(points, print_steps=False):
    
    Lup = []
    #first, we sort the points by x-coordinate and then by y-coordinate
    points.sort(key = lambda p:(p.x, p.y))

    # Find the first 2 points for Lup
    Lup.append(points[0]) # the point with the lowest x-coordinate
    Lup.append(points[1])

    #we keep track of the number of points
    n = len(points)

    # Plot the first 2 points
    if print_steps: 
        plot2D(points, Lup, False, "Incremental")

    # Lup
    for i in range(2, n):
        # Insert each point to Lup
        Lup.append(points[i])
        # CounterClockWise, left turn so we remove the middle point
        while (len(Lup) > 2) and (orientation_predicate(Lup[-3], Lup[-2], Lup[-1]) == CCW):
            Lup.pop(-2)

        if print_steps:
            plot2D(points, Lup, False, "Incremental")

    Ldown = []
    # Find the first 2 points for Ldown
    Ldown.append(points[n - 1])
    Ldown.append(points[n - 2])

    # Lup + first 2 points of Ldown
    if print_steps:
        plot2D(points, Lup + Ldown)
    
    # Ldown
    for i in range(n - 3, -1, -1):
        # Insert each point to Ldown
        Ldown.append(points[i])
        # CounterClockWise, left turn so we remove the middle point
        while (len(Ldown) > 2) and (orientation_predicate(Ldown[-3], Ldown[-2], Ldown[-1]) == CCW):
            Ldown.pop(-2)

        if print_steps:
            plot2D(points, Lup + Ldown, False, "Incremental")

    # Remove first and last point from Ldown so we don't have duplicates
    Ldown.pop(-1)
    Ldown.pop(0)

    # Combine Lup and Ldown and return the Convex Hull
    ConvexHull = Lup + Ldown

    # Plot the final Convex Hull
    if print_steps:
        plot2D(points, ConvexHull, True, "Incremental")    

    return ConvexHull