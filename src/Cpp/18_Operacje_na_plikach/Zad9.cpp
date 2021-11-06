#include <experimental/filesystem>
#include <string>
#include <cassert>
#include <fstream>

namespace filesys = std::experimental::filesystem;

/*
Otrzymujesz napis reprezentujący ścieżkę folderu. Usuń 
wszystkie pliki o rozmiarach większych niż 10 kB znajdujące 
się w podanym folderze oraz jego podfolderach.
*/

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

  // stwórz folder testowy
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
