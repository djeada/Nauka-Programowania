/*
ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego
wystąpienia `klucz` w liście. Jeśli `klucz` nie występuje — wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna liczba całkowita — indeks (od `0`) lub `-1`.

### Przykład

**Wejście:**

```
5
2
9
-1
3
8
-1
```

**Wyjście:**

```
2
```

*/
#include <cassert>
#include <vector>

int znajdzKluczV1(std::vector<int> &lista, int klucz) {
  for (unsigned int i = 0; i < lista.size(); i++) {
    if (lista[i] == klucz) return i;
  }

  return -1;
}

void test1() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  int klucz = 2;
  int wynik = 6;

  assert(znajdzKluczV1(lista, klucz) == wynik);
}

void test2() {
  std::vector<int> lista{3, -2, 4, 9, -3, -40, 8, 5, -7, -1};
  int klucz = 2;
  int wynik = -1;

  assert(znajdzKluczV1(lista, klucz) == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
