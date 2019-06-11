#ifndef CITY_H
#define CITY_H
#include <string>

using namespace std;
class City {
  private:
    int id;
    string name;
    int population;
    float latitude;
    float longitude;
  public:
    City(int id, string name, int pop, float lat, float lon);
    int getId() const; 
    string getName() const; 
    float getLatitude() const; 
    float getLongitude() const; 
    int getPopulation() const;
    bool operator<(const City&) const;
};

#endif //CITY.H
