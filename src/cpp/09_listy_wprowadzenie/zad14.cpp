/*
ZAD-14 — Element bez pary

**Poziom:** ★★☆
**Tagi:** `XOR`, `listy`, `zliczanie`

### Treść

Wczytaj listę liczb całkowitych o nieparzystej długości: wszystkie liczby poza
jedną występują dokładnie dwa razy. Znajdź liczbę bez pary.

### Wejście

* 1. linia: `N` (nieparzyste, `N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna liczba całkowita — element bez pary.

### Przykład

**Wejście:**

```
7
1
3
1
7
3
1
1
```

**Wyjście:**

```
7
```

*/
#include <iostream>
#include <unordered_map>
#include <vector>

int main() {
  int n;
  std::cin >> n;

  std::unordered_map<int, int> count;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    count[liczba]++;
  }

  for (auto& p : count) {
    if (p.second % 2 == 1) {
      std::cout << p.first << std::endl;
      break;
    }
  }

  return 0;
}
