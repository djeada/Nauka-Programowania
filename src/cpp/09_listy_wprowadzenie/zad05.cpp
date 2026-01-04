/*
ZAD-05 — Zmodyfikuj elementy spełniające warunek

**Poziom:** ★☆☆
**Tagi:** `listy`, `warunki`, `liczby pierwsze`

### Treść

Wczytaj listę liczb całkowitych. Dla każdego podpunktu utwórz **nową listę** na
podstawie listy z poprzedniego podpunktu i wypisz ją w jednej linii (przecinki
bez spacji):

a) Zwiększ o 1 elementy o **parzystych indeksach** (0,2,4,...).
b) Ustaw na `0` elementy będące **wielokrotnością 3**.
c) Podnieś do kwadratu elementy **mniejsze niż 10**.
d) Oblicz sumę wszystkich elementów listy i wstaw tę sumę na indeksy, które są
**liczbami pierwszymi** (2,3,5,7,11,...) — tylko te, które mieszczą się w
zakresie listy. e) Zamień każdy element na **iloczyn wszystkich pozostałych
elementów** listy.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Pięć linii (po kolei: a, b, c, d, e), w każdej lista oddzielona przecinkami.

### Przykład

**Wejście:**

```
5
5
7
9
4
2
```

**Wyjście:**

```
6,7,10,4,3
6,7,0,4,3
36,49,0,16,9
36,49,36,36,9
0,0,0,0,0
```

### Uwagi o formatowaniu

* W podpunkcie (d) indeks 0 i 1 nie są pierwsze.
* W podpunkcie (e) jeśli w liście jest `0`, to wiele wyników będzie `0` — to
normalne.
* Nie dodawaj przecinków na końcu linii.

*/
#include <cmath>
#include <iostream>
#include <vector>

void wypisz(const std::vector<int>& lista) {
  for (size_t i = 0; i < lista.size(); i++) {
    if (i > 0) std::cout << ",";
    std::cout << lista[i];
  }
  std::cout << std::endl;
}

bool czy_pierwsza(int n) {
  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 == 0 || n % 3 == 0) return false;
  for (int i = 5; i * i <= n; i += 6) {
    if (n % i == 0 || n % (i + 2) == 0) return false;
  }
  return true;
}

int main() {
  int n;
  std::cin >> n;

  std::vector<int> lista;
  for (int i = 0; i < n; i++) {
    int liczba;
    std::cin >> liczba;
    lista.push_back(liczba);
  }

  // a) Zwiększ o 1 elementy o parzystych indeksach
  for (int i = 0; i < n; i++) {
    if (i % 2 == 0) lista[i]++;
  }
  wypisz(lista);

  // b) Ustaw na 0 elementy będące wielokrotnością 3
  for (int i = 0; i < n; i++) {
    if (lista[i] % 3 == 0) lista[i] = 0;
  }
  wypisz(lista);

  // c) Podnieś do kwadratu elementy mniejsze niż 10
  for (int i = 0; i < n; i++) {
    if (lista[i] < 10) lista[i] = lista[i] * lista[i];
  }
  wypisz(lista);

  // d) Suma na indeksach pierwszych
  int suma = 0;
  for (int i = 0; i < n; i++) {
    suma += lista[i];
  }
  for (int i = 0; i < n; i++) {
    if (czy_pierwsza(i)) lista[i] = suma;
  }
  wypisz(lista);

  // e) Każdy element na iloczyn wszystkich pozostałych
  std::vector<int> nowa(n);
  for (int i = 0; i < n; i++) {
    int iloczyn = 1;
    for (int j = 0; j < n; j++) {
      if (i != j) iloczyn *= lista[j];
    }
    nowa[i] = iloczyn;
  }
  wypisz(nowa);

  return 0;
}
