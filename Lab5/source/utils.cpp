#include <cmath>
#include <utility>
#include "city.h"
#include "utils.h"

#include <iostream>

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

float calc_distance(std::vector<City*> cities, std::vector<int> cluster, int centerindex, std::pair<float, float> center) {
    float res = 0;
    int n = cluster.size();
    for(int i=0; i < n; ++i)
        if(cluster[i] == centerindex)
        res += geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), center.first, center.second);
    return res;
}

float calc_distortion(std::vector<City*> cities, std::vector<int> cluster, std::vector<std::pair<float, float>> centers){
    float sum = 0;
    for(int i=0; i<cities.size(); ++i){
      sum += pow(geoDistance(centers[cluster[i]].first, centers[cluster[i]].second, cities[i]->getLatitude(), cities[i]->getLongitude()), 2) * abs(cities[i]->getPopulation());
    }

  return sum;

}