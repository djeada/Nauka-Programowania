/*
ZAD-05 — Co k-ty znak poziomo i pionowo

**Poziom:** ★☆☆
**Tagi:** `string`, `slicing`, `pętle`

### Treść

Wczytaj napis i liczbę `k`.

a) Wypisz co `k`-ty znak w jednym wierszu, oddzielając znaki spacjami.
b) Wypisz co `k`-ty znak pionowo (każdy w osobnej linii).

### Wejście

* 1. linia: napis
* 2. linia: liczba naturalna `k` (k ≥ 1)

### Wyjście

* (a) 1 linia: znaki oddzielone spacjami
* (b) wiele linii: każdy znak osobno

### Przykład

**Wejście:**

```
Grzechotnik
3
```

**Wyjście:**

```
z h n
z
h
n
```

### Uwagi o formatowaniu

* Dokładnie jedna spacja między znakami w punkcie (a), bez spacji na końcu
linii.

*/
#include <iostream>

void wypiszPoziomo(const std::string &napis, int k) {
  for (unsigned int i = 0; i < napis.size(); i += k)
    std::cout << napis[i] << ", ";

  std::cout << std::endl;
}

void wypiszPionowo(const std::string &napis, int k) {
  for (unsigned int i = 0; i < napis.size(); i += k)
    std::cout << napis[i] << std::endl;
}

int main() {
  std::string napis = "hej dzieci jesli chcecie zobaczyc smerfow las";
  int k = 3;
  wypiszPoziomo(napis, k);
  wypiszPionowo(napis, k);

  return 0;
}
