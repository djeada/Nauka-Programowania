/*
ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`, `set`

### Treść

Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba
występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
6
3
2
1
3
2
2
```

**Wyjście:**

```
3,2,1
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

  std::vector<int> nowa;
  for (int i = 0; i < n; i++) {
    bool juz_jest = false;
    for (size_t j = 0; j < nowa.size(); j++) {
      if (nowa[j] == lista[i]) {
        juz_jest = true;
        break;
      }
    }
    if (!juz_jest) {
      nowa.push_back(lista[i]);
    }
  }

  for (size_t i = 0; i < nowa.size(); i++) {
    if (i > 0) std::cout << ",";
    std::cout << nowa[i];
  }
  std::cout << std::endl;

  return 0;
}
