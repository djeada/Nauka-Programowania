/*
ZAD-09 — N pierwszych liczb pierwszych

**Poziom:** ★★☆
**Tagi:** `pętle`, `pierwszość`, `wydajność`

### Treść

Wczytaj liczbę naturalną `N` (`N ≥ 1`) i wypisz pierwsze `N` liczb pierwszych w
**jednej linii**, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)

### Wyjście

Jedna linia: `N` liczb pierwszych oddzielonych spacjami.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
2 3 5 7 11
```

### Uwagi o formatowaniu

* Nie dodawaj spacji na końcu linii.
* Do sprawdzania pierwszości wystarczy test dzielnikami do `⌊sqrt(x)⌋`.

*/
#include <cmath>
#include <iostream>

bool czy_pierwsza(int num) {
  if (num <= 1) return false;
  if (num <= 3) return true;
  if (num % 2 == 0 || num % 3 == 0) return false;

  for (int i = 5; i * i <= num; i += 6) {
    if (num % i == 0 || num % (i + 2) == 0) return false;
  }

  return true;
}

int main() {
  int n;
  std::cin >> n;

  int count = 0;
  int num = 2;

  while (count < n) {
    if (czy_pierwsza(num)) {
      if (count > 0) std::cout << " ";
      std::cout << num;
      count++;
    }
    num++;
  }
  std::cout << std::endl;

  return 0;
}
