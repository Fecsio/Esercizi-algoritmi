 #include "pkmeans.h"
 #include <cilk/cilk.h>
 #include <iterator>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

class CSVRow {
    public:
        std::string const& operator[](std::size_t index) const {
            return m_data[index];
        }
        std::size_t size() const {
            return m_data.size();
        }
        void readNextRow(std::istream& str) {
            std::string line;
            std::getline(str, line);

            std::stringstream lineStream(line);
            std::string cell;

            m_data.clear();
            while(std::getline(lineStream, cell, ',')) {
                m_data.push_back(cell);
            }
            // This checks for a trailing comma with no data after it.
            if (!lineStream && cell.empty()) {
                // If there was a trailing comma then add an empty element.
                m_data.push_back("");
            }
        }
    private:
        std::vector<std::string> m_data;
};

std::istream& operator>>(std::istream& str, CSVRow& data) {
    data.readNextRow(str);
    return str;
}   

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

int main() {
    std::ifstream file("../cities-and-towns-of-usa.csv");
    std::vector<City*> cities;
    CSVRow row;
    int id, pop;
    float lat, lon;
    int minpop = -999;    // DOMANDA 1
    std::string line;
    // skip the first line with the header
    std::getline(file, line);
    while(file >> row) {
        std::stringstream(row[2]) >> pop;
        if(pop >= minpop) {
            std::stringstream(row[0]) >> id;
            std::stringstream(row[3]) >> lat;
            std::stringstream(row[4]) >> lon; 
            cities.push_back(new City(id, row[1], pop, lat, lon));
        }
    }
    std::cout << cities.size() << std::endl;

    std::vector<int> cluster;
    cluster.reserve(cities.size());
    std::cout << cities.size();
    cluster.push_back(3);

    for (auto i = 0; i<cities.size()/2; ++i){
        cluster.push_back(1);
        cluster.push_back(0);

    }

    auto r = PReduceCluster(cluster, cities, 0, cluster.size() - 1, 1);
    std::cout << "(" << r.first.first << "," << r.first.second << ")" << " " << r.second << endl;

}
