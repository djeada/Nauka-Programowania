/*
ZAD-07 — Średnia dwóch największych liczb

**Poziom:** ★☆☆
**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj `N` liczb naturalnych (`N ≥ 2`). Znajdź największą i drugą największą
wartość, a następnie wypisz ich średnią arytmetyczną jako liczbę
zmiennoprzecinkową z dokładnością do **jednego** miejsca po przecinku.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba zmiennoprzecinkowa w formacie `%.1f`.

### Przykład

**Wejście:**

```
6
9
2
3
2
1
7
```

**Wyjście:**

```
8.0
```

*/
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
  int n;
  std::cin >> n;

  std::vector<int> lista;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }

  std::sort(lista.begin(), lista.end(), std::greater<int>());

  double srednia = (lista[0] + lista[1]) / 2.0;

  std::cout << srednia << std::endl;

  return 0;
}
