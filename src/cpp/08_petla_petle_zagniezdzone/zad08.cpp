/*
ZAD-08 — Trójkąt Pascala

**Poziom:** ★★☆
**Tagi:** `pętle zagnieżdżone`, `listy`, `kombinatoryka`

### Treść

Wczytaj `n` (`n ≥ 1`) i wypisz trójkąt Pascala o wysokości `n`.

Wiersz 1: `1`
Wiersz 2: `1 1`
Wiersz 3: `1 2 1`
itd.

Liczby w wierszu oddzielaj pojedynczą spacją.

### Wejście

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

`n` linii, w `i`-tej linii jest `i` liczb.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
1
1 1
1 2 1
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu wiersza.

*/
#include <iostream>

int main() {
  int n;
  std::cin >> n;

  for (int i = 0; i < n; i++) {
    int c = 1;
    for (int j = 0; j <= i; j++) {
      if (j > 0) std::cout << " ";
      std::cout << c;
      c = c * (i - j) / (j + 1);
    }
    std::cout << std::endl;
  }

  return 0;
}
