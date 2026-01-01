/*
ZAD-01 — Czy ścieżka istnieje?

**Poziom:** ★☆☆
**Tagi:** `files`, `path`, `os`, `pathlib`

### Treść

Otrzymujesz ścieżkę w systemie plików. Sprawdź, czy odnosi się do istniejącego
**pliku lub folderu**.

### Wejście

* 1 linia: `path` (napis — ścieżka)

### Wyjście

* 1 linia: `Prawda` jeśli ścieżka istnieje, w przeciwnym razie `Fałsz`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik.txt
```

**Wyjście:**

```
Prawda
```

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
    if (filesys::exists(obiekt) && filesys::is_directory(obiekt)) return true;
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
