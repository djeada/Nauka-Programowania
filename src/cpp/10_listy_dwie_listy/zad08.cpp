/*
ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów

**Poziom:** ★★☆
**Tagi:** `list`, `merge`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych, każda **posortowana rosnąco**. Połącz je w
jedną listę:

* wynik ma być posortowany rosnąco,
* wynik ma zawierać **unikalne** elementy (bez duplikatów).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
[2, 3, 4, 5, 7, 9]
```

*/
#include <algorithm>
#include <cassert>
#include <vector>

// Zlozonosc obliczeniowa O(n)
// Zlozonosc pamieciowa O(n)
std::vector<int> polaczV1(std::vector<int> &listaA, std::vector<int> &listaB) {
  if (listaA.empty()) return listaB;

  if (listaB.empty()) return listaA;

  std::vector<int> wynik;

  unsigned int i = 0;
  unsigned int j = 0;

  while (i < listaA.size() && j < listaB.size()) {
    if (listaA[i] < listaB[j]) {
      wynik.push_back(listaA[i]);
      i++;
    } else {
      wynik.push_back(listaB[j]);
      j++;
    }
  }

  for (unsigned int k = i; k < listaA.size(); k++) wynik.push_back(listaA[k]);

  for (unsigned int k = j; k < listaB.size(); k++) wynik.push_back(listaB[k]);

  return wynik;
}

void test1() {
  std::vector<int> listaA{5, 7, 11};
  std::vector<int> listaB{1, 3, 8, 14};

  std::vector<int> wynik{1, 3, 5, 7, 8, 11, 14};
  assert(polaczV1(listaA, listaB) == wynik);
}

int main() {
  test1();

  return 0;
}
