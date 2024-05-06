def overlapping_intervals(interval1, interval2):
    # Unpack bounds
    left1, right1 = interval1
    left2, right2 = interval2

    # Check if one of interval2's bounds fall inside interval1
    return left1 <= left2 <= right1 or left1 <= right2 <= right1
