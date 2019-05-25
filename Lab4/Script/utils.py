import math


def calc_center(points):
    x, y = 0, 0

    for p in points:
        x += p.x
        y += p.y

    n = len(points)

    return x/n, y/n


def euclidean_dist(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)
