/*
ZAD-02 — Słownik z dwóch list (klucze i wartości)

**Poziom:** ★☆☆
**Tagi:** `dict`, `listy`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z
pierwszej listy → wartość z drugiej listy. Jeśli długości są różne, wypisz pusty
słownik `{}`.

### Wejście

* 1 linia: `n`
* 2 linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Słownik albo `{}`

### Przykład

**Wejście:**

```
3
3
3 5 8
1 2 -1
```

**Wyjście:**

```
{3: 1, 5: 2, 8: -1}
```

*/
#include <cassert>
#include <unordered_map>
#include <vector>

std::unordered_map<int, int> budujSlownik(std::vector<int> &listaA,
                                          std::vector<int> &listaB) {
  /*
   * Funkcja tworzy slownik zawierajacy klucze bedace elementami
   * pierwszej listy i wartosci bedace elementami drugiej listy.
   */
  std::unordered_map<int, int> slownik;

  if (listaA.size() != listaB.size()) return slownik;

  for (unsigned int i = 0; i < listaA.size(); i++)
    slownik[listaA[i]] = listaB[i];

  return slownik;
}

void test1() {
  std::vector<int> listaA{3, 5, 8};
  std::vector<int> listaB{1, 2, -1};
  std::unordered_map<int, int> wynik{{3, 1}, {5, 2}, {8, -1}};

  assert(budujSlownik(listaA, listaB) == wynik);
}

void test2() {
  std::vector<int> listaA{0, 1};
  std::vector<int> listaB{1, 0};
  std::unordered_map<int, int> wynik{{0, 1}, {1, 0}};

  assert(budujSlownik(listaA, listaB) == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
