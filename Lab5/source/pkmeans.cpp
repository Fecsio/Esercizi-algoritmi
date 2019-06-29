#include "pkmeans.h"
#include "utils.h"

#include <cilk/cilk.h>
#include <algorithm>    // std::sort
#include <chrono>
#include <iostream>
#include <numeric>


std::pair<std::pair<float, float>, int> PReduceCluster(const std::vector<int>& cluster, const std::vector<City*>& cities, int i, int j, int h){
    if(i == j){
        if(cluster[i] == h){
            return std::make_pair(std::make_pair(cities[i]->getLatitude(), cities[i]->getLongitude()), 1);
        }
        
        return std::make_pair(std::make_pair(0,0), 0);
    }

    int mid = (i+j)/2;
    auto left = cilk_spawn PReduceCluster(cluster, cities, i, mid, h);
    auto right = PReduceCluster(cluster, cities, mid + 1 , j, h);
    cilk_sync;
    return std::make_pair(std::make_pair(left.first.first + right.first.first, left.first.second + right.first.second), left.second + right.second);  
}

/* 
 * Partizionamento delle città su k clusters
 */

void Partition(const std::vector<City*>& cities, const std::vector<std::pair<float, float>>& centers, std::vector<int>& cluster, int k) {   
    //std::cout << "Partitioning start" << std::endl;
    int n = cities.size();
    cilk_for (int i = 0; i < n; ++i) { // parallel for
        int best_c = 0;    // centroid for city of index i initialized to centers[0]
        float best_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[0].first, centers[0].second);
        for(unsigned int z = 1; z < k; ++z) {
            float tmp_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[z].first, centers[z].second);
            if(tmp_dist < best_dist) {
                best_dist = tmp_dist;
                best_c = z;
            }
        }

        cluster[i] = best_c;
        //if(i >= 10 && i < 50) 
        //    std::cout << "best_dist for " << i << " at " << best_c << ": " << best_dist << std::endl;
    }
}

/**
 * Parallel k-means
 *  
 * Params:
 *  cities = std::vector of cities (points)
 *  q = # of iteractions
 *  k = # of clusters
 * 
 * Returns: 
 *  A pair made of: 
 *  1. A vector of n = cities.size() int, where an int at position i identify the center 
 *     of the cluster in which cities[i] is, that is, the index of that center in the array of point 2.;
 *  2. A vector of size = k, in which are stored centers (point (latitude, longitude)), calculated in the 
 *     last iteraction of the algorithm.
 * 
*/
std::pair<std::vector<int>, std::vector<std::pair<float, float>>> PKmeans(std::vector<City*>& cities, int k, int q){

    unsigned int n = cities.size();
    std::vector<City*> sortedP(cities);

    auto start = std::chrono::system_clock::now();

    std::sort (sortedP.begin(), sortedP.end(), City::comparePtrToNode);

    std::vector<int> cluster(n, -1);

    std::vector<std::pair<float, float>> centers;
    centers.reserve(k);
    // ~~~~~~~~~~~~
    int distance[k];
    int totDist = 0;
    int minDist = 999999999;
    int minIt;
    //~~~~~~~~~~~~

    // centers initialization
    for(int i=0; i < k; ++i) {
        centers.push_back(std::make_pair(sortedP[n-i-1]->getLatitude(), sortedP[n-i-1]->getLongitude()));
        // std::cout << "initial centers: " << centers[i].first << ", " << centers[i].second << std::endl;
    }

    std::cout << centers.size() << std::endl;
    std::cout << cluster.size() << std::endl;


    for(int i = 0; i<q; ++i){

        Partition(cities, centers, cluster, k); // side-effect on cluster

        cilk_for(unsigned int f = 0; f < k; ++f){
            auto sumSize = PReduceCluster(cluster, cities, 0, n-1, f);
            float sumLat = sumSize.first.first;
            float sumLong = sumSize.first.second;
            int size = sumSize.second;
            centers[f] = std::make_pair(sumLat/size, sumLong/size);
        }
    }
    
    std::cout << centers.size() << std::endl;

    for(auto c: centers){
        std::cout << "(" << c.first << ", " << c.second << ")" << std::endl;
    }

    return std::make_pair(cluster, centers);

}



