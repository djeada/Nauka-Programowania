/*
ZAD-09 — Usuń pliki większe niż 10 kB (rekurencyjnie)

**Poziom:** ★★☆
**Tagi:** `files`, `delete`, `size`, `recursive`

### Treść

Otrzymujesz ścieżkę do folderu. Usuń wszystkie pliki o rozmiarze **> 10240
bajtów** w tym folderze i jego podfolderach.

### Wejście

* 1 linia: `folder_path`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\DoUsunięcia
```

**Wyjście:**
*(brak)*

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
  for (int i = 0; i < 100000; i++) plik << "test\n";
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
