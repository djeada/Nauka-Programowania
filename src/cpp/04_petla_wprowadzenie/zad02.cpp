/*
ZAD-02 — Wypisywanie liczb mniejszych od podanej

**Poziom:** ★☆☆
**Tagi:** `for`, `while`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n > 0`) i wypisz wszystkie liczby naturalne
mniejsze od `n`, zaczynając od `n - 1` i kończąc na `1`.

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n > 0`)

### Wyjście

Kolejne liczby naturalne mniejsze od `n`, każda w nowej linii, w kolejności
malejącej.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
1
```

### Uwagi o formatowaniu

* Jeśli `n = 1`, nie wypisuj nic.

*/
#include <iostream>

int main() {
  std::cout << "Podaj liczbe" << std::endl;
  int a;
  std::cin >> a;

  for (int i = 1; i < a; i++) std::cout << i << " ";

  std::cout << std::endl;

  return 0;
}
