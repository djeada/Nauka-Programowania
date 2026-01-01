/*
ZAD-06 — Czy średnia elementów znajduje się w liście?

**Poziom:** ★☆☆
**Tagi:** `listy`, `średnia`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych. Oblicz średnią arytmetyczną elementów i
sprawdź, czy ta średnia jest **dokładnie** jednym z elementów listy.

Wypisz:

* `Tak` — jeśli średnia występuje w liście,
* `Nie` — w przeciwnym razie.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
```

**Wyjście:**

```
Nie
```

### Uwagi

* Średnia może być ułamkiem — wtedy na pewno nie znajduje się w liście liczb
całkowitych.

*/
#include <cassert>
#include <vector>

int policzSrednia(std::vector<int> &lista) {
  int suma = 0;

  for (auto liczba : lista) suma += liczba;

  return suma / lista.size();
}

bool czySredniaWLiscie(std::vector<int> &lista) {
  int srednia = policzSrednia(lista);

  for (auto liczba : lista) {
    if (liczba == srednia) return true;
  }

  return false;
}

void test1() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  assert(!czySredniaWLiscie(lista));
}

void test2() {
  std::vector<int> lista{1, 2, 3};
  assert(czySredniaWLiscie(lista));
}

int main() {
  test1();
  test2();

  return 0;
}
