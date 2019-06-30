#ifndef CITY_H
#define CITY_H
#include <string>

using namespace std;
class City {
  private:
    int id;
    string name;
    int population;
    double latitude;
    double longitude;
  public:
    City(int id, string name, int pop, double lat, double lon);
    int getId() const; 
    string getName() const; 
    double getLatitude() const; 
    double getLongitude() const; 
    int getPopulation() const;
    static bool comparePtrToNode(City*, City*);
    bool operator<(const City&) const;
};

#endif //CITY.H
