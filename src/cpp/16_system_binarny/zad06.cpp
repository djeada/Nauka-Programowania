/*
ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj:

1. liczbę `X` zapisaną w systemie o podstawie `p`
2. podstawę `p` (2..36)
3. podstawę docelową `q` (2..36)

i wypisz reprezentację `X` w systemie o podstawie `q`.

### Wejście

Trzy linie:

1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
2. `p` (2..36)
3. `q` (2..36)

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi o formacie

* `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
* Dla wartości 10..35 stosuj `A..Z`.

*/
#include <algorithm>
#include <cassert>
#include <stdexcept>
#include <string>

int naDziesietny(std::string liczba, int staraPodstawa) {
  /*
   * Funkcja zamienia liczbe z reprezentacji w systemie stara_podstawa na
   * reprezentacje w systemie dziesietnym.
   */

  int reprezentacjaDziesietna = 0;

  for (char znak : liczba) {
    int cyfra;
    if (znak >= 'A' && znak <= 'Z')
      cyfra = znak - 'A' + 10;
    else
      cyfra = znak - '0';

    reprezentacjaDziesietna = reprezentacjaDziesietna * staraPodstawa + cyfra;
  }

  return reprezentacjaDziesietna;
}

void zmianaPodstawy(std::string &liczba, int staraPodstawa, int nowaPodstawa) {
  /*
   * Funkcja zamienia liczbe z reprezentacji w systemie stara_podstawa na
   * reprezentacje w systemie nowa_podstawa.
   */
  const int maksymalnaPodstawa = 10 + 'Z' - 'A' + 1;
  if (staraPodstawa < 2 || staraPodstawa > maksymalnaPodstawa ||
      nowaPodstawa < 2 || nowaPodstawa > maksymalnaPodstawa)
    throw std::invalid_argument("Podstawa systemu musi byc z zakresu 2-36");

  int reprezentacjaDziesietna = naDziesietny(liczba, staraPodstawa);
  liczba = "";
  const int podstawa = nowaPodstawa;

  if (reprezentacjaDziesietna == 0) {
    liczba = "0";
    return;
  }

  while (reprezentacjaDziesietna > 0) {
    int reszta = reprezentacjaDziesietna % podstawa;
    reprezentacjaDziesietna /= podstawa;

    char nowyZnak = '0' + reszta;

    if (nowyZnak > '9') nowyZnak = 'A' + (nowyZnak - '9') - 1;

    liczba += nowyZnak;
  }

  std::reverse(liczba.begin(), liczba.end());
}

void testZmianaPodstawy() {
  std::string liczba = "4301";
  std::string wynik = "1003031";
  zmianaPodstawy(liczba, 10, 4);

  assert(liczba == wynik);
}

void testZmianaPodstawyLitery() {
  std::string liczba = "FF";
  zmianaPodstawy(liczba, 16, 2);
  assert(liczba == "11111111");

  liczba = "35";
  zmianaPodstawy(liczba, 10, 36);
  assert(liczba == "Z");

  liczba = "Z";
  zmianaPodstawy(liczba, 36, 10);
  assert(liczba == "35");

  liczba = "0";
  zmianaPodstawy(liczba, 10, 2);
  assert(liczba == "0");
}

int main() {
  testZmianaPodstawy();
  testZmianaPodstawyLitery();

  return 0;
}
