#include <iostream>
#include <algorithm>    // std::sort
#include <map>
#include <vector>
#include <utility>      // std::pair
#include "city.h"
// #include "utils.cpp"

/*
partition(std::vector<City*> cities, int* centers) {
    
}
*/

static void kmeans(std::vector<City*> &cities, int k, int q) { //Cluster
    std::vector<City*> sortedP(cities);
    std::sort(*sortedP.begin(), *sortedP.end()-1);   
    std::cout << sortedP[0]->getName() << " (" << sortedP[0]->getPopulation() << ")\n"
              << sortedP[1]->getName() << " (" << sortedP[1]->getPopulation() << ")\n"
              << sortedP[2]->getName() << " (" << sortedP[2]->getPopulation() << ")\n"
              << sortedP[3]->getName() << " (" << sortedP[3]->getPopulation() << ")\n"
              << sortedP[4]->getName() << " (" << sortedP[4]->getPopulation() << ")\n";
}
