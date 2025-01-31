def optimal_fire_station_location(houses):
    # Extract x and y coordinates separately
    x_coords = [house[0] for house in houses]
    y_coords = [house[1] for house in houses]

    # Sort the coordinates to find the median
    x_coords.sort()
    y_coords.sort()

    # Find the median of the x and y coordinates
    n = len(houses)
    if n % 2 == 1:
        median_x = x_coords[n // 2]
        median_y = y_coords[n // 2]
    else:
        median_x = (x_coords[n // 2 - 1] + x_coords[n // 2]) / 2
        median_y = (y_coords[n // 2 - 1] + y_coords[n // 2]) / 2

    return (median_x, median_y)

# Example usage:
houses = [(1, 2), (3, 6), (5, 1), (9, 7), (4, 3)]
optimal_location = optimal_fire_station_location(houses)
print(optimal_location)  # Output: (4, 3)
