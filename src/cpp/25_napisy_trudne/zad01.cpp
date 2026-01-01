/*
ZAD-01 — Podmiana słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Masz trzy napisy:

1. Zdanie (tekst do modyfikacji),
2. Słowo A (podnapis do znalezienia),
3. Słowo B (podnapis zastępujący).

Zamień **wszystkie wystąpienia** słowa/podnapisu **A** na **B** w podanym
zdaniu.

> Uwaga: A może być częścią innych słów — zamiana dotyczy **każdego wystąpienia
podnapisu**.

### Wejście

* 1 linia: zdanie `S`
* 2 linia: napis `A`
* 3 linia: napis `B`

### Wyjście

* 1 linia: zdanie po zamianie

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
rzy
```

**Wyjście:**

```
Lerzy jerzy na wierzy
```

*/
#include <cassert>
#include <string>

std::string zamienWszystkoV1(std::string zdanie, std::string napisA,
                             std::string napisB) {
  auto k = zdanie.find(napisA);

  while (k != std::string::npos) {
    zdanie.replace(k, napisA.size(), napisB);
    k = zdanie.find(napisA, k + napisB.size());
  }

  return zdanie;
}

// Testy Poprawnosci
void test1() {
  std::string zdanie = "Lezy jezy na wiezy";
  std::string napisA = "zy";
  std::string napisB = "rzy";
  std::string wynik = "Lerzy jerzy na wierzy";

  assert(zamienWszystkoV1(zdanie, napisA, napisB) == wynik);
}

int main() {
  test1();

  return 0;
}

// Compiled with g++ -std=c++17 Zad1.cpp -lstdc++fs -o exe
