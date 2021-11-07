#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <pwd.h>
#include <sys/types.h>
#include <unistd.h>

namespace filesys = std::experimental::filesystem;

/*
Otrzymujesz napis reprezentujacy nazwe pliku. Przeszukaj caly
system i zapisz w liscie wszystkie sciezki plikow o danej nazwie.
*/

std::string katalogDomowy() {

#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
  return std::string(getenv("HOMEDRIVE")) + std::string(getenv("HOMEPATH"));

#else
  const char *homedir;

  if ((homedir = getenv("HOME")) == NULL)
    homedir = getpwuid(getuid())->pw_dir;

  return std::string(homedir);
#endif

  return "";
}

std::vector<std::string> plikiWFolderze(const std::string &sciezkaFolderu,
                                        const std::string &szukanyPlik) {

  std::vector<std::string> listaSciezek;
  try {
    for (auto &file : filesys::recursive_directory_iterator(sciezkaFolderu)) {
      if (file.path().filename().string() == szukanyPlik)
        listaSciezek.push_back(file.path());
    }
  }

  catch (std::system_error &e) {
    std::cerr << "Exception :: " << e.what();
  }

  return listaSciezek;
}

std::vector<std::string> sciezkiWSystemie(const std::string &szukanyPlik) {
  return plikiWFolderze(katalogDomowy(), szukanyPlik);
}

void test1() {

  const std::string szukanyPlik = "test.txt";

  // stworz dwa foldery
  filesys::path sciezka{"temp_dir"};
  filesys::create_directories(sciezka);
  filesys::create_directories(sciezka / sciezka);

  std::vector<std::string> nazwyPlikow{"lista.txt", szukanyPlik};

  // umiesc dwa tymczaowe pliki w utworzonych folderach
  for (const auto nazwa : nazwyPlikow) {
    std::ofstream ofs(sciezka / nazwa);
    std::ofstream ofs2(sciezka / sciezka / nazwa);
    ofs << "przykladowy tekst.\n";
    ofs2 << "przykladowy tekst.\n";
    ofs.close();
    ofs2.close();
  }

  auto wynik = sciezkiWSystemie(szukanyPlik);

  // sprawdz czy tymczasowe pliku znajduja sie w liscie znalezionych plikow
  assert(std::count(wynik.begin(), wynik.end(),
                    filesys::canonical(sciezka / szukanyPlik)));
  assert(std::count(wynik.begin(), wynik.end(),
                    filesys::canonical(sciezka / sciezka / szukanyPlik)));

  filesys::remove_all(sciezka);
}

int main() {

  test1();

  return 0;
}
