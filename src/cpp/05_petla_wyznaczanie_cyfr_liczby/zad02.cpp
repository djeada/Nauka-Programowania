/*
ZAD-02 — Wypisywanie cyfr liczby w odwrotnej kolejności

**Poziom:** ★☆☆
**Tagi:** `pętle`, `modulo`, `dzielenie całkowite`

### Treść

Wczytaj liczbę naturalną `n` i wypisz jej cyfry w kolejności od cyfry jedności
(czyli w odwrotnej kolejności niż w zapisie liczby). Każdą cyfrę wypisz w
osobnej linii.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 0`)

### Wyjście

Kolejne cyfry `n` w odwrotnej kolejności, każda w nowej linii.

### Przykład

**Wejście:**

```
8214
```

**Wyjście:**

```
4
1
2
8
```

### Uwagi o formatowaniu

* Dla `n = 0` wypisz jedną linię z `0`.

*/
#include <iostream>

int main() {
  int liczba;
  std::cin >> liczba;

  if (liczba == 0) {
    std::cout << "0" << std::endl;
    return 0;
  }

  while (liczba > 0) {
    std::cout << liczba % 10 << std::endl;
    liczba = liczba / 10;
  }

  return 0;
}
