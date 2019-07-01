#ifndef UTILS_H
#define UTILS_H
#include <utility>
#include <vector>

#define PI 3.14159265

double convertRadians(double);

double geoDistance(double dLat1, double dLong1, double dLat2, double dLong2);

// ~~~~~~ used for tests
double calc_distance(std::vector<City*> cities, std::vector<int> cluster, int centerindex, std::pair<double, double> center);

// ~~~~~~ used for tests
double calc_distortion(std::vector<City*> cities, std::vector<int> cluster, std::vector<std::pair<double, double>> centers);

std::vector<std::pair<double, double>> calculate_initial_centroids(const std::vector<City *>& cities, int k);

#endif