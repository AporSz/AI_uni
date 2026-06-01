from hw2.TravellingSalesmanProblem.models.Point import Point

def read_file(filename):
    with open(filename, 'r') as f:
        array = []

        n = int(f.readline())
        for i in range(n):
            line = f.readline()
            x, y = map(int, line.split())
            p = Point(x, y, i)
            array.append(p)

        return array

def bruteforce(array):
    m = float('inf')
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j:
                p1 = array[i]
                p2 = array[j]

                d = p1.distance(p2)
                if d < m:
                    m = d

    return m

result_b = bruteforce(read_file("cmap.in"))

with open('cmap.out', 'w') as f:
    f.write(str(result_b))

# A utility function to find the distance between the closest points of
# strip of a given size. All points in strip[] are sorted according to
# y coordinate. They all have an upper bound on minimum distance as d.
# Note that this method seems to be a O(n^2) method, but it's a O(n)
# method as the inner loop runs at most 6 times
def strip_closest(strip, d):
    min_dist = d
    strip.sort(key=lambda p: p.x)

    for i in range(len(strip)):
        for j in range(i + 1, len(strip)):
            if strip[j].y - strip[i].y >= min_dist:
                break
            min_dist = min(min_dist, strip[i].distance(strip[j]))

    return min_dist

# A recursive function to find the smallest distance. The array Px contains
# all points sorted according to x coordinates and Py contains all points
# sorted according to y coordinates
def closest_util(points):
    n = len(points)

    if n <= 3:
        return bruteforce(points)

    mid = n // 2
    mid_point = points[mid]

    dl = closest_util(points[:mid])
    dr = closest_util(points[mid:])

    d = min(dl, dr)

    strip = [p for p in points if abs(p.x - mid_point.x) < d]

    return min(d, strip_closest(strip, d))

def relation(p1, p2):
    if p1.x != p2.x:
        return p1.x < p2.x
    if p1.y != p2.y:
        return p1.y < p2.y
    return p1.x < p2.x

def closest(points):
    points.sort()
    return closest_util(points)

result_d = closest(read_file("cmap.in"))

print(result_b)
print(result_d)