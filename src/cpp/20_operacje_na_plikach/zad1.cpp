/*
Tytul: Sprawdzenie, czy sciezka nalezy do pliku/folderu
Tresc: Otrzymujesz napis reprezentujacy sciezke. Sprawdz, czy jest to sciezka do
pliku lub folderu. Dane wejsciowe: Napis Dane wyjsciowe: Wartosc logiczna

*/
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>

namespace filesys = std::experimental::filesystem;

bool czyPlik(std::string sciezka) {
  try {
    filesys::path obiekt(sciezka);
    if (filesys::exists(obiekt) && filesys::is_regular_file(obiekt))
      return true;
  }

  catch (filesys::filesystem_error &e) {
    std::cerr << e.what() << std::endl;
  }

  return false;
}

bool czyFolder(std::string sciezka) {
  try {
    filesys::path obiekt(sciezka);
    if (filesys::exists(obiekt) && filesys::is_directory(obiekt))
      return true;
  }

  catch (filesys::filesystem_error &e) {
    std::cerr << e.what() << std::endl;
  }

  return false;
}

void test1() {
  filesys::path sciezkaPliku{"temp.txt"};

  std::ofstream ofs(sciezkaPliku);
  ofs << "przykladowy tekst.\n";
  ofs.close();

  assert(czyPlik(sciezkaPliku.string()));
  assert(!czyFolder(sciezkaPliku.string()));

  filesys::remove(sciezkaPliku);
}

void test2() {

  filesys::path sciezkaFolderu{"temp_dir"};
  filesys::create_directories(sciezkaFolderu);

  assert(!czyPlik(sciezkaFolderu.string()));
  assert(czyFolder(sciezkaFolderu.string()));

  filesys::remove(sciezkaFolderu);
}

int main() {

  test1();
  test2();

  return 0;
}

// Compiling with g++ -std=c++17 Zad1.cpp -lstdc++fs -o exe

