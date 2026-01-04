/*
ZAD-03 — Trójkąt prostokątny (malejący)

**Poziom:** ★☆☆
**Tagi:** `pętle`, `print`, `string`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz odwrócony trójkąt o wysokości `n`, zaczynając od
`n` gwiazdek i kończąc na `1`.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii:

* 1. linia: `n` gwiazdek
* 2. linia: `n-1` gwiazdek
* …
* ostatnia linia: `*`

### Przykład

**Wejście:**

```
4
```

**Wyjście:**

```
****
***
**
*
```

*/
#include <iostream>

int main() {
  int n;
  std::cin >> n;

  for (int i = n; i >= 1; i--) {
    for (int j = 0; j < i; j++) {
      std::cout << "*";
    }
    std::cout << std::endl;
  }

  return 0;
}
