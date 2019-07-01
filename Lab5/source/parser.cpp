#include <iterator>
#include <iostream>
#include <fstream>
#include <sstream>
#include "parser.h"

std::string const& CSVRow::operator[](std::size_t index) const {
    return m_data[index];
}

std::size_t CSVRow::size() const {
    return m_data.size();
}

void CSVRow::readNextRow(std::istream& str) {
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

std::istream& operator>>(std::istream& str, CSVRow& data) {
    data.readNextRow(str);
    return str;
}   

std::vector<City*> Parser(const std::string& filepath, int minpop){
    std::ifstream file(filepath);
    std::vector<City*> cities;
    CSVRow row;
    int id, pop;
    double lat, lon;
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

    return cities;
}