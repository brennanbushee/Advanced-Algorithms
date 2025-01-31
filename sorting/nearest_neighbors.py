from math import dist
def nearest_neighbours(p_x, p_y, k, n_points):
    """
    Args:
     p_x(int32)
     p_y(int32)
     k(int32)
     n_points(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    euclidean_distance = (dist([p_x, p_y], point) for point in n_points)
    return sorted(n_points, key=lambda point: dist([p_x, p_y], point))[:k]


if __name__ == '__main__':
    print(nearest_neighbours(p_x=1, p_y= 1, k=1, n_points=[[0, 0], [1, 0]])) # Should be [1,0]
    print(nearest_neighbours(p_x=1, p_y=1, k=2, n_points=[[1, 0], [2, 1], [0, 1]]))