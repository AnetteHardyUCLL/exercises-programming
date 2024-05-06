def closest(points, target_point):
    def distance_two_points(point):
        x, y = point
        distance_x = x - target_x
        distance_y = y - target_y
        return distance_x**2 + distance_y**2

    target_x, target_y = target_point
    return min(points, key=distance_two_points)
