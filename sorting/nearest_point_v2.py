from collections import namedtuple
from math import dist
from typing import List, Tuple

# Define a named tuple for points
Point = namedtuple('Point', ['x', 'y'])


def update_answer(point1: Point, point2: Point, mindist: float, best_pair: Tuple[int, int]) -> Tuple[
    float, Tuple[int, int]]:
    """
    Update the current minimum distance and best pair of points if the new pair is closer.
    """
    #Try custom distance measure
    # manhattan = abs(point1.x - point2.x) + abs(point1.y - point2.y)
    current_dist = dist((point1.x, point1.y), (point2.x, point2.y))
    if current_dist < mindist:
        mindist = current_dist
        best_pair = (point1, point2)
    return mindist, best_pair


def closest_pair_recursive(points: List[Point], temp: List[Point], left: int, right: int, mindist: float,
                           best_pair: Tuple[int, int]) -> Tuple[float, Tuple[int, int]]:
    if right - left <= 3:
        for i in range(left, right):
            for j in range(i + 1, right):
                mindist, best_pair = update_answer(points[i], points[j], mindist, best_pair)
        points[left:right] = sorted(points[left:right], key=lambda p: p.y)
        return mindist, best_pair

    mid = (left + right) // 2
    mid_x = points[mid].x

    mindist, best_pair = closest_pair_recursive(points, temp, left, mid, mindist, best_pair)
    mindist, best_pair = closest_pair_recursive(points, temp, mid, right, mindist, best_pair)

    # Merge step for y-ordering
    temp[left:right] = sorted(points[left:right], key=lambda p: p.y)
    points[left:right] = temp[left:right]

    temp_size = 0
    for i in range(left, right):
        if abs(points[i].x - mid_x) < mindist:
            for j in range(temp_size - 1, -1, -1):
                if points[i].y - temp[j].y >= mindist:
                    break
                mindist, best_pair = update_answer(points[i], temp[j], mindist, best_pair)
            temp[temp_size] = points[i]
            temp_size += 1

    return mindist, best_pair


def closest_pair(points: List[Point]) -> Tuple[float, Tuple[int, int]]:
    n = len(points)
    temp = [None] * n
    mindist = float('inf')
    best_pair = (-1, -1)

    # Sort points based on x-coordinate before starting the recursive approach
    points.sort(key=lambda p: p.x)
    return closest_pair_recursive(points, temp, 0, n, mindist, best_pair)


# Example usage
#Try a custom distance measure
# manhattan = lambda point1, point2: abs(point1.x - point2.x) + abs(point1.y - point2.y)

points = [Point(2, 3), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
mindist, best_pair = closest_pair(points)
print(f"The smallest distance is {mindist} between points {best_pair}")
