/*
ZAD-08 — Maksymalny zysk ze sprzedaży sznurka

**Poziom:** ★★★
**Tagi:** `dp`, `rod cutting`, `optymalizacja`

### Treść

Masz sznurek o długości `n` i cennik: ceny kawałków długości od `1` do `n`.
Możesz pociąć sznurek na kawałki o całkowitych długościach. Znajdź maksymalny
zysk.

### Wejście

* 1 linia: lista `prices` (długości 1..n)
* 2 linia: `n` (liczba naturalna)

### Wyjście

* 1 linia: maksymalny zysk (liczba całkowita)

### Przykład

**Wejście:**

```
[1, 5, 8, 9, 10, 17, 17, 20]
4
```

**Wyjście:**

```
10
```

*/
#include <cassert>
#include <stdexcept>
#include <vector>

// Zlozonosc czasowa O(n^n)
// Zlozonosc pamieciowa O(1)
int podzielSznurekV1(std::vector<int> &ceny, int n) {
  if (ceny.size() < n)
    throw std::invalid_argument(
        "Dlugosc sznurka do sprzedazy nie moze byc "
        "wieksza od liczby elementow listy ceny.");

  if (n == 0) return 0;

  auto maks = 0;

  for (auto i = 0; i < n; i++) {
    auto cena = ceny[i] + podzielSznurekV1(ceny, n - i - 1);

    if (cena > maks) maks = cena;
  }

  return maks;
}

// Zlozonosc czasowa O(n^2)
// Zlozonosc pamieciowa O(n)
int podzielSznurekV2(std::vector<int> &ceny, int n) {
  if (ceny.size() < n)
    throw std::invalid_argument(
        "Dlugosc sznurka do sprzedazy nie moze byc "
        "wieksza od liczby elementow listy ceny.");

  std::vector<int> pom(n + 1, 0);

  for (auto i = 0; i < n; i++) {
    for (auto j = 0; j < i + 1; j++)
      pom[i + 1] = std::max(pom[i + 1], ceny[j] + pom[i - j]);
  }

  return pom[n];
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{1, 5, 8, 9, 10, 17, 17, 20};
  auto n = 4;
  auto wynik = 10;

  assert(podzielSznurekV1(lista, n) == wynik);
  assert(podzielSznurekV2(lista, n) == wynik);
}

void test2() {
  std::vector<int> lista{3, 9, 10, 20};
  auto n = 5;

  for (auto funkcja : std::vector<int (*)(std::vector<int> &, int)>(
           {podzielSznurekV1, podzielSznurekV2})) {
    try {
      funkcja(lista, n);
      assert(false);
    } catch (...) {
      assert(true);
    }
  }
}

void test3() {
  std::vector<int> lista{5};
  auto n = 1;
  auto wynik = 5;

  assert(podzielSznurekV1(lista, n) == wynik);
  assert(podzielSznurekV2(lista, n) == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
