#include <iostream> // ~~~~~~~~~~~~~ DA RIMUOVERE POI
#include <algorithm>    // std::sort
#include <vector>
#include <chrono>
#include <utility>      // std::pair
#include <limits>
#include "kmeans.h"
#include "utils.h"

/* 
 * Partizionamento delle città su k clusters
 * 
 */
void Partition(const std::vector<City*>& cities, const std::vector<std::pair<float, float>>& centers, std::vector<int>& cluster, int k) {   
    //std::cout << "Partitioning start" << std::endl;
    int n = cities.size();
    for(int i = 0; i < n; ++i) { 
        int best_c = 0;    // centroid for city of index i initialized to centers[0]
        float best_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[0].first, centers[0].second);
        for(int z = 1; z < k; ++z) {
            float tmp_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[z].first, centers[z].second);
            if(tmp_dist < best_dist) {
                best_dist = tmp_dist;
                best_c = z;
            }
        }

        cluster[i] = best_c;
    }
}

std::pair<std::pair<float, float>, int> ReduceCluster(const std::vector<int>& cluster, const std::vector<City*>& cities, int i, int j, int h){
   /*if(i == j){
        if(cluster[i] == h){
            return std::make_pair(std::make_pair(cities[i]->getLatitude(), cities[i]->getLongitude()), 1);
        }
        
        return std::make_pair(std::make_pair(0,0), 0);
    }

    int mid = (i+j)/2;
    auto left =  ReduceCluster(cluster, cities, i, mid, h);
    auto right = ReduceCluster(cluster, cities, mid + 1, j, h);
    return std::make_pair(std::make_pair(left.first.first + right.first.first, left.first.second + right.first.second), left.second + right.second);  
*/
    int n = cities.size();
    float lat = 0;
    float lon = 0;
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


std::pair<std::vector<int>, std::vector<std::pair<float, float>>> Kmeans(std::vector<City*> &cities, int k, int q) { // partition of cities, k clusters, q iteration 
    std::vector<City*> sortedP(cities);
    auto start = std::chrono::system_clock::now();
    
    unsigned int n = cities.size();
    std::sort (sortedP.begin(), sortedP.end(), City::comparePtrToNode);

    std::vector<int> cluster(n, -1);

    std::vector<std::pair<float, float>> centers;
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
            auto sumSize = ReduceCluster(cluster, cities, 0, n-1, j);
            float sumLat = sumSize.first.first;
            float sumLong = sumSize.first.second;
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

    /*// stampo centroidi finali per confronto
    for(auto c: centers){
        std::cout << "(" << c.first << ", " << c.second << ")" << std::endl;
    }*/

    std::cout << calc_distortion(cities, cluster, centers) << std::endl;

    return std::make_pair(cluster, centers);
}
