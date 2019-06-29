#ifndef UTILS_H
#define UTILS_H
#include <utility>
#include <vector>

#define PI 3.14159265

float convertRadians(float);

float geoDistance(float dLat1, float dLong1, float dLat2, float dLong2);

float calc_distance(std::vector<City*> cities, std::vector<int> cluster, int centerindex, std::pair<float, float> center);

#endif