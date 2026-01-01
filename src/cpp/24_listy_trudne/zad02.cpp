/*
ZAD-02 — Przesuń zera na koniec listy

**Poziom:** ★★☆
**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy,
**zachowując kolejność** pozostałych elementów.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista po przekształceniu

### Przykład

**Wejście:**

```
[0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
```

**Wyjście:**

```
[1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
```

*/
#include <cassert>
#include <vector>

void zeraV1(std::vector<int> &lista) {
  auto N = lista.size();

  for (unsigned int i = 0; i < N; i++) {
    if (lista[i] == 0) {
      auto j = i + 1;

      while (lista[j] == 0 && j < N) j++;

      std::iter_swap(lista.begin() + i, lista.begin() + j);
    }
  }
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0};
  std::vector<int> wynik{1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0};

  zeraV1(lista);
  assert(lista == wynik);
}

void test2() {
  std::vector<int> lista{0, 0, 0, 0};
  std::vector<int> wynik{0, 0, 0, 0};

  zeraV1(lista);
  assert(lista == wynik);
}

void test3() {
  std::vector<int> lista{1, 2, 3, 4, 5, 6};
  std::vector<int> wynik{1, 2, 3, 4, 5, 6};

  zeraV1(lista);
  assert(lista == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
