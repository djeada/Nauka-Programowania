/*
ZAD-07 — Choinka z N trójkątów

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `generowanie`, `print`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`). Wypisz choinkę składającą się z `N`
trójkątów ustawionych jeden pod drugim:

* 1. trójkąt ma wysokość 1,
* 2. trójkąt ma wysokość 2,
* …
* `N`-ty trójkąt ma wysokość `N`.

Każdy trójkąt jest „rosnący” (jak w ZAD-02): w jego wierszu `i` wypisz `i`
gwiazdek.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

Suma wysokości wszystkich trójkątów, czyli `1 + 2 + ... + N` linii.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
*
*
**
*
**
***
```

### Uwagi o formatowaniu

* Nie dodawaj pustych linii między trójkątami.

*/
#include <iostream>

int main() {
  int n;
  std::cin >> n;

  for (int h = 1; h <= n; h++) {
    for (int i = 1; i <= h; i++) {
      for (int j = 0; j < i; j++) {
        std::cout << "*";
      }
      std::cout << std::endl;
    }
  }

  return 0;
}
