/*
ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

**Poziom:** ★★★
**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej reprezentacji binarnej znajdź długość
najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami**
(tzw. *binary gap*).

Jeśli nie ma takiego ciągu — wypisz `0`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego „gapu”.

### Przykład

**Wejście:**

```
14
```

**Wyjście:**

```
0
```

### Uwagi (ważne)

* `14` ma zapis `1110` — zero na końcu **nie jest otoczone jedynkami z prawej**,
więc wynik to `0`. Dla przykładu `20` (`10100`) najdłuższy gap ma długość `1`
(między `1` i `1`).

*/
#include <algorithm>
#include <cassert>

int najdluzszyCiagZer(int liczba) {
  /*
   * Funkcja zwraca dlugosc najdluzszego ciagu zer otoczonego z obu stron
   * jedynkami w binarnej reprezentacji liczby.
   */
  if (liczba <= 0) return 0;

  // Zera na koncu liczby nie sa otoczone jedynkami z prawej strony.
  while (liczba % 2 == 0) liczba /= 2;

  int wynik = 0;
  int pom = 0;

  while (liczba != 0) {
    int reszta = liczba % 2;
    liczba /= 2;
    if (reszta == 1) {
      wynik = std::max(wynik, pom);
      pom = 0;
    } else
      pom++;
  }
  return wynik;
}

void testNajdluzszyCiagZer() {
  assert(najdluzszyCiagZer(111) == 1);
  assert(najdluzszyCiagZer(8219) == 8);
  assert(najdluzszyCiagZer(14) == 0);
  assert(najdluzszyCiagZer(20) == 1);
  assert(najdluzszyCiagZer(9) == 2);
  assert(najdluzszyCiagZer(1) == 0);
  assert(najdluzszyCiagZer(0) == 0);
}

int main() {
  testNajdluzszyCiagZer();

  return 0;
}
