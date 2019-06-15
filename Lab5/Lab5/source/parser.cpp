#include <iterator>
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include "kmeans.h"

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
int main() {
    std::ifstream file("cities-and-towns-of-usa.csv");
    std::vector<City*> cities;
    CSVRow row;
    int id, pop;
    float lat, lon;
    std::string line;
    // skip the first line
    std::getline(file, line);
    while(file >> row) {
        std::stringstream(row[0]) >> id;
        std::stringstream(row[2]) >> pop;
        std::stringstream(row[3]) >> lat;
        std::stringstream(row[4]) >> lon; 
        cities.push_back(new City(id, row[1], pop, lat, lon));
    }
    /**
    // test allocazione City
    for(auto i : cities)
        std::cout << i->getId() << " | " << i->getName() <<  " | " << i->getPopulation() <<  " | " << i->getLatitude() <<  " | " << i->getLongitude() << "\n";
    
    // test operator<
    std::cout << cities[18]->getName() << ": " << cities[18]->getPopulation() << "\n";
    std::cout << cities[23]->getName() << ": " << cities[23]->getPopulation() << "\n";
    if(*cities[18] < *cities[23])
        std::cout << cities[18]->getName() << "(" << cities[18]->getPopulation() << ") <= "<< cities[23]->getName() << "(" << cities[23]->getPopulation() << ")\n"; 
    else
        std::cout << cities[18]->getName() << "(" << cities[18]->getPopulation() << ") > "<< cities[23]->getName() << "(" << cities[23]->getPopulation() << ")\n"; 
    
    std::cout << std::endl << "kmeans" << std::endl;
    */
    kmeans(cities, 5, 1);
    
}