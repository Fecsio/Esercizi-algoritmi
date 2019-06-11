#include <cmath>
#include <utility>
#include <vector>
#include "city.h"

#define PI 3.14159265

struct Cluster {
    std::vector<City*> clusterCities;
    std::pair<int, int> center;
};

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

static std::pair<int, int> calc_center(Cluster cluster) {
    std::pair<int, int> res;
    int x = 0;
    int y = 0;
    int n = cluster.clusterCities.size();
    for(int i=0; i < n; ++i) {
        x += cluster.clusterCities[i]->getLatitude();
        y += cluster.clusterCities[i]->getLongitude();
    }
    res.first = x/sizeof(n);
    res.second = y/sizeof(n);
    return res;
}
