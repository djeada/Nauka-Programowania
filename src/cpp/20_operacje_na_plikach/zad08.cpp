/*
Tytul: Znajdz i zmodyfikuj pliki spelniajace warunek.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do folderu.
a) Dodaj swoje inicjaly na koncu wszystkich plikow tekstowych znajdujacych sie w podanym folderze i jego podfolderach.
b) Usun srodkowy wiersz z kazdego pliku CSV znajdujacego sie w podanym folderze i jego podfolderach.
Dane wejsciowe: Napis reprezentujacy sciezke do folderu.
Dane wyjsciowe: Brak.

*/
#include <cassert>
#include <cstring>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>

namespace filesys = std::experimental::filesystem;

std::string znajdzRozszerzenie(std::string sciezka) {

  filesys::path obiekt(sciezka);

  if (obiekt.has_extension())
    return obiekt.extension().string();

  return "";
}

std::vector<std::string> plikiWFolderze(const std::string &sciezka,
                                        const std::string &rozszerzenie) {

  std::vector<std::string> pliki;

  for (const auto plik : filesys::directory_iterator(sciezka)) {
    if (znajdzRozszerzenie(plik.path()) == rozszerzenie)
      pliki.push_back(filesys::path(plik.path()));
  }

  return pliki;
}

void dodajInicjaly(const std::string &sciezkaFolderu, const std::string &dane) {

  auto _dodajInicjaly = [](const std::string &sciezka,
                           const std::string &dane) {
    std::ofstream plik;
    plik.open(sciezka, std::ios::out | std::ios::app);
    if (plik.fail())
      throw std::ios_base::failure(std::strerror(errno));

    plik.exceptions(plik.exceptions() | std::ios::failbit |
                    std::ifstream::badbit);
    plik << dane << std::endl;
  };

  auto sciezki = plikiWFolderze(sciezkaFolderu, ".txt");

  for (const auto &sciezka : sciezki)
    _dodajInicjaly(sciezka, dane);
}

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

void usunSrodkowy(const std::string &sciezkaFolderu) {

  auto _usunSrodkowy = [](const std::string &sciezka) {
    auto trescPliku = wczytajPlik(sciezka);

    try {
      std::string wiersz;
      std::ofstream plik(sciezka);
      plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit |
                      std::ifstream::badbit);

      trescPliku.erase(trescPliku.begin() + trescPliku.size() / 2);

      for (auto &wiersz : trescPliku)
        plik << wiersz + "\n";

      plik.close();
    }

    catch (std::exception const &e) {
      std::cout << "Error: " << e.what() << std::endl;
    }
  };

  auto sciezki = plikiWFolderze(sciezkaFolderu, ".csv");

  for (const auto &sciezka : sciezki)
    _usunSrodkowy(sciezka);
}

void testDodajInicjaly() {

  // stworz folder temp_dir
  filesys::path sciezka{"temp_dir"};
  filesys::create_directories(sciezka);

  // stworz pliki txt
  std::string plikTxt = "temp.txt";

  std::ofstream ofs(sciezka / plikTxt);
  ofs << "przykladowy tekst\n";
  ofs.close();

  // dodaj inicjaly
  std::string dane = "A.D.";
  dodajInicjaly(sciezka, dane);

  // sprawdz czy plik zostal zmodyfikowany
  std::vector<std::string> wynik = {"przykladowy tekst", "A.D."};
  assert(wczytajPlik((sciezka / plikTxt).string()) == wynik);

  // usun folder temp_dir
  filesys::remove_all(sciezka);
}

void testUsunSrodkowy() {

  // stworz folder temp_dir
  filesys::path sciezka{"temp_dir"};
  filesys::create_directories(sciezka);

  // stworz plik temp.csv
  std::string plikCsv = "temp.csv";
  std::ofstream ofs(sciezka / plikCsv);
  ofs << "test1; test2; test3\n";
  ofs << "test4; test5; test6\n";
  ofs << "test7; test8; test9\n";
  ofs.close();

  // usun srodkowy wiersz z pliku
  usunSrodkowy(sciezka);

  // sprawdz czy plik zostal zmieniony
  std::vector<std::string> wynik = {"test1; test2; test3\n",
                                    "test7; test8; test9\n"};
  assert(wczytajPlik((sciezka / plikCsv).string()) == wynik);

  // usun folder temp_dir
  filesys::remove_all(sciezka);
}

int main() {

  testDodajInicjaly();
  testUsunSrodkowy();

  return 0;
}

