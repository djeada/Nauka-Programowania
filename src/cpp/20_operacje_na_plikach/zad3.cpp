/*
Tytul: Statystyki dla pliku tekstowego.
Tresc zadania: Otrzymujesz napis reprezentujacy sciezke do pliku tekstowego.
Oblicz: a) Liczbe wierszy w pliku. b) Liczbe slow w pliku (slowa oddzielone sa
spacjami i moga skladac sie wylacznie z liter). c) Srednia dlugosc wiersza. d)
Srednia liczbe slow na wiersz. e) Czestosc wystepowania kazdego ze slow w pliku.
Dane wejsciowe: Napis reprezentujacy sciezke do pliku.
Dane wyjsciowe:
a) Liczba naturalna reprezentujaca liczbe wierszy.
b) Liczba naturalna reprezentujaca liczbe slow.
c) Liczba zmiennoprzecinkowa reprezentujaca srednia dlugosc wiersza.
d) Liczba zmiennoprzecinkowa reprezentujaca srednia liczbe slow na wiersz.
e) Slownik par: napis (slowo), liczba naturalna (czestotliwosc wystepowania
slowa). Przyklad: Dla otrzymanego napisu:
"C:\Users\Username\Documents\text_file.txt" powinno zostac zwrocone: a) Liczba
naturalna reprezentujaca liczbe wierszy, np. 6 b) Liczba naturalna
reprezentujaca liczbe slow, np. 25 c) Liczba zmiennoprzecinkowa reprezentujaca
srednia dlugosc wiersza, np. 41.5 d) Liczba zmiennoprzecinkowa reprezentujaca
srednia liczbe slow na wiersz, np. 4.2 e) Slownik par: napis (slowo), liczba
naturalna (czestotliwosc wystepowania slowa): {'The': 2, 'quick': 2, 'brown': 2,
'fox': 2, 'jumped': 1, 'over': 1, 'the': 1, 'lazy': 1, 'dog.': 1, 'cat': 1,
'sat': 1, 'on': 1, 'mat.': 1, 'Foxes': 1, 'are': 1, 'known': 1, 'for': 1,
'their': 2, 'cunning': 1, 'and': 1, 'intelligence.': 1, 'Dogs': 1, 'loyalty': 1,
'kindness.': 1, 'Cats': 1, 'independent': 1, 'animals': 1, 'but': 1, 'can': 1,
'be': 1, 'affectionate.': 1, 'This': 1, 'text': 1, 'file': 1, 'contains': 1,
'ten': 1, 'lines': 1, 'and': 1, 'words.': 1} Tekst pliku: "The quick brown fox
jumped over the lazy dog. The quick brown cat sat on the mat. Foxes are known
for their cunning and intelligence. Dogs are known for their loyalty and
kindness. Cats are independent animals but can be affectionate. This text file
contains six lines and 25 words."

*/
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

