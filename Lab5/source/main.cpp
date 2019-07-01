#include <chrono>
#include <iostream>
#include <fstream>
#include "parser.h"
#include "kmeans.h"
#include "pkmeans.h"
#include "utils.h"

int main() {

    std::ofstream outputFile("../risultati2.csv");
    outputFile << "Algoritmo, numero di punti, cluster, iterazioni, popolazione, cutoff, tempo(ms)" << std::endl;

    // ~~~~~~~~~~~~~~~~ DOMANDA 1 ~~~~~~~~~~~~~~~~
    /*outputFile << "DOMANDA" << std::endl;
    int k = 50;
    int q = 100;
    int min_pop[7] = {100000, 50000, 15000, 5000, 2000, 250, -999};

    for(int i: min_pop){
        auto cities = Parser("../cities-and-towns-of-usa.csv", i); 
        int n = cities.size();
        std::vector<std::pair<double, double>> initial_centroids = calculate_initial_centroids(cities, k);

        auto start = std::chrono::system_clock::now();
        Kmeans(cities, initial_centroids, k, q);
        auto end = std::chrono::system_clock::now();

        std::chrono::duration<double> elapsed_seconds = end-start;
        auto millis = std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_seconds).count();
        outputFile << "Seriale," << n << "," << k << "," << q << "," << i << ", ," << millis << std::endl;

        start = std::chrono::system_clock::now();
        PKmeans(cities, initial_centroids, k, q);
        end = std::chrono::system_clock::now();

        elapsed_seconds = end-start;
        millis = std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_seconds).count();
        outputFile << "Parallelo," << n << "," << k << "," << q << "," << i << ",0," << millis << std::endl;


    }

    // ~~~~~~~~~~~~~~~~ DOMANDA 2 ~~~~~~~~~~~~~~~~
    outputFile << "DOMANDA" << std::endl;

    q = 100;

    for(k = 10; k<=100; k += 10){
        auto cities = Parser("../cities-and-towns-of-usa.csv"); 
        int n = cities.size();
        std::vector<std::pair<double, double>> initial_centroids = calculate_initial_centroids(cities, k);

        auto start = std::chrono::system_clock::now();
        Kmeans(cities, initial_centroids, k, q);
        auto end = std::chrono::system_clock::now();

        std::chrono::duration<double> elapsed_seconds = end-start;
        auto millis = std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_seconds).count();
        outputFile << "Seriale," << n << "," << k << "," << q << "," << 38183 << ", ," << millis << std::endl;


        start = std::chrono::system_clock::now();
        PKmeans(cities, initial_centroids, k, q);
        end = std::chrono::system_clock::now();

        elapsed_seconds = end-start;
        millis = std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_seconds).count();
        outputFile << "Parallelo," << n << "," << k << "," << q << "," << 38183 << ",0," << millis << std::endl;

    }

    // ~~~~~~~~~~~~~~~~ DOMANDA 3 ~~~~~~~~~~~~~~~~
    outputFile << "DOMANDA" << std::endl;
    k = 50;

    for(q = 10; q<=1000; q += 90){
        auto cities = Parser("../cities-and-towns-of-usa.csv"); 
        int n = cities.size();
        std::vector<std::pair<double, double>> initial_centroids = calculate_initial_centroids(cities, k);

        auto start = std::chrono::system_clock::now();
        Kmeans(cities, initial_centroids, k, q);
        auto end = std::chrono::system_clock::now();

        std::chrono::duration<double> elapsed_seconds = end-start;
        auto millis = std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_seconds).count();
        outputFile << "Seriale," << n << "," << k << "," << q << "," << 38183 << ", ," << millis << std::endl;


        start = std::chrono::system_clock::now();
        PKmeans(cities, initial_centroids, k, q);
        end = std::chrono::system_clock::now();

        elapsed_seconds = end-start;
        millis = std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_seconds).count();
        outputFile << "Parallelo," << n << "," << k << "," << q << "," << 38183 << ",0," << millis << std::endl;

        
    }*/
    // ~~~~~~~~~~~~~~~~ DOMANDA 4 ~~~~~~~~~~~~~~~~
    outputFile << "DOMANDA" << std::endl;
    int k = 50;
    int q = 100;

    for(int cutoff = 10; cutoff <= 38183; cutoff += 647){
        auto cities = Parser("../cities-and-towns-of-usa.csv"); 
        int n = cities.size();
        std::vector<std::pair<double, double>> initial_centroids = calculate_initial_centroids(cities, k);

        auto start = std::chrono::system_clock::now();
        PKmeans(cities, initial_centroids, k, q, cutoff);
        auto end = std::chrono::system_clock::now();

        std::chrono::duration<double> elapsed_seconds = end-start;
        auto millis = std::chrono::duration_cast<std::chrono::milliseconds>(elapsed_seconds).count();
        outputFile << "Parallelo," << n << "," << k << "," << q << "," << 38183 << "," << cutoff << "," << millis << std::endl;

    }

}