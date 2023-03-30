/*
Tytul: Znajdz i zmodyfikuj pliki spelniajace warunek.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do folderu.
a) Dodaj swoje inicjaly na koncu wszystkich plikow tekstowych znajdujacych sie w
podanym folderze i jego podfolderach. b) Usun srodkowy wiersz z kazdego pliku
CSV znajdujacego sie w podanym folderze i jego podfolderach. Dane wejsciowe:
Napis reprezentujacy sciezke do folderu. Dane wyjsciowe: Brak.

*/
#include <algorithm>
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>

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

void sortujAdresyIp(std::vector<std::string> &ip) {
  std::sort(ip.begin(), ip.end(), [](const auto &lhs, const auto &rhs) {
    std::vector<int> oktetA;
    std::vector<int> oktetB;

    auto fun = [&](std::vector<int> &wektor, const std::string &slowo) {
      std::stringstream ss(slowo);

      for (int i; ss >> i;) {
        wektor.push_back(i);
        if (ss.peek() == '.')
          ss.ignore();
      }
    };

    fun(oktetA, lhs);
    fun(oktetB, rhs);

    if (oktetA == oktetB)
      return false;

    else if (oktetA[0] > oktetB[0])
      return false;

    else if (oktetA[0] < oktetB[0])
      return true;

    else if (oktetA[1] > oktetB[1])
      return false;

    else if (oktetA[1] < oktetB[1])
      return true;

    else if (oktetA[2] > oktetB[2])
      return false;

    else if (oktetA[2] < oktetB[2])
      return true;

    else if (oktetA[3] > oktetB[3])
      return false;

    else if (oktetA[3] < oktetB[3])
      return true;
  });
}

void test1() {
  filesys::path sciezka{"temp.txt"};

  std::ofstream ofs(sciezka);
  ofs << "123.4.245.23\n";
  ofs << "104.244.253.29\n";
  ofs << "1.198.3.93\n";
  ofs << "32.183.93.40\n";
  ofs << "104.30.244.2\n";
  ofs << "104.244.4.1\n";
  ofs.close();

  auto adresyIp = wczytajPlik(sciezka);
  sortujAdresyIp(adresyIp);

  std::vector<std::string> posortowaneAdresy = {
      "1.198.3.93",  "32.183.93.40",   "104.30.244.2",
      "104.244.4.1", "104.244.253.29", "123.4.245.23"};

  assert(adresyIp == posortowaneAdresy);

  filesys::remove(sciezka);
}

int main() {

  test1();

  return 0;
}

