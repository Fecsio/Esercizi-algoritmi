#ifndef KMEANS_H
#define KMEANS_H
#include <vector>
#include <utility>      // std::pair
#include "city.h"

void Partition(const std::vector<City*>& cities, const std::vector<std::pair<double, double>>& centers, std::vector<int>& cluster, int k);

std::pair<std::pair<double, double>, int> ReduceCluster(const std::vector<int>& cluster, const std::vector<City*>& cities, int h);

std::pair<std::vector<int>, std::vector<std::pair<double, double>>> Kmeans(std::vector<City*>& cities, std::vector<std::pair<double, double>> centers, int k, int q);

#endif