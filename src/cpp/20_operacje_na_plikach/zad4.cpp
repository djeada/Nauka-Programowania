/*
Tytul: Dodaj wiersz do pliku.
Tresc zadania: Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke do
pliku tekstowego, a drugi napis reprezentuje wiersz tekstu. Dodaj otrzymany
wiersz na poczatek pliku tekstowego. Dane wejsciowe: Dwa napisy - sciezka do
pliku oraz wiersz tekstu. Dane wyjsciowe: Brak.

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

