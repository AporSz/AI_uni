import math

# Distance between two points
def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 +
                     (p1[1] - p2[1])**2)

# Brute force
def brute_force(points):
    min_dist = float('inf')
    n = len(points)

    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(min_dist, dist(points[i], points[j]))

    return min_dist

# A utility function to find the distance between the closest points of
# strip of a given size. All points in strip[] are sorted according to
# y coordinate. They all have an upper bound on minimum distance as d.
# Note that this method seems to be a O(n^2) method, but it's a O(n)
# method as the inner loop runs at most 6 times
def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda p: p[1])

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            min_dist = min(min_dist, dist(strip[i], strip[j]))

    return min_dist

# A recursive function to find the smallest distance. The array Px contains
# all points sorted according to x coordinates and Py contains all points
# sorted according to y coordinates
def closest_util(points):
    n = len(points)

    if n <= 3:
        return brute_force(points)

    mid = n // 2
    mid_point = points[mid]

    dl = closest_util(points[:mid])
    dr = closest_util(points[mid:])

    d = min(dl, dr)

    strip = [p for p in points if abs(p[0] - mid_point[0]) < d]

    return min(d, strip_closest(strip, d))

def closest(points):
    points.sort()
    return closest_util(points)

# Driver code
points = [(2, 4), (2, 3), (12, 30), (40, 50),
          (5, 1), (12, 10), (3, 4)]

print("Minimum distance = {:.6f}".format(closest(points)))