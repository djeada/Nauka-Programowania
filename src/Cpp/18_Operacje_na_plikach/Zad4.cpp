#include <fstream>
#include <iostream>
#include <stdexcept>

//Otrzymujesz napis reprezentujący sciezke pliku tekstowego.
//Wczytaj i wypisz tresc pliku.

void wypiszPlik(const std::string& sciezka)
{
    try {
        std::string wiersz;
        std::ifstream plik(sciezka);
        plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit | std::ifstream::badbit);

        while (plik) {
            getline(plik, wiersz);
            std::cout << wiersz << std::endl;
        }

        plik.close();
    }

    catch (std::exception const& e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
}

int main()
{

    const std::string sciezka = "test.txt";
    wypiszPlik(sciezka);

    return 0;
}
