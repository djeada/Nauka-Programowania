/*
ZAD-18 — Odwróć słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `split`, `string`, `pętle`

### Treść

Wczytaj zdanie i odwróć litery **w każdym słowie osobno**, zachowując kolejność
słów.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie z odwróconymi słowami

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
alA am atok
```

*/
#include <algorithm>
#include <cassert>
#include <string>
#include <vector>

// Zlozonosc Czasowa: O(n)
// Zlozonosc Pamieciowa: O(1)
void odwrocNapis(std::string &slowo, int pocz, int koniec) {
  int j = koniec;

  for (int i = pocz; i <= j; i++, j--) {
    char c = slowo[i];
    slowo[i] = slowo[j];
    slowo[j] = c;
  }
}

// Zlozonosc Czasowa: O(n^2)
// Zlozonosc Pamieciowa: O(1)
void odwrocNapisy(std::string &zdanie) {
  unsigned int N = zdanie.length();
  unsigned int pocz = 0;
  unsigned int koniec;

  for (unsigned int i = 0; i < N; i++) {
    if (zdanie[i] == ' ') {
      koniec = i - 1;
      odwrocNapis(zdanie, pocz, koniec);
      pocz = i + 1;
    }
  }

  // Odwroc ostatnie slowo
  if (pocz < N) {
    koniec = N - 1;
    odwrocNapis(zdanie, pocz, koniec);
  }
}

void test1() {
  std::string napis = "Cameron Diaz";
  std::string wynik = "noremaC zaiD";

  odwrocNapisy(napis);
  assert(napis == wynik);
}

int main() {
  test1();

  return 0;
}
