/*
ZAD-04 — Wspólny podciąg o największej długości (równe sumy)

**Poziom:** ★★★
**Tagi:** `list`, `prefix`, `hashmap`, `podciąg`

### Treść

Otrzymujesz dwie listy binarne `A` i `B` (zera i jedynki) o tej samej długości.
Znajdź **maksymalną długość** podciągu (ciągłych elementów), dla którego suma
elementów w podciągu z `A` jest równa sumie elementów w odpowiadającym podciągu
z `B` (ten sam zakres indeksów).

### Wejście

* 1 linia: lista binarna `A`
* 2 linia: lista binarna `B` (tej samej długości)

### Wyjście

* 1 linia: maksymalna długość (liczba naturalna)

### Przykład

**Wejście:**

```
[0, 0, 1, 1, 1, 1]
[0, 1, 1, 0, 1, 0]
```

**Wyjście:**

```
5
```

*/
#include <cassert>
#include <unordered_map>
#include <vector>

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
int znajdzPodciagV1(std::vector<int> &listaA, std::vector<int> &listaB) {
  if (listaA.size() != listaB.size())
    throw std::invalid_argument("Listy musza byc rownej dlugosci.");

  std::unordered_map<int, int> slownik{{0, -1}};

  int wynik = 0;
  int sumaA = 0;
  int sumaB = 0;

  for (auto i = 0; i <= listaA.size(); i++) {
    sumaA += listaA[i];
    sumaB += listaB[i];

    auto roznica = sumaA - sumaB;

    if (!slownik.count(roznica))
      slownik[roznica] = i;

    else
      wynik = std::max(wynik, i - slownik[roznica]);
  }

  return wynik;
}

// Testy Poprawnosc
void test1() {
  std::vector<int> listaA{0, 0, 1, 1, 1, 1};
  std::vector<int> listaB{0, 1, 1, 0, 1, 0};
  int wynik = 5;

  assert(znajdzPodciagV1(listaA, listaB) == wynik);
}

void test2() {
  std::vector<int> listaA{0, 0, 1, 1};
  std::vector<int> listaB{0, 1, 1, 0, 1, 0};
  try {
    znajdzPodciagV1(listaA, listaB);
    assert(false);
  } catch (...) {
    assert(true);
  }
}

int main() {
  test1();
  test2();

  return 0;
}
