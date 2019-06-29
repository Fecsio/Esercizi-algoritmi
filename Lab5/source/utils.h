#ifndef UTILS_H
#define UTILS_H
#include <cmath>
#include <utility>
#include <vector>

#define PI 3.14159265

float convertRadians(float);

float geoDistance(float, float, float, float);

float calc_distance(std::vector<City*>, std::vector<int>, std::pair<float, float> *, int);

#endif