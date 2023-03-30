/*
Tytul: Przesun wszystkie pliki CSV do jednego folderu.
Tresc zadania: Otrzymujesz dwa napisy reprezentujace sciezki do folderow.
Przenies wszystkie pliki CSV z pierwszego folderu (oraz jego podfolderow) do
drugiego folderu. Dane wejsciowe: Dwa napisy reprezentujace sciezki do folderow.
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

