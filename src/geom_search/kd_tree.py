# The rectangle class
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    # Check if a point is inside the rectangle
    def contains(self, point):
        return self.x1 <= point[0] <= self.x2 and self.y1 <= point[1] <= self.y2


# kd-tree node
class Knode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# kd-tree
class KdTree:
    def __init__(self, points=None, k=2):
        self.root = self.build_kdtree(points, 0, k)

    # Build a kd-tree using recursion
    def build_kdtree(self, points, depth, k):
        if not points:
            return None

        # Select axis based on depth so that axis cycles through all valid values
        axis = depth % k

        # Sort the points based on the axis and choose the median as the pivot element
        points.sort(key=lambda x: x[axis])

        median = len(points) // 2

        # Create a node with the median point and recursively build the left and right subtrees
        return Knode(
            data=points[median],
            left=self.build_kdtree(points[:median], depth + 1, k),
            right=self.build_kdtree(points[median + 1:], depth + 1, k)
        )

    # Search for the points inside the rectangle
    def search_inside_rectangle(self, rect):
        result = []
        self.search_inside_rectangle_recursive(self.root, rect, 0, result)
        return result

    # Search for the points inside the rectangle using recursion
    def search_inside_rectangle_recursive(self, node, rect, depth, result):
        if not node:
            return

        # Check if the point is inside the rectangle
        if rect.contains(node.data):
            result.append(node.data)

        # Select axis based on depth so that axis cycles through all valid values
        axis = depth % 2

        # Check if the rectangle intersects the left subtree
        if node.left and rect.x1 <= node.data[axis]:
            self.search_inside_rectangle_recursive(node.left, rect, depth + 1, result)

        # Check if the rectangle intersects the right subtree
        if node.right and rect.x2 >= node.data[axis]:
            self.search_inside_rectangle_recursive(node.right, rect, depth + 1, result)