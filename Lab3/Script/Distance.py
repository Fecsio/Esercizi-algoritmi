import math


def convertRadians(x):
    deg1 = int(x)
    min1 = x - deg1
    return math.pi * (deg1 + 5 * min1 / 3) / 180


def geoDistance(dLat1, dLong1, dLat2, dLong2):
    earthRadius = 6378.388
    lat1 = convertRadians(dLat1)
    lat2 = convertRadians(dLat2)
    long1 = convertRadians(dLong1)
    long2 = convertRadians(dLong2)
    q1 = math.cos(long1 - long2)
    q2 = math.cos(lat1 - lat2)
    q3 = math.cos(lat1 + lat2)
    dij = int(earthRadius * math.acos(0.5*((1 + q1)*q2 - (1 - q1)*q3)) + 1)
    return dij


def eucDistance(x1, y1, x2, y2):
    return int(math.sqrt((x1 - y1)**2 + (x2 - y2)**2))

