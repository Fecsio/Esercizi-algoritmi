#ifndef KMEANS_H
#define KMEANS_H
#include <vector>
#include <utility>      // std::pair
#include "city.h"

void Partition(const std::vector<City*>& cities, const std::vector<std::pair<float, float>>& centers, std::vector<int>& cluster, int k);

std::pair<std::pair<float, float>, int> ReduceCluster(const std::vector<int>& cluster, const std::vector<City*>& cities, int i, int j, int h);

std::pair<std::vector<int>, std::vector<std::pair<float, float>>> Kmeans(std::vector<City*>& cities, int k, int q);

#endif