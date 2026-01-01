/*
ZAD-03 — Wypisywanie liczby π z określoną dokładnością

**Poziom:** ★☆☆
**Tagi:** `math.pi`, `formatowanie`, `pętle`

### Treść

1. Wczytaj liczbę naturalną `n` (`n > 0`).
2. Wypisz liczbę π dokładnie `n` razy.
3. Każda wypisana wartość ma mieć **dokładnie `n` miejsc po przecinku**.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n > 0`)

### Wyjście

`n` wierszy, w każdym liczba π z dokładnością do `n` miejsc po przecinku.

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
3.14
3.14
```

### Uwagi o formatowaniu

* Liczba miejsc po przecinku ma być **dokładnie** równa `n` (np. dla `n=1`
wypisz `3.1`).
* Stosuj standardowe zaokrąglanie przy formatowaniu.

*/
#include <iomanip>
#include <iostream>
#include <numbers>

int main() {
  std::cout << "Podaj liczbe: " << std::endl;
  int n;
  std::cin >> n;

  std::cout << std::fixed << std::setprecision(n);

  for (int i = 0; i < n; i++) std::cout << std::numbers::pi << " ";

  return 0;
}

// g++-10 -Wall -Wextra -std=c++20 Zad3.cpp -o exe
