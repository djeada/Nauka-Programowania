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
#include <cassert>
#include <cmath>
#include <numeric>
#include <vector>

void zwieksz(std::vector<int> &lista) {
  for (unsigned int i = 0; i < lista.size(); i++) {
    if (i % 2 == 0) lista[i]++;
  }
}

void wyzeruj(std::vector<int> &lista) {
  for (auto &liczba : lista) {
    if (liczba % 3 == 0) liczba = 0;
  }
}

void kwadrat(std::vector<int> &lista) {
  for (auto &liczba : lista) {
    if (liczba < 10) liczba = pow(liczba, 2);
  }
}

int czyPierwsza(int n) {
  if ((!(n % 2) && n != 2) || n < 1) return false;

  for (int i = 3; i <= std::sqrt((double)n); i += 2) {
    if (!(n % i)) return false;
  }

  return true;
}

void suma(std::vector<int> &lista) {
  int suma = accumulate(lista.begin(), lista.end(), 0);

  for (unsigned int i = 0; i < lista.size(); i++) {
    if (czyPierwsza(i)) lista[i] = suma;
  }
}

void zamien(std::vector<int> &lista) {
  std::vector<int> iloczyny;

  for (unsigned int i = 0; i < lista.size(); i++) {
    int iloczyn = 1;

    for (unsigned int j = 0; j < lista.size(); j++) {
      if (j == i) continue;

      iloczyn *= lista[j];
    }

    iloczyny.push_back(iloczyn);
  }

  lista = iloczyny;
}

void test1() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  std::vector<int> wynik{4, 5, -6, 4, 10, -11, 3};
  zwieksz(lista);
  assert(lista == wynik);
}

void test2() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  std::vector<int> wynik{0, 5, -7, 4, 0, -11, 2};
  wyzeruj(lista);
  assert(lista == wynik);
}

void test3() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  std::vector<int> wynik{9, 25, 49, 16, 81, 121, 4};
  kwadrat(lista);
  assert(lista == wynik);
}

void test4() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  std::vector<int> wynik{3, 5, 5, 5, 9, 5, 2};
  suma(lista);
  assert(lista == wynik);
}

void test5() {
  std::vector<int> lista{3, 5, -7, 4, 9, -11, 2};
  std::vector<int> wynik{27720, 16632, -11880, 20790, 9240, -7560, 41580};
  zamien(lista);
  assert(lista == wynik);
}

int main() {
  test1();
  test2();
  test3();
  test4();
  test5();

  return 0;
}
