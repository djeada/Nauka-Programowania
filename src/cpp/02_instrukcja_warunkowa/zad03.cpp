/*
ZAD-03 — Określanie znaku liczby

**Poziom:** ★☆☆
**Tagi:** `if-elif-else`, `porównania`, `string`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jeden z komunikatów:

* dla `x < 0`: `Liczba jest ujemna.`
* dla `x > 0`: `Liczba jest dodatnia.`
* dla `x = 0`: `Liczba jest zerem.`

### Wejście

* 1 linia: `x` (liczba całkowita)

### Wyjście

Jedna linia — dokładnie jeden komunikat.

### Przykłady

**Wejście:**

```
-5
```

**Wyjście:**

```
Liczba jest ujemna.
```

**Wejście:**

```
0
```

**Wyjście:**

```
Liczba jest zerem.
```

**Wejście:**

```
2
```

**Wyjście:**

```
Liczba jest dodatnia.
```

*/
#include <iostream>

int main() {
  std::cout << "podaj liczbe:" << std::endl;

  int a;
  std::cin >> a;

  if (a < 0)
    std::cout << "libczba jest ujemna" << std::endl;
  else if (a > 0)
    std::cout << "liczba jest dodatnia" << std::endl;
  else
    std::cout << "liczba jest zerem" << std::endl;

  return 0;
}
