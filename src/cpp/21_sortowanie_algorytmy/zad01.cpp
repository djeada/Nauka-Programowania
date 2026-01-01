/*
ZAD-01 — Sortowanie bąbelkowe

**Poziom:** ★☆☆
**Tagi:** `sorting`, `bubble-sort`, `list`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania
bąbelkowego**. Algorytm polega na wielokrotnym porównywaniu sąsiednich elementów
i zamianie ich miejscami, jeśli są w złej kolejności. Powtarzaj przebiegi, aż w
całym przebiegu nie zajdzie żadna zamiana.

### Wejście

* 1 linia: lista liczb całkowitych, np. `[6, 2, 1, 4, 27]`

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

* Po każdym pełnym przebiegu największy element „wypływa” na koniec.
* W kolejnych przebiegach możesz zmniejszać zakres sprawdzania o 1.

*/

#include <cassert>
#include <vector>

void swap(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

void sortuj(std::vector<int> &lista) {
  for (long unsigned int i = 0; i < lista.size(); i++) {
    for (long unsigned int j = i + 1; j < lista.size(); j++) {
      if (lista[i] > lista[j]) swap(&lista[i], &lista[j]);
    }
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
// -pedantic -o main.out Zad1.cpp
