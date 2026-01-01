/*
ZAD-03 — Znajdź wszystkie ścieżki plików o danej nazwie (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `walk`, `recursive`, `pathlib`

### Treść

Otrzymujesz nazwę pliku (np. `raport.docx`). Przeszukaj cały system plików i
znajdź wszystkie pliki o tej nazwie. Wypisz listę pełnych ścieżek do
znalezionych plików.

### Wejście

* 1 linia: `filename` (np. `raport.docx`)

### Wyjście

* 1 linia: lista pełnych ścieżek (napisy)

### Przykład

**Wejście:**

```
raport.docx
```

**Wyjście:**

```
[
  'C:\Users\Username\Documents\raport.docx',
  'D:\Projekty\Raporty\raport.docx',
  'E:\Backup\raport.docx'
]
```

### Uwagi

* W środowisku testowym możesz nie mieć uprawnień do wszystkich katalogów —
program powinien to bezpiecznie obsłużyć (np. pomijać niedostępne miejsca).

*/
#include <pwd.h>
#include <sys/types.h>
#include <unistd.h>

#include <algorithm>
#include <cassert>
#include <cstdlib>
#include <experimental/filesystem>
#include <fstream>
#include <iostream>

namespace filesys = std::experimental::filesystem;

std::string katalogDomowy() {
#if defined(WIN32) || defined(_WIN32) || defined(__WIN32__) || defined(__NT__)
  return std::string(getenv("HOMEDRIVE")) + std::string(getenv("HOMEPATH"));

#else
  const char *homedir;

  if ((homedir = getenv("HOME")) == NULL) homedir = getpwuid(getuid())->pw_dir;

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
