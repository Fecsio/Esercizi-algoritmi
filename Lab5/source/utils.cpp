#include <cmath>
#include <utility>
#include <vector>
#include "city.h"
#include "utils.h"

float convertRadians(float x) {
  int deg1 = int(x);
  float min1 = x - deg1;
  return PI * (deg1 + 5.0 * min1 / 3.0) / 180.0;
}

float geoDistance(float dLat1, float dLong1, float dLat2, float dLong2) {
  float earthRadius = 6378.388;
  float lat1 = convertRadians(dLat1);
  float lat2 = convertRadians(dLat2);
  float long1 = convertRadians(dLong1);
  float long2 = convertRadians(dLong2);
  float q1 = cos(long1 - long2);
  float q2 = cos(lat1 - lat2);
  float q3 = cos(lat1 + lat2);
  return int(earthRadius * acos(0.5*((1.0 + q1)*q2 - (1.0 - q1)*q3)) + 1.0);
}
