#include "parser.h"
#include "kmeans.h"
#include "pkmeans.h"

int main() {
    auto cities = Parser("../cities-and-towns-of-usa.csv");
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
    Kmeans(cities, 10, 10);
}