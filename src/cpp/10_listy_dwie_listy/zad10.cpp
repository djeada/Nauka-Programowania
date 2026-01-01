/*
ZAD-10 — Mediana dwóch posortowanych list

**Poziom:** ★★☆
**Tagi:** `list`, `median`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych:

* obie są posortowane rosnąco,
* obie mają tę samą, niezerową długość.

Znajdź medianę zbioru wszystkich elementów z obu list (czyli medianę po
„złączeniu” obu list).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: mediana jako liczba zmiennoprzecinkowa
  (jeśli mediana jest całkowita, wypisz ją z `.0`, np. `4.0`)

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
4.5
```

*/
#include <algorithm>
#include <cassert>
#include <vector>

// Zlozonosc obliczeniowa O(m + n)
// Zlozonosc pamieciowa O(1)
double mediana(std::vector<int> &listaA, std::vector<int> &listaB) {
  unsigned int i = 0;
  unsigned int j = 0;
  unsigned int n = listaA.size();
  unsigned int m = listaB.size();
  double m1 = -1, m2 = -1;

  for (unsigned int licznik = 0; licznik <= (n + m) / 2; licznik++) {
    if ((m + n) % 2 == 0) m2 = m1;

    if (i != n && j != m)
      m1 = (listaA[i] > listaB[j]) ? listaB[j++] : listaA[i++];

    else if (i < n)
      m1 = listaA[i++];

    else
      m1 = listaB[j++];
  }

  if ((m + n) % 2 == 1) return m1;

  return (m1 + m2) / 2.00;
}

void test1() {
  std::vector<int> listaA({2, 4, 7});
  std::vector<int> listaB({3, 5, 9});

  double wynik = 4.5;
  assert(mediana(listaA, listaB) == wynik);
}

int main() {
  test1();

  return 0;
}
