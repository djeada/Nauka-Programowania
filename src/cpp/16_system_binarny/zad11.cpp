/*
ZAD-11 — Palindrom w systemie binarnym

**Poziom:** ★★☆
**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej reprezentacja binarna (bez
wiodących zer) jest palindromem.

Wypisz:

* `Prawda` — jeśli tak,
* `Fałsz` — jeśli nie.

### Wejście

* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda` lub `Fałsz`.

### Przykład

**Wejście:**

```
26
```

**Wyjście:**

```
Fałsz
```

### Uwagi (ważne)

* `26` ma zapis binarny `11010`, który **nie** jest palindromem.
  (W Twoim wcześniejszym przykładzie było to opisane błędnie — tu trzymamy się
definicji palindromu 1:1.)

*/
#include <bitset>
#include <cassert>

const int liczbaBitow = 8;

bool czyPalindrom(int liczba) {
  /*
   * Funkcja sprawdza czy podana liczba jest palindromem.
   */
  std::bitset<liczbaBitow> bity = liczba;

  for (int i = 0; i < liczbaBitow / 2 - 1; i++) {
    if (bity[i] ^ bity[liczbaBitow - 1 - i]) return false;
  }

  return true;
}

void testCzyPalindrom() {
  assert(czyPalindrom(231));
  assert(!czyPalindrom(17));
}

int main() {
  testCzyPalindrom();
  return 0;
}
