/*
ZAD-03 — Sortowanie przez wstawianie

**Poziom:** ★★☆
**Tagi:** `sorting`, `insertion-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania
przez wstawianie**. Buduj posortowany fragment od lewej strony: każdy kolejny
element „wstaw” w odpowiednie miejsce, przesuwając większe elementy w prawo.

### Wejście

* 1 linia: lista liczb całkowitych

### Wyjście

* 1 linia: posortowana lista rosnąco

### Przykład

**Wejście:**

```
[6, 2, 1, 4, 27]
```

**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

* Działa bardzo dobrze dla danych prawie posortowanych.

*/

#include <cassert>
#include <vector>

void sortuj(std::vector<int> &lista) {
  for (unsigned int i = 1; i < lista.size(); i++) {
    int klucz = lista[i];
    int j = i - 1;

    while (j >= 0 && lista[j] > klucz) {
      lista[j + 1] = lista[j];
      j--;
    }

    lista[j + 1] = klucz;
  }
}

void test1() {
  std::vector<int> lista({4, 2, 5, 3, 1});
  std::vector<int> wynik({1, 2, 3, 4, 5});

  sortuj(lista);

  assert(lista == wynik);
}

int main() {
  test1();

  return 0;
}

// Kompilowano z uzyciem komendy: g++-10 -ggdb3 -O0 -std=c++20 -Wall -Wextra
// -pedantic -o main.out Zad3.cpp
