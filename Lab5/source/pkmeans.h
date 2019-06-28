#include <map>
#include <vector>
#include <utility>      // std::pair
#include "city.h"

// std::map<std::pair<int, int>, std::vector<City*>>    --> map(center pair, cities)
// std::map<std::pair<float, float>, std::vector<int>> partition(std::vector<City*>, std::pair<float, float>*);

std::pair<std::pair<float, float>, int> PReduceCluster(const std::vector<int>&, const std::vector<City*>&, int , int , int );

// void pkmeans(std::vector<City*>&, int, int);