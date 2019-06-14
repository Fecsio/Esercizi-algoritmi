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
    City(int, string, int, float, float);
    int getId() const; 
    string getName() const; 
    float getLatitude() const; 
    float getLongitude() const; 
    int getPopulation() const;
    static bool comparePtrToNode(City*, City*);
    bool operator<(const City&) const;
};

#endif //CITY.H
