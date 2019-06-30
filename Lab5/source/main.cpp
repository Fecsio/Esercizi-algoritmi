#include "parser.h"
#include "kmeans.h"
#include "pkmeans.h"
#include <iostream>
#include <algorithm>    // std::sort


int main() {
    auto cities = Parser("../cities-and-towns-of-usa.csv");
    int k = 50;
    int cutoff = 0;
    int q = 100;
    int n = cities.size();

    /*
    std::vector<City*> sortedP(cities);
    std::sort (sortedP.begin(), sortedP.end(), City::comparePtrToNode);
    std::vector<std::pair<double, double>> centers;
    
    
    
    centers.reserve(k);
    for(int i=0; i < k; ++i) {
        centers.push_back(std::make_pair(sortedP[n-i-1]->getLatitude(), sortedP[n-i-1]->getLongitude()));
    }*/



    /* DOMANDA 2
    for(int i=10; i<=100; i += 10) {
        std::cout << "# cluster: " << i << std::endl;
        kmeans(cities, i, 100);
    }
    */
    /* DOMANDA 3
    for(int i=10; i<=1000; i += 99) {
        std::cout << "# iterazioni: " << i << std::endl;
        kmeans(cities, 50, i);
    }
    */

    PKmeans(cities, 50, 100);
    std::cout << std::endl;
    Kmeans(cities, 50, 100);
}