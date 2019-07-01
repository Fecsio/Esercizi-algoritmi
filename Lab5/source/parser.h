#ifndef PARSER_H
#define PARSER_H
#include <string>
#include <vector>
#include "city.h"

class CSVRow {
    public:
        std::string const& operator[](std::size_t) const;
        std::size_t size() const;
        void readNextRow(std::istream&);

    private:
        std::vector<std::string> m_data;
};

std::istream& operator>>(std::istream&, CSVRow&);

std::vector<City*> Parser(const std::string& filepath, int minpop = -999);

#endif