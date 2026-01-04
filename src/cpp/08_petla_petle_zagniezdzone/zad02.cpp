/*
ZAD-02 — Trójkąt prostokątny (rosnący)

**Poziom:** ★☆☆
**Tagi:** `pętle`, `print`, `string`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt o wysokości `n`, gdzie w wierszu `i` jest
`i` gwiazdek (`i = 1..n`).

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii:

* 1. linia: `*`
* 2. linia: `**`
* …
* `n`-ta linia: `n` gwiazdek

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
*
**
***
```

*/
#include <iostream>

int main() {
  int n;
  std::cin >> n;

  for (int i = 1; i <= n; i++) {
    for (int j = 0; j < i; j++) {
      std::cout << "*";
    }
    std::cout << std::endl;
  }

  return 0;
}
