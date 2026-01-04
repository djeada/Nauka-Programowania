/*
ZAD-13 — Brakujący element w ciągu arytmetycznym

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `ciąg arytmetyczny`, `listy`

### Treść

Wczytaj `N` liczb naturalnych. Lista jest fragmentem ciągu arytmetycznego z
**jednym brakującym elementem**. Znajdź i wypisz brakującą wartość.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — brakujący element.

### Przykład

**Wejście:**

```
4
5
2
1
3
```

**Wyjście:**

```
4
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

  std::sort(lista.begin(), lista.end());

  int minVal = lista[0];
  int maxVal = lista[n - 1];
  int sumaOczekiwana = (n + 1) * (minVal + maxVal) / 2;

  int sumaRzeczywista = 0;
  for (int i = 0; i < n; i++) {
    sumaRzeczywista += lista[i];
  }

  std::cout << (sumaOczekiwana - sumaRzeczywista) << std::endl;

  return 0;
}
