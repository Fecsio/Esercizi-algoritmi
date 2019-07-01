#include <cmath>
#include <utility>
#include "city.h"
#include "utils.h"
#include <algorithm>    // std::partial_sort_copy

double convertRadians(double x) {
  int deg1 = int(x);
  double min1 = x - deg1;
  return PI * (deg1 + 5.0 * min1 / 3.0) / 180.0;
}

double geoDistance(double dLat1, double dLong1, double dLat2, double dLong2) {
  double earthRadius = 6378.388;
  double lat1 = convertRadians(dLat1);
  double lat2 = convertRadians(dLat2);
  double long1 = convertRadians(dLong1);
  double long2 = convertRadians(dLong2);
  double q1 = cos(long1 - long2);
  double q2 = cos(lat1 - lat2);
  double q3 = cos(lat1 + lat2);
  return int(earthRadius * acos(0.5*((1.0 + q1)*q2 - (1.0 - q1)*q3)) + 1.0);
}

double calc_distance(std::vector<City*> cities, std::vector<int> cluster, int centerindex, std::pair<double, double> center) {
    double res = 0;
    int n = cluster.size();
    for(int i=0; i < n; ++i)
        if(cluster[i] == centerindex)
        res += geoDistance(cities[i]->getLatitude(), cities[i]->getLongitude(), center.first, center.second);
    return res;
}

double calc_distortion(std::vector<City*> cities, std::vector<int> cluster, std::vector<std::pair<double, double>> centers){
    double sum = 0;
    for(int i=0; i<cities.size(); ++i){
      int pop = cities[i]->getPopulation();
      //if(pop < 0 ) pop = 0;
      sum += pow(geoDistance(centers[cluster[i]].first, centers[cluster[i]].second, cities[i]->getLatitude(), cities[i]->getLongitude()), 2) * pop;
    }

  return sum;

}

std::vector<std::pair<double, double>> calculate_initial_centroids(const std::vector<City *>& cities, int k){
  std::vector<City*> sortedP(k);
    std::partial_sort_copy(
        cities.begin(), cities.end(),
        sortedP.begin(), sortedP.end(), 
        City::comparePtrToNodeMax
    );

    std::vector<std::pair<double, double>> centroids;
    centroids.reserve(k);
    for(int i=0; i < k; ++i) {
        centroids.push_back(std::make_pair(sortedP[i]->getLatitude(), sortedP[i]->getLongitude()));
    }

    return centroids;
}
