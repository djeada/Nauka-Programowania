/*
Tytul: Usun pliki spelniajace warunek.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do folderu. Usun wszystkie pliki o rozmiarze wiekszym niz 10 kB znajdujace sie w podanym folderze i jego podfolderach.
Dane wejsciowe: Napis reprezentujacy sciezke do folderu.
Dane wyjsciowe: Brak.

*/
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <string>

namespace filesys = std::experimental::filesystem;

int rozmiarPliku(const std::string &sciezka) {
  return filesys::file_size(filesys::path(sciezka));
}

void usunPliki(const std::string &sciezka) {

  for (const auto plik : filesys::directory_iterator(sciezka)) {
    if (rozmiarPliku(plik.path()) > 10240)
      filesys::remove(filesys::path(plik.path()));
  }
}

void testUsunPliki() {

  // stworz folder testowy
  std::string sciezka = "test";
  filesys::create_directory(filesys::path(sciezka));

  // dodaj plik do folderu
  std::string sciezkaPliku = "test/plik.txt";
  std::ofstream plik(sciezkaPliku);
  for (int i = 0; i < 100000; i++)
    plik << "test\n";
  plik.close();

  // usun pliki z testowego folderu
  usunPliki(sciezka);

  // sprawdz czy folder test jest pusty
  assert(filesys::is_empty(filesys::path(sciezka)));

  // usun folder test
  filesys::remove_all(filesys::path(sciezka));
}

int main() {

  testUsunPliki();

  return 0;
}

