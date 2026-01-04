/*
ZAD-12 — Rotacja w lewo / prawo

**Poziom:** ★★☆
**Tagi:** `listy`, `rotacja`, `modulo`

### Treść

Wczytaj listę liczb całkowitych, a następnie:

* `kierunek = 0` → rotacja w lewo,
* `kierunek = 1` → rotacja w prawo,

o `K` pozycji (gdzie `K ≥ 0`). Wypisz listę po rotacji, przecinkami bez spacji.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* kolejna linia: `kierunek` (0 lub 1)
* ostatnia linia: `K` (`K ≥ 0`)

### Wyjście

Jedna linia: lista po rotacji, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
7
5
27
6
2
1
10
8
0
2
```

**Wyjście:**

```
6,2,1,10,8,5,27
```

### Uwagi

* Zredukuj `K` przez `K % N`.

*/
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

  int k;
  std::cin >> k;

  k = k % n;  // Obsługa k większego niż n

  std::vector<int> nowa(n);
  for (int i = 0; i < n; i++) {
    nowa[(i + k) % n] = lista[i];
  }

  for (int i = 0; i < n; i++) {
    if (i > 0) std::cout << ",";
    std::cout << nowa[i];
  }
  std::cout << std::endl;

  return 0;
}
