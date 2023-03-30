/*
Tytul: Wczytaj i wypisz tresc pliku.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego. Wczytaj plik i wypisz jego tresc.
Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
Dane wyjsciowe: Napis zawierajacy tresc pliku.

*/
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>

namespace filesys = std::experimental::filesystem;

void wypiszPlik(const std::string &sciezka) {
  try {
    std::string wiersz;
    std::ifstream plik(sciezka);
    plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit |
                    std::ifstream::badbit);

    while (plik) {
      getline(plik, wiersz);
      std::cout << wiersz << std::endl;
    }

    plik.close();
  }

  catch (std::exception const &e) {
    std::cout << "Error: " << e.what() << std::endl;
  }
}

int main() {

  const std::string sciezka = "test.txt";

  std::ofstream ofs(sciezka);
  ofs << "przykladowy tekst.\n";
  ofs.close();

  wypiszPlik(sciezka);

  filesys::remove(sciezka);

  return 0;
}

