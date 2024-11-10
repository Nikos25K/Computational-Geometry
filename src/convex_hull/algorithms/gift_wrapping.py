from utils import orientation_predicate, CW, plot2D

def gift_wrapping(points, print_steps=False):
    r = min(points, key=lambda p: (p.x, p.y))

    # Initialize the chain of points with the start point
    chain = [r]

    # Find the next point
    while True:
        next_point = None
        for p in points:
            # Skip current point
            if p == r:
                continue
            # If the next point is None or the orientation is CW
            if next_point is None or (orientation_predicate(r, next_point, p) == CW):
                # Update the next point
                next_point = p

        # If the next point is the start point
        if next_point == chain[0]:
            break
        # else add the next point to the chain and continue
        chain.append(next_point)
        r = next_point

        # Plot the current step
        if print_steps:
            plot2D(points, chain, False, "Gift Wrapping")

    # Plot the final convex hull
    if print_steps:
        plot2D(points, chain, True, "Gift Wrapping")

    return chain