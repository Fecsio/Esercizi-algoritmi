#include <cilk/cilk.h>
#include <numeric>
#include "pkmeans.h"
#include "utils.h"
/**
 * Auxiliar parallel function used to calculate new centroid for a cluster.
 * 
 * Params:
 *  - cluster = vector of n int, that specify for each i which is the cluster associated with city[i];
 *  - cities = vector of n cities (points);
 *  - i = index of the first element of vector cities to process;
 *  - j = index of the last element of vector cities to process;
 *  - h = index of the cluster.
 *  - cutoff = int that identify the treshold below which the function utilizes a sequential iterative algorithm.
 *  
 * Returns: 
 *  A pair made of:
 *   1. A pair(latitude, longitude) that is the sum of all cities "in" cluster[h];
 *   2. An int, that is the # of cities "in" cluster[h].
 * 
*/
std::pair<std::pair<double, double>, int> PReduceCluster(const std::vector<int>& cluster, const std::vector<City*>& cities, int i, int j, int h, int cutoff){
    if(j-i <= cutoff){
        double lat = 0;
        double lon = 0;
        int size = 0;

        for(int z = i; z <= j; ++z){
            if(cluster[z] == h){
                lat += cities[z]->getLatitude();
                lon += cities[z]->getLongitude();
                size+=1;
            }
        }

        return std::make_pair(std::make_pair(lat, lon), size);

    }

    int mid = (i+j)/2;
    auto left = cilk_spawn PReduceCluster(cluster, cities, i, mid, h, cutoff); // spawn
    auto right = PReduceCluster(cluster, cities, mid + 1, j, h, cutoff);
    cilk_sync; // sync
    return std::make_pair(std::make_pair(left.first.first + right.first.first, left.first.second + right.first.second), left.second + right.second);  
}

/* 
 * Parallel partitioning in k cluster
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
void PPartition(const std::vector<City*>& cities, const std::vector<std::pair<double, double>>& centers, std::vector<int>& cluster, int i, int j, int k, int cutoff) {   
    if(j-i <= cutoff){
        for(int z = i; z <= j; ++z){
            int best_c = 0;    // centroid for city of index i initialized to centers[0]
            double best_dist = geoDistance(cities[z]->getLatitude(), cities[z]->getLongitude(), centers[0].first, centers[0].second);
            for(int c = 1; c < k; ++c) {
                double tmp_dist = geoDistance(cities[z]->getLatitude(), cities[z]->getLongitude(), centers[c].first, centers[c].second);
                if(tmp_dist < best_dist) {
                    best_dist = tmp_dist;
                    best_c = c;
                }
            }

        cluster[z] = best_c;
        }
    }

    else{
        int mid = (i+j)/2;
        cilk_spawn PPartition(cities, centers, cluster, i, mid, k, cutoff);
        PPartition(cities, centers, cluster, mid + 1, j, k, cutoff);
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
std::pair<std::vector<int>, std::vector<std::pair<double, double>>> PKmeans(const std::vector<City*>& cities, const std::vector<std::pair<double, double>>& initial_centroids ,int k, int q, int cutoff){
    int n = cities.size();
    std::vector<int> cluster(n, -1);

    std::vector<std::pair<double, double>> centers(initial_centroids);

    for(int i = 0; i<q; ++i){

        PPartition(cities, centers, cluster, 0, n-1, k, cutoff); // side-effect on cluster

        cilk_for(int f = 0; f < k; ++f){
            auto sumSize = PReduceCluster(cluster, cities, 0, n-1, f, cutoff);
            double sumLat = sumSize.first.first;
            double sumLong = sumSize.first.second;
            int size = sumSize.second;
            centers[f] = std::make_pair(sumLat/size, sumLong/size);
        }
    }

    return std::make_pair(cluster, centers);

}



