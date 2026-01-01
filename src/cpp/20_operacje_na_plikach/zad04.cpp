/*
ZAD-04 — Wczytaj i wypisz treść pliku

**Poziom:** ★☆☆
**Tagi:** `files`, `read`, `encoding`

### Treść

Otrzymujesz ścieżkę do pliku tekstowego. Wczytaj zawartość pliku i wypisz ją.

### Wejście

* 1 linia: `file_path`

### Wyjście

* treść pliku (dokładnie taka jak w pliku)

### Przykład

**Wejście:**

```
C:\Users\Username\Documents\wiadomość.txt
```

**Wyjście:**

```
Witaj! To jest przykładowa treść pliku tekstowego.
```

*/
#include <experimental/filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>

namespace filesys = std::experimental::filesystem;

void wypiszPlik(const std::string &sciezka) {
  try {
    std::string wiersz;
    std::ifstream plik(sciezka);
    plik.exceptions(std::ifstream::eofbit | std::ifstream::failbit |
                    std::ifstream::badbit);

    while (plik) {
      getline(plik, wiersz);
      std::cout << wiersz << std::endl;
    }

    plik.close();
  }

  catch (std::exception const &e) {
    std::cout << "Error: " << e.what() << std::endl;
  }
}

int main() {
  const std::string sciezka = "test.txt";

  std::ofstream ofs(sciezka);
  ofs << "przykladowy tekst.\n";
  ofs.close();

  wypiszPlik(sciezka);

  filesys::remove(sciezka);

  return 0;
}
