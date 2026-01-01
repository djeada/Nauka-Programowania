/*
ZAD-09 — Usuń z pierwszej listy część wspólną obu list

**Poziom:** ★★☆
**Tagi:** `list`, `filter`

### Treść

Wczytaj dwie listy liczb całkowitych. Usuń z pierwszej listy wszystkie elementy,
które występują również w drugiej liście.

* Zachowaj kolejność pozostałych elementów z pierwszej listy.
* Jeśli wszystko zostanie usunięte — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista 1 po usunięciu elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[9, 5]
```

*/
#include <algorithm>
#include <cassert>
#include <vector>

// Zlozonosc obliczeniowa O(n^2)
// Zlozonosc pamieciowa O(n)
void usunCzescWspolnaV1(std::vector<int> &listaA, std::vector<int> &listaB) {
  auto it = listaA.begin();

  while (it != listaA.end()) {
    if (find(listaB.begin(), listaB.end(), *it) != listaB.end())
      it = listaA.erase(it);
    else
      it++;
  }
}

void test1() {
  std::vector<int> listaA{3, 6, 2, 7, 9};
  std::vector<int> listaB{4, 2, 3, 5, 6};
  std::vector<int> wynik{7, 9};

  usunCzescWspolnaV1(listaA, listaB);

  assert(listaA == wynik);
}

int main() {
  test1();

  return 0;
}
