#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>

namespace filesys = std::experimental::filesystem;

/*
Otrzymujesz napis reprezentujący ścieżkę pliku tekstowego. 
Wczytaj i wypisz treść pliku.
*/

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
