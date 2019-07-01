#ifndef PKMEANS_H
#define PKMEANS_H
#include <vector>
#include <utility>      // std::pair
#include "city.h"

std::pair<std::pair<double, double>, int> PReduceCluster(const std::vector<int>& cluster, const std::vector<City*>& cities, int i, int j, int h, int cutoff = 0);

void PPartition(const std::vector<City*>& cities, const std::vector<std::pair<double, double>>& centers, std::vector<int>& cluster, int i, int j, int k, int cutoff);

std::pair<std::vector<int>, std::vector<std::pair<double, double>>> PKmeans(const std::vector<City*>& cities, const std::vector<std::pair<double, double>>& initial_centroids ,int k, int q, int cutoff = 0);

#endif