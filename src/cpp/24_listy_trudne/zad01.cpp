/*
ZAD-01 — Najdłuższy ciąg jedynek

**Poziom:** ★★☆
**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Znajdź **indeks zera**,
które po zamianie na `1` da **najdłuższy ciąg kolejnych jedynek**.

Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz
`-1`.

### Wejście

* 1 linia: lista `A` (tylko `0` i `1`)

### Wyjście

* 1 linia: indeks (liczba całkowita) albo `-1`

### Przykład

**Wejście:**

```
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
```

**Wyjście:**

```
7
```

### Uwagi

* Jeśli kilka zer daje ten sam maksymalny wynik — wybierz to o **najmniejszym
indeksie** (jeśli nie określono inaczej w testach).

*/
#include <cassert>
#include <vector>

// Zlozonosc czasowa O(n)
// Zlozonosc pamieciowa O(1)
int znajdzZeroDoPodmianyV1(std::vector<int> &lista) {
  auto licznikJedynek = 0;
  auto licznikZer = 0;

  auto indeksZera = -1;
  auto poprzedniIndeksZera = -1;

  for (unsigned int i = 0; i < lista.size(); i++) {
    if (lista[i] == 1)
      licznikZer++;

    else {
      licznikZer = i - poprzedniIndeksZera;
      poprzedniIndeksZera = i;
    }

    if (licznikZer > licznikJedynek) {
      licznikJedynek = licznikZer;
      indeksZera = poprzedniIndeksZera;
    }
  }

  return indeksZera;
}

// Testy Poprawnosci
void test1() {
  std::vector<int> lista{0, 0, 1, 0, 1, 1, 1, 0, 1, 1};
  int wynik = 7;

  assert(znajdzZeroDoPodmianyV1(lista) == wynik);
}

void test2() {
  std::vector<int> lista{1, 1, 1, 1, 1, 1, 1, 1};
  int wynik = -1;

  assert(znajdzZeroDoPodmianyV1(lista) == wynik);
}

void test3() {
  std::vector<int> lista{1, 0, 1, 1, 1, 1, 1, 1};
  int wynik = 1;

  assert(znajdzZeroDoPodmianyV1(lista) == wynik);
}

int main() {
  test1();
  test2();
  test3();

  return 0;
}
