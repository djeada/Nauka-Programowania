/*
ZAD-01 — Wczytaj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `I/O`, `odwracanie`

### Treść

Wczytaj `N`, następnie `N` liczb całkowitych do listy.

a) Wypisz elementy listy od początku do końca — każdy w osobnej linii.
b) Wypisz elementy listy od końca do początku — w **jednej** linii, oddzielone
przecinkami (bez spacji).

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

a) `N` linii — elementy w kolejności wczytania.
b) 1 linia — elementy w kolejności odwrotnej, oddzielone przecinkami.

### Przykład

**Wejście:**

```
3
8
12
7
```

**Wyjście:**

```
8
12
7
7,12,8
```

### Uwagi o formatowaniu

* W podpunkcie (b) nie dodawaj przecinka na końcu.

*/
#include <iostream>
#include <vector>

void wczytaj(std::vector<int> &lista, int n) {
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }
}

void wypiszOdPoczatku(std::vector<int> &lista) {
  for (auto liczba : lista) std::cout << liczba << std::endl;
}

void wypiszOdKonca(std::vector<int> &lista) {
  auto it = cend(lista);
  while (it != cbegin(lista)) std::cout << *(--it) << ", ";

  std::cout << std::endl;
}

int main() {
  std::vector<int> lista;
  int n;

  std::cout << "podaj liczbe n: " << std::endl;
  std::cin >> n;
  wczytaj(lista, n);

  std::cout << std::endl << "liczby w kolejnosci wczytania:" << std::endl;
  wypiszOdPoczatku(lista);

  std::cout << std::endl << "liczby wypisane od konca:" << std::endl;
  wypiszOdKonca(lista);

  return 0;
}
