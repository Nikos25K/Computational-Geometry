# Computational Geometry Project

## Overview
This project implements various computational geometry algorithms, focusing on convex hulls, linear programming, Delaunay triangulation, and geometric search. <br>
The code is organized into multiple modules, each solving specific geometry-related problems and demonstrating core computational methods.

## Algorithms Implemented

### Convex Hull Algorithms
- **Incremental Algorithm (Graham Scan)**: Sorts points by x-coordinates and constructs the hull by adding points and removing non-hull points.
- **Gift Wrapping Algorithm**: Builds the hull by iteratively selecting boundary points in a clockwise direction.
- **Divide and Conquer Algorithm**: Divides points into subsets, recursively computes hulls for each subset, and merges them.
- **QuickHull (2D and 3D)**: Computes the hull using the QuickHull method for both 2D and 3D points.

### Linear Programming
This module solves linear programming problems, parsing constraints from a configuration file and solving them using the `scipy.optimize.linprog` function.

### Delaunay Triangulation
Utilizes Voronoi diagrams and Delaunay triangulation techniques. The triangulation's duality with the Voronoi diagram allows for visualization and efficient computation of geometric relationships.

### Geometric Search
Implements a 2D KD-tree to conduct rectangular range searches, retrieving points within specified boundaries efficiently.

## Project Structure

```
.
├── src
│   ├── main.py           # Main entry point for running algorithms
│   ├── utils.py          # Helper functions for data handling and visualization
│   └── algorithms        # Directory containing algorithm implementations
│       ├── graham_scan.py
│       ├── gift_wrapping.py
│       ├── divide_and_conquer.py
│       └── quickhull.py
│
├── linear
│   ├── constraints.txt   # Input file with problem constraints
│   ├── linear.py         # Solves the linear programming problem
│   └── utils.py          # Helper functions for reading constraints
│
├── delaunay
│   ├── points.txt        # Input file with random points for triangulation
│   ├── main.py           # Main file to run Delaunay triangulation
│   └── utils.py          # Helper functions for reading points and visualization
│
└── geom_search
    ├── points.txt        # Input file with random points
    ├── result.txt        # Output file with points within a defined search area
    ├── main.py           # Main file to run KD-tree based search
    ├── kd_tree.py        # KD-tree implementation
    └── utils.py          # Helper functions for reading and visualizing points
```

## Installation and Requirements

To run this project, you need Python 3.x and the following packages:

- `scipy` (for `scipy.spatial.ConvexHull` and `scipy.optimize.linprog`)
- `matplotlib` (for visualization)

Install dependencies with:

```bash
pip install -r src/requirements.txt
```

## Usage

### Running Convex Hull Algorithms
Navigate to the `src/convex_hull/src` folder and run the main script to choose and execute any of the convex hull algorithms:

```bash
python main.py
```


### Options include:
- **Incremental Algorithm** (Graham Scan)
- **Gift Wrapping Algorithm**
- **Divide and Conquer Algorithm**
- **QuickHull (2D and 3D)**

### Solving a Linear Programming Problem
Navigate to the `src/linear` directory and and run the main script:

```bash
python main.py
```

Ensure constraints are specified in constraints.txt following the required format.

### Delaunay Triangulation
Navigate to the `src/delaunay` directory and and run the main script:
```bash
python main.py
```

### Geometric Search Using KD-Tree
Navigate to the `src/geom_search` directory and and run the main script:
```bash
python main.py
```




## Results and Visualization

- **Convex Hull Algorithms**: Outputs are saved in the `files/output` directory. Visualization is available for each step except for the QuickHull algorithm.
- **Linear Programming**: Displays the optimal solution to the objective function.
- **Delaunay Triangulation and Voronoi Diagram**: Visualization of Delaunay triangulation and Voronoi diagrams for the generated points.
- **Geometric Search**: Highlights points within the defined rectangular boundary and saves results to `result.txt`.

## Complexity Analysis

- **Convex Hull Algorithms**: Complexity varies by algorithm, ranging from \(O(n \log n)\) for the Graham Scan and Divide and Conquer algorithms, to \(O(nh)\) for Gift Wrapping, where \(h\) is the number of hull vertices.
- **Delaunay Triangulation**: Has a time complexity of \(O(n \log n)\), where \(n\) is the number of points.
- **KD-Tree Range Search**: Constructing the KD-tree requires \(O(n \log n)\), and searching takes \(O(n + k)\), where \(k\) is the number of reported points.