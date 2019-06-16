#include <iostream>
#include <algorithm>    // std::sort
#include <map>
#include <vector>
#include <typeinfo>
#include <chrono>
#include <utility>      // std::pair
#include "kmeans.h"
#include "utils.h"

int calc_distance(std::vector<City*> cities, std::vector<int> clusterCityIndexes, std::pair<float, float> *centers, int centerIndex) {
    int res = 0;
    for(int i=0; i < clusterCityIndexes.size(); ++i)
        res += geoDistance(cities[clusterCityIndexes[i]]->getLatitude(), cities[clusterCityIndexes[i]]->getLongitude(), centers[centerIndex].first, centers[centerIndex].second);
    return res;
}

/* 
 * Partizionamento delle città su k clusters
 * std::map<std::pair<float, float>, std::vector<int>>> --> map(center pair, cities indexes)
 */
std::map<int, std::vector<int>> partition(std::vector<City*> cities, std::pair<float, float> *centers, int k) {
    std::map<int, std::vector<int>> c;
    
    //std::cout << "Partitioning start" << std::endl;
    for(int i = 0; i < cities.size(); ++i) {
        int best_c = 0;    // centroid for city of index i initialized to centers[0]
        float best_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[0].first, centers[0].second);
        for(int z = 1; z < k; ++z) {
            float tmp_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[z].first, centers[z].second);
            if(tmp_dist < best_dist) {
                best_dist = tmp_dist;
                best_c = z;
            }
        }
        c[best_c].push_back(i);
        //if(i >= 10 && i < 50) 
        //    std::cout << "best_dist for " << i << " at " << best_c << ": " << best_dist << std::endl;
    }
    return c;
}

// Calculate new centroids (cities: cities in database, clusterCityIndexes: index of cities in the cluster)
std::pair<float, float> calc_center(std::vector<City*> &cities, std::vector<int> clusterCityIndexes) {
    std::pair<float, float> res;
    float x = 0.0;
    float y = 0.0;
    int n = clusterCityIndexes.size();
    for(int i=0; i < n; ++i) {
        x += cities[clusterCityIndexes[i]]->getLatitude();
        y += cities[clusterCityIndexes[i]]->getLongitude();
    }
    if(n == 0)
        ++n;
    res.first = x/n;
    res.second = y/n;
    return res;
}

void kmeans(std::vector<City*> &cities, int k, int q) { // partition of cities, k clusters, q iteration 
    std::vector<City*> sortedP(cities);
    auto start = std::chrono::system_clock::now();
    
    std::sort (sortedP.begin(), sortedP.end(), City::comparePtrToNode);

    std::pair<float, float> centers[k];
    std::map<int, std::vector<int>> clusters;
    std::pair<float, float> old_centers[k];
    int distance[k];
    int totDist = 0;
    int minDist = 999999999;
    int minIt;
    // centers initialization
    for(int i=0; i < k; ++i) {
        centers[i] = std::make_pair(sortedP[sortedP.size()-i-1]->getLatitude(), sortedP[sortedP.size()-i-1]->getLongitude());
        // std::cout << "initial centers: " << centers[i].first << ", " << centers[i].second << std::endl;
    }
    for(int i=0; i < q; ++i) {
        clusters = partition(cities, centers, k);
        totDist = 0;
        for(int j=0; j < k; ++j) {
            // std::cout << "Cluster " << j << ": " << centers[j].first << ", " << centers[j].second << " - size: " << clusters[j].size() << std::endl;
            centers[j] = calc_center(cities, clusters[j]);
            distance[j] = calc_distance(cities, clusters[j], centers, j);
            // std::cout << "Distanza dal cluster " << j << ": " << distance[j] << " - Distanza media: " << distance[j]/k << std::endl;
            totDist += distance[j];
        }
        if(totDist < minDist) {
            minDist = totDist;
            minIt = i;
        }
        // std::cout << "Distanza totale: " << totDist << std::endl << "--------------------------------------------------------" << std::endl;
    }
    auto end = std::chrono::system_clock::now();

    std::chrono::duration<double> elapsed_seconds = end-start;
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << minDist << " - " << minIt << std::endl;
    std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";
}
