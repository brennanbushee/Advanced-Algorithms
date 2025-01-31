from collections import namedtuple
from math import sqrt
import random
import matplotlib.pyplot as plt

# Define a named tuple for points
Point = namedtuple('Point', ['x', 'y'])

def generate_random_points(n, x_range, y_range):
    """ Generate n random points within the specified ranges. """
    return [Point(random.uniform(*x_range), random.uniform(*y_range)) for _ in range(n)]


def plot_points_and_median(points, median):
    """ Plot the points and the geometric median on a grid. """
    x_values = [p.x for p in points]
    y_values = [p.y for p in points]

    plt.scatter(x_values, y_values, label='Points')
    plt.scatter(median.x, median.y, color='red', label='Geometric Median')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)

    plt.title('Geometric Median and Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.show()

def total_distance(p: Point, points: list) -> float:
    """ Calculate the total distance from point p to all points in the list. """
    return sum(sqrt((p.x - q.x) ** 2 + (p.y - q.y) ** 2) for q in points)


def weiszfeld_algorithm(points: list, tolerance: float = 1e-6) -> Point:
    """
    Find the geometric median using Weiszfeld's algorithm.
    Args:
        points: List of Point tuples.
        tolerance: The convergence tolerance.

    Returns:
        A Point that is the geometric median.
    """
    # Start with an initial guess, usually the centroid of the points
    x = sum(p.x for p in points) / len(points)
    y = sum(p.y for p in points) / len(points)
    print(f"Initial guess: {x=}, {y=}")

    while True:
        num_x, num_y = 0, 0
        denom = 0
        #Compute weighted average of points based on their distance to the current estimate.
        for p in points:
            dist = sqrt((x - p.x) ** 2 + (y - p.y) ** 2)
            if dist != 0:
                num_x += p.x / dist
                num_y += p.y / dist
                denom += 1 / dist

        new_x, new_y = num_x / denom, num_y / denom

        # Check for convergence
        if sqrt((new_x - x) ** 2 + (new_y - y) ** 2) < tolerance:
            break

        x, y = new_x, new_y

    return Point(new_x, new_y)


# Example usage
n = 20
x_range = (-10, 10)
y_range = (-10, 10)
# points = [Point(20, 30), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
points = generate_random_points(n, x_range, y_range)
median = weiszfeld_algorithm(points)

print(f"The geometric median is at ({median.x}, {median.y})")

plot_points_and_median(points, median)
