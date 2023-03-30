/*
Tytul: Dodaj wiersz do pliku.
Tresc zadania: Otrzymujesz dwa napisy. Pierwszy napis reprezentuje sciezke do pliku tekstowego, a drugi napis reprezentuje wiersz tekstu. Dodaj otrzymany wiersz na poczatek pliku tekstowego.
Dane wejsciowe: Dwa napisy - sciezka do pliku oraz wiersz tekstu.
Dane wyjsciowe: Brak.

*/
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>

namespace filesys = std::experimental::filesystem;

std::vector<std::string> wczytajPlik(const std::string &sciezka) {

  std::vector<std::string> tresc;
  try {
    std::string wiersz;
    std::ifstream plik(sciezka);
    plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit |
                    std::ifstream::badbit);

    while (plik) {
      getline(plik, wiersz);
      tresc.push_back(wiersz);
    }

    plik.close();
  }

  catch (std::exception const &e) {
    std::cout << "Error : " << e.what() << std::endl;
  }

  return tresc;
}

void zapiszNaPoczatku(const std::string &sciezka, const std::string &dane) {

  auto trescPliku = wczytajPlik(sciezka);

  try {
    std::string wiersz;
    std::ofstream plik(sciezka);
    plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit |
                    std::ifstream::badbit);

    plik << dane;
    for (auto &wiersz : trescPliku)
      plik << wiersz + "\n";

    plik.close();
  }

  catch (std::exception const &e) {
    std::cout << "Error: " << e.what() << std::endl;
  }
}

void test1() {
  filesys::path sciezka{"temp.txt"};

  std::ofstream ofs(sciezka);
  ofs << "przykladowy tekst\n";
  ofs.close();

  zapiszNaPoczatku(sciezka, "Hej \n");
  std::vector<std::string> wynik = {"Hej ", "przykladowy tekst"};

  assert(wczytajPlik(sciezka) == wynik);

  filesys::remove(sciezka);
}

int main() {

  test1();
  return 0;
}

