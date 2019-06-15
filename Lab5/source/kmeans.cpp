#include <iostream>
#include <algorithm>    // std::sort
#include <map>
#include <vector>
#include <typeinfo>

#include <chrono>

#include <utility>      // std::pair
#include "kmeans.h"
#include "utils.h"

int counti=0, countb=0;
/* 
 * Partizionamento delle città su k clusters
 * std::map<std::pair<float, float>, std::vector<int>>> --> map(center pair, cities indexes)
 */
std::map<std::pair<float, float>, std::vector<int>> partition(std::vector<City*> cities, std::pair<float, float> *centers, int k) {
    std::map<std::pair<float, float>, std::vector<int>> c;  // sostituire la coppia di punti con indice di centers?
    //std::cout << "Partitioning start" << std::endl;
    for(int i = 0; i < cities.size(); ++i) {
        std::pair<float, float> best_c = centers[0];    // centroid for city of index i initialized to centers[0]
        float best_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[0].first, centers[0].second);
        for(int z = 1; z < k; ++z) {
            float tmp_dist = geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), centers[z].first, centers[z].second);
            if(tmp_dist < best_dist) {
                best_dist = tmp_dist;
                best_c = centers[z];
            }
        }
        // std::cout << "best_c: " << best_c.first << ", " << best_c.second << ". Inserimento indice " << i << std::endl;
        c[best_c].push_back(i); // non elimina vecchi centroidi/clusters!
    }
    return c;
}

// Calcolo nuovi centroidi
std::pair<float, float> calc_center(std::vector<City*> &cities, std::vector<int> clusterCityIndexes) {
    std::pair<float, float> res;
    int x = 0;
    int y = 0;
    int n = clusterCityIndexes.size();
    for(int i=0; i < n; ++i) {
        x += cities[clusterCityIndexes[i]]->getLatitude();
        y += cities[clusterCityIndexes[i]]->getLongitude();
    }
    res.first = x/sizeof(n);
    res.second = y/sizeof(n);
    std::cout << "res.first: " << res.first << "res.second: " << res.second << std::endl;
    return res;
}

void kmeans(std::vector<City*> &cities, int k, int q) { // partition of cities, k clusters, q iteration 
    std::vector<City*> sortedP(cities);
    // auto start = std::chrono::system_clock::now();
    
    std::sort (sortedP.begin(), sortedP.end(), City::comparePtrToNode);

    // auto end = std::chrono::system_clock::now();

    // std::chrono::duration<double> elapsed_seconds = end-start;
    // std::time_t end_time = std::chrono::system_clock::to_time_t(end);

    // std::cout << "elapsed time: " << elapsed_seconds.count() << "s\n";
    std::pair<float, float> centers[k];
    std::map<std::pair<float, float>, std::vector<int>> clusters;
    std::pair<float, float> old_centers[k];

    // centers initialization
    for(int i=0; i < k; ++i) {
        centers[i] = std::make_pair(sortedP[sortedP.size()-i-1]->getLatitude(), sortedP[sortedP.size()-i-1]->getLongitude());
        std::cout << "initial centers: " << centers[i].first << ", " << centers[i].second << std::endl;
    }
    std::cout << "q= " << q << std::endl;
    for(int i=0; i < q; ++i) {
        clusters = partition(cities, centers, k);

        /*
        if(i == q-1)
            for(int z=0; z < k; ++z)
                old_centers[z] = centers[z];
        */
        for(int j=0; j < k; ++j) 
            centers[j] = calc_center(cities, clusters[centers[j]]);
    }
    for(int i=0; i < k; ++i)
        std::cout << "Centroide #" << i << ": " << centers[i].first << ", " << centers[i].second << std::endl;
    // Manca calcolo finale centroidi aggiornati
}
