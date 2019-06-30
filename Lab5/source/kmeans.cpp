#include <iostream> // ~~~~~~~~~~~~~ DA RIMUOVERE POI
#include <algorithm>    // std::sort
#include <vector>
#include <chrono>
#include <utility>      // std::pair
#include <limits>
#include "kmeans.h"
#include "utils.h"

/* 
 * Partitioning in k cluster
 * 
 * Params:
 *  - cities = vector of n cities (points);
 *  - centers = vector of k centers (as pairs(latitude, longitude));
 *  - cluster = vector of n int, that specify for each i which is the center of the cluster associated with city[i];
 *  - k = # of clusters.
 *  
 * Returns: 
 *  Nothing because it changes values in param cluster (that is passed by reference).
 * 
 * 
 */
void Partition(const std::vector<City*>& cities, const std::vector<std::pair<double, double>>& centers, std::vector<int>& cluster, int k) {   
    //std::cout << "Partitioning start" << std::endl;
    int n = cities.size();
    for(int i = 0; i < n; ++i) { 
        int best_c = 0;    // centroid for city of index i initialized to centers[0]
        double best_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[0].first, centers[0].second);
        for(int z = 1; z < k; ++z) {
            double tmp_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[z].first, centers[z].second);
            if(tmp_dist < best_dist) {
                best_dist = tmp_dist;
                best_c = z;
            }
        }

        cluster[i] = best_c;
    }
}

/**
 * Auxiliar function used to calculate new centroid for a cluster.
 * 
 * Params:
 *  - cluster = vector of n int, that specify for each i which is the cluster associated with city[i];
 *  - cities = vector of n cities (points);
 *  - h = index of the cluster
 *  
 * Returns: 
 *  A pair made of:
 *   1. A pair(latitude, longitude) that is the sum of all cities "in" cluster[h];
 *   2. An int, that is the # of cities "in" cluster[h].
 * 
*/
std::pair<std::pair<double, double>, int> ReduceCluster(const std::vector<int>& cluster, const std::vector<City*>& cities, int h){
    int n = cities.size();
    double lat = 0;
    double lon = 0;
    int size = 0;
    for(int z = 0; z < n; ++z){
        if(cluster[z] == h){
            lat += cities[z]->getLatitude();
            lon += cities[z]->getLongitude();
            size+=1;
        }
    }

    return std::make_pair(std::make_pair(lat, lon), size);
}

/**
 * Serial Kmeans
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
std::pair<std::vector<int>, std::vector<std::pair<double, double>>> Kmeans(std::vector<City*> &cities, int k, int q) { // partition of cities, k clusters, q iteration 
    std::vector<City*> sortedP(cities);
    auto start = std::chrono::system_clock::now();
    
    unsigned int n = cities.size();
    std::sort (sortedP.begin(), sortedP.end(), City::comparePtrToNode);

    std::vector<int> cluster(n, -1);

    std::vector<std::pair<double, double>> centers;
    centers.reserve(k);

    // centers initialization
    for(int i=0; i < k; ++i) {
        centers.push_back(std::make_pair(sortedP[n-i-1]->getLatitude(), sortedP[n-i-1]->getLongitude()));
    }

    int distance[k];
    int totDist = 0;
    int minDist = std::numeric_limits<int>::max();
    int minIt;

    for(int i=0; i < q; ++i) {
        Partition(cities, centers, cluster, k);

        totDist = 0;
        for(int j=0; j < k; ++j) {
            auto sumSize = ReduceCluster(cluster, cities, j);
            double sumLat = sumSize.first.first;
            double sumLong = sumSize.first.second;
            int size = sumSize.second;
            centers[j] = std::make_pair(sumLat/size, sumLong/size);
            distance[j] = calc_distance(cities, cluster, j, centers[j]);
            totDist += distance[j];
        }

        if(totDist < minDist) {
            minDist = totDist;
            minIt = i;
        }
    }

    auto end = std::chrono::system_clock::now();

    std::chrono::duration<double> elapsed_seconds = end-start;
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << minDist << " - " << minIt << std::endl;
    std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";

    //stampo centroidi finali per confronto
    for(auto c: centers){
        std::cout << "(" << c.first << ", " << c.second << ")" << std::endl;
    }

    std::cout << calc_distortion(cities, cluster, centers) << std::endl;

    return std::make_pair(cluster, centers);
}
