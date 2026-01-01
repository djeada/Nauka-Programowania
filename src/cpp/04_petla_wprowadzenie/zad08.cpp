/*
ZAD-08 — Obliczanie liczby kur i owiec na farmie

**Poziom:** ★★☆
**Tagi:** `układ równań`, `arytmetyka`

### Treść

Na farmie są kury i owce. Wiadomo, że:

* łączna liczba głów wynosi `a`,
* łączna liczba nóg wynosi `b`,
* kura ma 2 nogi, owca ma 4 nogi,
* każda ma dokładnie 1 głowę.

Oblicz liczbę kur oraz liczbę owiec.

### Wejście

Dwie liczby naturalne:

* 1. linia: `a` — liczba głów (`a ≥ 0`)
* 2. linia: `b` — liczba nóg (`b ≥ 0`)

### Ograniczenia / gwarancje

* Istnieje rozwiązanie w liczbach całkowitych nieujemnych.

### Wyjście

Dwie liczby naturalne, każda w oddzielnej linii:

1. liczba kur
2. liczba owiec

### Przykład

**Wejście:**

```
40
100
```

**Wyjście:**

```
30
10
```

### Uwagi o formatowaniu

* Nie wypisuj dodatkowych opisów — tylko liczby.

*/
#include <iostream>

int main() {
  int glowy, nogi;
  std::cin >> glowy >> nogi;

  // kury mają 2 nogi, owce mają 4 nogi
  // k + o = glowy
  // 2k + 4o = nogi
  // k = glowy - o
  // 2(glowy - o) + 4o = nogi
  // 2*glowy - 2o + 4o = nogi
  // 2o = nogi - 2*glowy
  // o = (nogi - 2*glowy) / 2
  
  int owce = (nogi - 2 * glowy) / 2;
  int kury = glowy - owce;

  std::cout << kury << std::endl;
  std::cout << owce << std::endl;

  return 0;
}
