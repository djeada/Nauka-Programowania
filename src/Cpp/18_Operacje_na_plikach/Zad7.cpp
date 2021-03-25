#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>
//Otrzymujesz dwa napisy. Pierwszy reprezentuje sciezke pliku tekstowego.
//Drugi wiersz tekstu. Dodaj wiersz na poczatku pliku.

std::vector<std::string> wczytajPlik(const std::string& sciezka)
{

    std::vector<std::string> tresc;
    try {
        std::string wiersz;
        std::ifstream plik(sciezka);
        plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit | std::ifstream::badbit);

        while (plik) {
            getline(plik, wiersz);
            tresc.push_back(wiersz);
        }

        plik.close();
    }

    catch (std::exception const& e) {
        std::cout << "Error : " << e.what() << std::endl;
    }

    return tresc;
}

void zapiszNaPoczatku(const std::string& sciezka, const std::string& dane)
{

    auto trescPliku = wczytajPlik(sciezka);

    try {
        std::string wiersz;
        std::ofstream plik(sciezka);
        plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit | std::ifstream::badbit);

        plik << dane;
        for (auto& wiersz : trescPliku)
            plik << wiersz + "\n";

        plik.close();
    }

    catch (std::exception const& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
}

int main()
{

    const std::string sciezka = "folder/test.txt";
    zapiszNaPoczatku(sciezka, "Hej \n");

    return 0;
}
