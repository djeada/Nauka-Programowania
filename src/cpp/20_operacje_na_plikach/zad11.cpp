/*
ZAD-11 — Zamień miejscami treści dwóch plików

**Poziom:** ★★☆
**Tagi:** `files`, `swap`, `read/write`

### Treść

Otrzymujesz ścieżki do dwóch plików. Zamień ich treści miejscami:

* plik A ma mieć dawną treść pliku B,
* plik B ma mieć dawną treść pliku A.

### Wejście

* 1 linia: `file_A`
* 2 linia: `file_B`

### Wyjście

Brak.

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\plik1.txt
C:\Users\Username\Documents\plik2.txt
```

**Wyjście:**
*(brak)*

*/
#include <cassert>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace filesys = std::filesystem;

std::vector<std::string> wczytajPlik(const std::string &sciezka) {
  std::vector<std::string> tresc;
  std::ifstream plik(sciezka);

  if (!plik.is_open()) {
    std::cout << "Error : nie mozna otworzyc pliku " << sciezka << std::endl;
    return tresc;
  }

  std::string wiersz;
  while (std::getline(plik, wiersz)) tresc.push_back(wiersz);

  return tresc;
}

void skopiujPlik(const std::string &sciezka,
                 const std::string &sciezkaDocelowa) {
  try {
    filesys::copy_file(sciezka, sciezkaDocelowa,
                       filesys::copy_options::overwrite_existing);
  } catch (filesys::filesystem_error &e) {
    std::cout << e.what() << std::endl;
  }
}

void zamienPliki(const std::string &sciezkaA, const std::string &sciezkaB) {
  std::string tempSciezka(sciezkaB);

  while (filesys::exists(tempSciezka)) {
    filesys::path sciezka(tempSciezka);
    tempSciezka =
        (sciezka.parent_path() / ("x" + sciezka.filename().string())).string();
  }

  skopiujPlik(sciezkaA, tempSciezka);
  skopiujPlik(sciezkaB, sciezkaA);
  skopiujPlik(tempSciezka, sciezkaB);
  filesys::remove(tempSciezka);
}

void testZamienPliki() {
  // stworz folder test
  std::string sciezkaTest = "test";
  filesys::create_directory(sciezkaTest);

  // stworz pliki
  std::string sciezkaA =
      sciezkaTest + filesys::path::preferred_separator + "plikA.txt";
  std::string sciezkaB =
      sciezkaTest + filesys::path::preferred_separator + "plikB.txt";

  std::string tekstA = "Ala ma kota";
  std::string tekstB = "Kot ma Ale";

  std::ofstream plikA(sciezkaA);
  plikA << tekstA;
  plikA.close();

  std::ofstream plikB(sciezkaB);
  plikB << tekstB;
  plikB.close();

  zamienPliki(sciezkaA, sciezkaB);

  assert(wczytajPlik(sciezkaA) == std::vector<std::string>{tekstB});
  assert(wczytajPlik(sciezkaB) == std::vector<std::string>{tekstA});

  // usun folder test
  filesys::remove_all(sciezkaTest);
}

int main() {
  testZamienPliki();

  return 0;
}
