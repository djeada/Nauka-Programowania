/*
ZAD-08 — Usuń klucz

**Poziom:** ★☆☆
**Tagi:** `listy`, `remove`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych oraz `klucz`. Usuń **pierwsze** wystąpienie
`klucz` (jeśli istnieje). Następnie wypisz listę po modyfikacji w jednej linii,
elementy oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna linia: lista po usunięciu, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
4
```

**Wyjście:**

```
6,2,1,27
```

### Uwagi

* Jeśli `klucz` nie występuje, wypisz listę bez zmian.

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

  int klucz;
  std::cin >> klucz;

  std::vector<int> nowa;
  for (int i = 0; i < n; i++) {
    if (lista[i] != klucz) {
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
