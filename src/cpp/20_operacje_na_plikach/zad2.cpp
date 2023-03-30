/*
Tytul: Plik z lista adresow IP.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego.
Kazdy wiersz pliku reprezentuje adres IP. Posortuj adresy IP i zapisz je w
liscie. Dane wejsciowe: Napis reprezentujacy sciezke do pliku. Dane wyjsciowe:
Lista adresow IP posortowanych alfabetycznie.

*/
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <string>
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
      pliki.push_back(filesys::path(plik.path()).filename());
  }

  return pliki;
}

void test1() {

  filesys::path sciezka{"temp_dir"};
  filesys::create_directories(sciezka);

  std::vector<std::string> nazwyPlikow{"lista.txt", "test.txt"};

  for (const auto nazwa : nazwyPlikow) {
    std::ofstream ofs(sciezka / nazwa);
    ofs << "przykladowy tekst.\n";
    ofs.close();
  }

  std::string rozszerzenie = ".txt";
  assert(plikiWFolderze(sciezka.string(), rozszerzenie) == nazwyPlikow);

  filesys::remove_all(sciezka);
}

int main() {

  test1();

  return 0;
}

