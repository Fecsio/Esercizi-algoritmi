#ifndef PKMEANS_H
#define PKMEANS_H
#include <vector>
#include <utility>      // std::pair
#include "city.h"

std::pair<std::pair<float, float>, int> PReduceCluster(const std::vector<int>& cluster, const std::vector<City*>& cities, int i, int j, int h, int cutoff);

void PPartition(const std::vector<City*>& cities, const std::vector<std::pair<float, float>>& centers, std::vector<int>& cluster, int k);

std::pair<std::vector<int>, std::vector<std::pair<float, float>>> PKmeans(std::vector<City*>& cities, int k, int q, int cutoff);

#endif