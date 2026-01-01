/*
ZAD-02 — Wczytaj, zmodyfikuj i wypisz

**Poziom:** ★☆☆
**Tagi:** `listy`, `indeksy`, `modyfikacja`

### Treść

Wczytaj `N` oraz `N` liczb całkowitych do listy. Następnie:

a) Zwiększ każdy element o `1`.
b) Pomnóż każdy element przez jego indeks (indeksy od `0`).
c) Zastąp wszystkie elementy wartością pierwszego elementu.

Po każdym podpunkcie wypisz wynikową listę w **jednej** linii, elementy
oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Trzy linie:

1. wynik po (a)
2. wynik po (b)
3. wynik po (c)

Elementy w linii oddzielone przecinkami (bez spacji).

### Przykład

**Wejście:**

```
3
3
9
7
```

**Wyjście:**

```
4,10,8
0,9,14
3,3,3
```

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

void zwieksz(std::vector<int> &lista) {
  for (auto &liczba : lista) liczba += 1;
}

void pomnoz(std::vector<int> &lista) {
  for (unsigned int i = 0; i < lista.size(); i++) lista[i] *= i;
}

void zastap(std::vector<int> &lista) {
  if (lista.empty()) return;

  for (auto &liczba : lista) liczba = lista[0];
}

void wypisz(std::vector<int> &lista) {
  for (auto liczba : lista) std::cout << liczba << ", ";
  std::cout << std::endl;
}

int main() {
  std::vector<int> lista;
  int n;

  std::cout << "podaj liczbe n: ";
  std::cin >> n;
  wczytaj(lista, n);

  std::vector<int> kopia(lista);
  zwieksz(kopia);
  wypisz(kopia);

  kopia = lista;
  pomnoz(kopia);
  wypisz(kopia);

  kopia = lista;
  zastap(kopia);
  wypisz(kopia);

  return 0;
}
