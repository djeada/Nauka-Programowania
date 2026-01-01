/*
ZAD-02 — Pliki o danym rozszerzeniu w folderze (bez podfolderów)

**Poziom:** ★★☆
**Tagi:** `files`, `dir`, `listdir`, `pathlib`

### Treść

Otrzymujesz ścieżkę do folderu i rozszerzenie (np. `.txt`). Znajdź wszystkie
pliki o tym rozszerzeniu znajdujące się **bezpośrednio** w tym folderze (bez
przeszukiwania podfolderów). Zwróć listę nazw plików.

### Wejście

* 1 linia: `folder_path`
* 2 linia: `ext` (np. `.txt`)

### Wyjście

* 1 linia: lista nazw plików w formacie `['a.txt', 'b.txt']`

### Przykład

**Wejście:**

```
C:\Users\Username\Documents
.txt
```

**Wyjście:**

```
['dokument1.txt', 'notatki.txt', 'lista_zakupów.txt']
```

### Uwagi o formatowaniu

* Porównuj rozszerzenia **bez względu na wielkość liter** (np. `.TXT` też pasuje
do `.txt`).

*/
#include <cassert>
#include <experimental/filesystem>
#include <fstream>
#include <string>
#include <vector>

namespace filesys = std::experimental::filesystem;

std::string znajdzRozszerzenie(std::string sciezka) {
  filesys::path obiekt(sciezka);

  if (obiekt.has_extension()) return obiekt.extension().string();

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
