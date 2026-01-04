/*
ZAD-15 — Element dominujący

**Poziom:** ★★☆
**Tagi:** `zliczanie`, `dict`, `majority`

### Treść

Wczytaj listę liczb naturalnych. Jeśli istnieje liczba, która występuje **więcej
niż N/2 razy**, wypisz ją. W przeciwnym razie wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — element dominujący lub `-1`.

### Przykład

**Wejście:**

```
5
4
7
4
4
2
```

**Wyjście:**

```
4
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
    if (p.second > n / 2) {
      std::cout << p.first << std::endl;
      break;
    }
  }

  return 0;
}
