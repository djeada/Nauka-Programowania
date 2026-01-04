/*
ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego
wystąpienia `klucz` w liście. Jeśli `klucz` nie występuje — wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna liczba całkowita — indeks (od `0`) lub `-1`.

### Przykład

**Wejście:**

```
5
2
9
-1
3
8
-1
```

**Wyjście:**

```
2
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

  int klucz;
  std::cin >> klucz;

  int wynik = -1;
  for (size_t i = 0; i < lista.size(); i++) {
    if (lista[i] == klucz) {
      wynik = i;
      break;
    }
  }

  std::cout << wynik << std::endl;

  return 0;
}
