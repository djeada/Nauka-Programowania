/*
ZAD-04 — Maksimum i minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `min`, `if`, `formatowanie`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Wypisz je w jednej linii w kolejności: **większa, potem mniejsza**, oddzielone
pojedynczą spacją. Jeśli `a = b`, wypisz `a b` (czyli dwie takie same liczby).

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia:
`max(a, b) min(a, b)`

### Przykłady

**Wejście:**

```
1
4
```

**Wyjście:**

```
4 1
```

**Wejście:**

```
5
5
```

**Wyjście:**

```
5 5
```

*/
#include <iostream>

int main() {
  std::cout << "podaj dwie liczby:" << std::endl;

  int a;
  int b;

  std::cin >> a;
  std::cin >> b;

  if (a > b) {
    std::cout << a << std::endl;
    std::cout << b << std::endl;
    std::cout << "pierwsza liczba jest wieksza od drugiej" << std::endl;

  }

  else {
    std::cout << b << std::endl;
    std::cout << a << std::endl;
    std::cout << "pierwsza liczba nie jest wieksza od drugiej" << std::endl;
  }

  return 0;
}
