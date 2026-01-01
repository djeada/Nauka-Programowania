/*
ZAD-05 — Sortowanie szybkie

**Poziom:** ★★☆
**Tagi:** `sorting`, `quick-sort`, `recursion`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **Quick Sort**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
2. Wybierz **pivot** (np. pierwszy element).
3. Podziel elementy na trzy grupy:

   * mniejsze od pivota,
   * równe pivotowi,
   * większe od pivota.
4. Rekurencyjnie posortuj część mniejszych i większych.
5. Sklej wynik: `mniejsze + równe + większe`.

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

* Średnio: `O(n log n)`, w pesymistycznym przypadku: `O(n^2)`.
* Wybór pivota ma wpływ na wydajność.

*/

#include <cassert>
#include <functional>
#include <vector>

int rozdziel(std::vector<int> &lista, int indeksPocz, int indeksKonc) {
  int wartosc = lista[indeksKonc];
  int i = indeksPocz - 1;
  for (int j = indeksPocz; j < indeksKonc; j++) {
    if (lista[j] <= wartosc) {
      i++;
      std::swap(lista[i], lista[j]);
    }
  }

  std::swap(lista[i + 1], lista[indeksKonc]);

  return i + 1;
}

void sortuj(std::vector<int> &lista) {
  std::function<void(std::vector<int> &, int, int)> _sortuj;
  _sortuj = [&_sortuj](std::vector<int> &lista, int p, int r) {
    if (p < r) {
      int q = rozdziel(lista, p, r);
      _sortuj(lista, p, q - 1);
      _sortuj(lista, q + 1, r);
    }
  };

  _sortuj(lista, 0, lista.size() - 1);
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
// -pedantic -o main.out Zad5.cpp
