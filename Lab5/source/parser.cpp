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
    kmeans(cities, 50, 100);
}