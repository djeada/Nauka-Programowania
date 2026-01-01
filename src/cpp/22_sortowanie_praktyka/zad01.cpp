/*
ZAD-01 — Sortowanie znaków w napisie

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`

### Treść

Otrzymujesz napis. Posortuj alfabetycznie wszystkie jego znaki i wypisz wynikowy
napis.

### Wejście

* 1 linia: napis `s`

### Wyjście

* 1 linia: napis `s` po posortowaniu znaków rosnąco (porównanie znaków jak w
Pythonie / Unicode)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
 Aaaaklmot
```

### Uwagi o formatowaniu

* Spacje też są znakami i biorą udział w sortowaniu (dlatego w przykładzie
wyjście zaczyna się od spacji).

*/

#include <algorithm>
#include <cassert>
#include <string>

void sortuj(std::string &napis) { std::sort(napis.begin(), napis.end()); }

void test1() {
  std::string napis = "bcda";
  std::string wynik = "abcd";

  sortuj(napis);

  assert(napis == wynik);
}

int main() {
  test1();

  return 0;
}
