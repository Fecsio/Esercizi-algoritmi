#include "parser.h"
#include "kmeans.h"
#include "pkmeans.h"
#include <iostream>
#include <algorithm>    // std::partial_sort_copy


int main() {
    auto cities = Parser("Lab5/cities-and-towns-of-usa.csv");
    int k = 50;
    int cutoff = 0;
    int q = 100;
    int n = cities.size();

    
    /*   ~~~~~~~~~~~ CREAZIONE CENTROIDI INIZIALI ~~~~~~
    std::vector<City*> sortedP(cities);
    std::sort (sortedP.begin(), sortedP.end(), City::comparePtrToNode);
    std::vector<std::pair<double, double>> centers;
    
    
    
    centers.reserve(k);
    for(int i=0; i < k; ++i) {
        centers.push_back(std::make_pair(sortedP[n-i-1]->getLatitude(), sortedP[n-i-1]->getLongitude()));
    }
    */

    std::vector<City*> sortedP(k);
    std::partial_sort_copy(
        std::begin(cities), std::end(cities),
        std::begin(sortedP), std::end(sortedP), 
        City::comparePtrToNodeMax
    );

    std::vector<std::pair<double, double>> initial_centroids;
    initial_centroids.reserve(k);
    for(int i=0; i < k; ++i) {
        initial_centroids.push_back(std::make_pair(sortedP[i]->getLatitude(), sortedP[i]->getLongitude()));
    }


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

    PKmeans(cities, initial_centroids, 100);
    std::cout << std::endl;
    Kmeans(cities, initial_centroids, 50, 100);
}