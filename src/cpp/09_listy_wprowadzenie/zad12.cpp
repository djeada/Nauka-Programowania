/*
ZAD-12 — Rotacja w lewo / prawo

**Poziom:** ★★☆
**Tagi:** `listy`, `rotacja`, `modulo`

### Treść

Wczytaj listę liczb całkowitych, a następnie:

* `kierunek = 0` → rotacja w lewo,
* `kierunek = 1` → rotacja w prawo,

o `K` pozycji (gdzie `K ≥ 0`). Wypisz listę po rotacji, przecinkami bez spacji.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* kolejna linia: `kierunek` (0 lub 1)
* ostatnia linia: `K` (`K ≥ 0`)

### Wyjście

Jedna linia: lista po rotacji, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
7
5
27
6
2
1
10
8
0
2
```

**Wyjście:**

```
6,2,1,10,8,5,27
```

### Uwagi

* Zredukuj `K` przez `K % N`.

*/
#include <cassert>
#include <string>
#include <vector>

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(n)
void rotacja(std::vector<int> &lista, const std::string &kierunek, int liczba) {
  if (kierunek == "prawo") {
    for (int i = 0; i < liczba; i++) {
      lista.insert(lista.begin(), lista.back());
      lista.erase(std::prev(lista.end()));
    }
  }

  else {
    for (int i = 0; i < liczba; i++) {
      lista.push_back(lista.front());
      lista.erase(lista.begin());
    }
  }
}

void test1() {
  std::vector<int> lista{5, 27, 6, 2, 1, 10, 8};
  std::vector<int> wynik{6, 2, 1, 10, 8, 5, 27};
  std::string kierunek = "lewo";
  int liczba = 2;

  rotacja(lista, kierunek, liczba);
  assert(lista == wynik);
}

void test2() {
  std::vector<int> lista{9, 9, 42, 47, 5, 6, 19, 7};
  std::vector<int> wynik{6, 19, 7, 9, 9, 42, 47, 5};
  std::string kierunek = "prawo";
  int liczba = 3;

  rotacja(lista, kierunek, liczba);
  assert(lista == wynik);
}

int main() {
  test1();
  test2();

  return 0;
}
