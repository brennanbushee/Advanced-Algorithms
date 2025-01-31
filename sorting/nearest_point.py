from dataclasses import dataclass
from math import dist

@dataclass
class Point:
    x: int
    y: int


from dataclasses import dataclass
from math import sqrt
from typing import List, Tuple


@dataclass
class Point:
    x: int
    y: int


# Initialize variables
closest_distance = float('inf')
best_pair = None


def update_closest_pair(p1: Point, p2: Point):
    global closest_distance, best_pair
    distance = sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)
    if distance < closest_distance:
        closest_distance = distance
        best_pair = (p1, p2)


def closest_pair_divide_and_conquer(points: List[Point], temp: List[Point], left: int, right: int):
    if right - left <= 3:
        for i in range(left, right):
            for j in range(i + 1, right):
                update_closest_pair(points[i], points[j])
        points[left:right] = sorted(points[left:right], key=lambda p: p.y)
        return

    mid = (left + right) // 2
    mid_x = points[mid].x
    closest_pair_divide_and_conquer(points, temp, left, mid)
    closest_pair_divide_and_conquer(points, temp, mid, right)

    temp[left:right] = sorted(points[left:right], key=lambda p: p.y)

    tsz = 0
    for i in range(left, right):
        if abs(points[i].x - mid_x) < closest_distance:
            for j in range(tsz - 1, -1, -1):
                if points[i].y - temp[j].y >= closest_distance:
                    break
                update_closest_pair(points[i], temp[j])
            temp[tsz] = points[i]
            tsz += 1


def find_closest_pair(points: List[Point]) -> Tuple[int, int]:
    global closest_distance, best_pair
    closest_distance = float('inf')
    best_pair = None

    points = sorted(points, key=lambda p: p.x)
    temp = [None] * len(points)
    closest_pair_divide_and_conquer(points, temp, 0, len(points))

    return best_pair


points = [Point(20, 30), Point(12, 30), Point(40, 50), Point(5, 1), Point(12, 10), Point(3, 4)]
result = find_closest_pair(points)
print(f"The closest pair of points is: {result}, distance = {closest_distance}")

