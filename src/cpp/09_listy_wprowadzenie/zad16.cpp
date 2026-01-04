/*
ZAD-16 — Indeksy pierwszej pary o sumie x

**Poziom:** ★★☆
**Tagi:** `hashmap`, `indeksy`, `2-sum`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `x`. Znajdź indeksy **pierwszej**
pary `(i, j)` (z `i < j`) takiej, że `lista[i] + lista[j] == x`.

Jeśli nie istnieje taka para — wypisz `-1 -1`.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Dwie liczby całkowite w jednej linii (oddzielone spacją): `i j` albo `-1 -1`.

### Przykład

**Wejście:**

```
5
1
3
4
5
2
5
```

**Wyjście:**

```
0 2
```

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

  int suma;
  std::cin >> suma;

  bool znaleziono = false;
  for (int i = 0; i < n && !znaleziono; i++) {
    for (int j = i + 1; j < n; j++) {
      if (lista[i] + lista[j] == suma) {
        std::cout << i << " " << j << std::endl;
        znaleziono = true;
        break;
      }
    }
  }

  if (!znaleziono) {
    std::cout << "-1 -1" << std::endl;
  }

  return 0;
}
