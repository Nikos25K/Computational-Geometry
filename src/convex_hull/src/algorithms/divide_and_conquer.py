from utils import orientation_predicate, CCW, plot2D

# If the user wants to see the steps
# Set the global variables to print the steps
prints = False
pointss = []

def divide_and_conquer(points, print_steps=False):
    if print_steps:
        prints = True
        pointss = points

    # Sort the points by x-coordinate
    points.sort(key=lambda p: (p.x, p.y))

    #call the recursive function
    merged = divide_recursive(points, print_steps)

    #print the final convex hull
    if print_steps:
        plot2D(pointss, merged, True, "Divide and Conquer")

    return merged


def divide_recursive(points, print_steps=False):
    # If the user wants to see the steps
    # Set the global variables to print the steps

    n = len(points)
    # Base case
    if n <= 2:
        return points

    # Divide the points into two halves
    left = points[:n//2]
    right = points[n//2:]

    # Recursively find the convex hull for the left and right halves
    left_hull = divide_recursive(left)
    right_hull = divide_recursive(right)

    # Merge the convex hulls
    merged = merge(left_hull, right_hull)

    # if prints:
    #     plot2D(pointss, merged, final=False)

    return merged

#helper function to add the points to the merged from hull
def add_to_hull(merged, hull, lower, upper):
    n = len(hull)
    ind = upper
    merged.append(hull[upper])
    while ind != lower:
        ind = (ind+1) % n
        merged.append(hull[ind])


def merge(left_hull, right_hull):
    # Find the upper and lower points
    uppera, upperb = Lup_merge(left_hull, right_hull)
    lowera, lowerb = Ldown_merge(left_hull, right_hull)

    # Combine the upper and lower hulls based on the upper and lower points
    merged = []

    add_to_hull(merged, left_hull, lowera, uppera)
    add_to_hull(merged, right_hull, upperb, lowerb)

    return merged

def find_rightmost_leftmost(left_hull, right_hull):
    # find the rightmost point of the left hull
    i = left_hull.index(max(left_hull, key=lambda p: p.x))

    # find the leftmost point of the right hull
    j = right_hull.index(min(right_hull, key=lambda p: p.x))

    return i, j



def Lup_merge(left_hull, right_hull):
    # find the rightmost point of the left hull and the leftmost point of the right hull
    i, j = find_rightmost_leftmost(left_hull, right_hull)

    # flag to check if the points are in the right order
    flag = False
    n1 = len(left_hull)
    n2 = len(right_hull)

    while not flag:
        flag = True

        while orientation_predicate(left_hull[i], left_hull[(i+1) % n1], right_hull[j]) == CCW:
            i = (i + 1) % n1
            flag = False

        while orientation_predicate(right_hull[(n2+j-1) % n2], right_hull[j],left_hull[i]) == CCW:
            j = (n2+ j - 1) % n2
            flag = False 

    return i,j


def Ldown_merge(left_hull, right_hull):
    # find the rightmost point of the left hull and the leftmost point of the right hull
    i, j = find_rightmost_leftmost(left_hull, right_hull)


    # flag to check if the points are in the right order
    flag = False
    n1 = len(left_hull)
    n2 = len(right_hull)
    while not flag:
        flag = True

        while orientation_predicate(right_hull[j], right_hull[(j+1) % n2], left_hull[i]) == CCW:
            j = (j + 1) % n2
            flag = False

        while orientation_predicate(left_hull[(n1+i-1) % n1], left_hull[i], right_hull[j]) == CCW:
            i = (n1+ i - 1) % n1
            flag = False

    return i,j