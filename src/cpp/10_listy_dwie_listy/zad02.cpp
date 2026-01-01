/*
ZAD-02 — Połączenie dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `indeksy`, `concat`

### Treść

Wczytaj dwie listy liczb całkowitych i wykonaj niezależnie:

**a)** Połącz listy, doklejając drugą listę na koniec pierwszej.
**b)** W pierwszej liście **podmień** elementy o parzystych indeksach (0, 2, 4,
…) elementami z drugiej listy o tych samych indeksach — o ile taki indeks
istnieje w obu listach.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: wynik dla **a)** jako lista
* 2 linia: wynik dla **b)** jako lista

### Przykład

**Wejście:**

```
[1, 2, 3]
[4, 5, 6]
```

**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
```

*/
#include <cassert>
#include <vector>

std::vector<int> dostaw(std::vector<int> &listaA, std::vector<int> &listaB) {
  std::vector<int> wynik(listaA);

  for (auto liczba : listaB) wynik.push_back(liczba);

  return wynik;
}

std::vector<int> podmien(std::vector<int> &listaA, std::vector<int> &listaB) {
  std::vector<int> wynik(listaA);

  for (unsigned int i = 0; i < wynik.size(); i += 2) wynik[i] = listaB[i];

  return wynik;
}

void test1() {
  std::vector<int> listaA{-2, 8, 3, 6};
  std::vector<int> listaB{7, 5, 0};

  std::vector<int> wynik{-2, 8, 3, 6, 7, 5, 0};
  assert(dostaw(listaA, listaB) == wynik);
}

void test2() {
  std::vector<int> listaA{-2, 8, 3, 6};
  std::vector<int> listaB{7, 5, 0};

  std::vector<int> wynik{7, 8, 0, 6};
  assert(podmien(listaA, listaB) == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
