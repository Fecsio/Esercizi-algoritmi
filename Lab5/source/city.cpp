#include <iostream>
#include "city.h"

City::City(int id, string name, int pop, float lat, float lon): 
            id(id), name(name), population(pop), latitude(lat), longitude(lon) {}

int City::getId() const {
  return id;
}

string City::getName() const {
  return name;
}

float City::getLatitude() const {
  return latitude;
}

float City::getLongitude() const {
  return longitude;
}

int City::getPopulation() const {
  return population;
}

bool City::comparePtrToNode(City* c1, City* c2) { return (*c1 < *c2); }

bool City::operator<(const City& c) const {
  if(getPopulation() < c.getPopulation()) 
    return true;
  return false;
}
