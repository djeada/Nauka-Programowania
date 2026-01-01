/*
ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`, `set`

### Treść

Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba
występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
6
3
2
1
3
2
2
```

**Wyjście:**

```
3,2,1
```

*/
#include <algorithm>
#include <cassert>
#include <unordered_set>
#include <vector>

// Zlozonosc czasowa O(nlogn)
void usunDuplikatyV1(std::vector<int> &lista) {
  sort(lista.begin(), lista.end());
  lista.erase(unique(lista.begin(), lista.end()), lista.end());
}

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
void usunDuplikatyV2(std::vector<int> &lista) {
  std::unordered_set<int> zbior;
  for (auto liczba : lista) zbior.insert(liczba);

  lista.assign(zbior.begin(), zbior.end());
}

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
void usunDuplikatyV3(std::vector<int> &lista) {
  std::vector<int> pom;

  auto i = lista.begin();
  while (i != lista.end()) {
    if (find(pom.begin(), pom.end(), *i) != pom.end())
      i = lista.erase(i);
    else {
      pom.push_back(*i);
      ++i;
    }
  }
}

bool wektoryRowne(std::vector<int> &v1, std::vector<int> &v2) {
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());
  return v1 == v2;
}

void test1() {
  std::vector<int> lista{3, 5, 3, 3, 2};
  std::vector<int> wynik{3, 5, 2};

  usunDuplikatyV1(lista);
  assert(wektoryRowne(lista, wynik));
}

void test2() {
  std::vector<int> lista{3, 5, 3, 3, 2};
  std::vector<int> wynik{3, 5, 2};

  usunDuplikatyV2(lista);
  assert(wektoryRowne(lista, wynik));
}

void test3() {
  std::vector<int> lista{3, 5, 3, 3, 2};
  std::vector<int> wynik{3, 5, 2};

  usunDuplikatyV3(lista);
  assert(wektoryRowne(lista, wynik));
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
