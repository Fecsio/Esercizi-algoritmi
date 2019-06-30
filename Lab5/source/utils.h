#ifndef UTILS_H
#define UTILS_H
#include <utility>
#include <vector>

#define PI 3.14159265

double convertRadians(double);

double geoDistance(double dLat1, double dLong1, double dLat2, double dLong2);

double calc_distance(std::vector<City*> cities, std::vector<int> cluster, int centerindex, std::pair<double, double> center);

double calc_distortion(std::vector<City*> cities, std::vector<int> cluster, std::vector<std::pair<double, double>> centers);

#endif