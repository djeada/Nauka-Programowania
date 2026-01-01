/*
ZAD-02A — Wypisz binarnie tylko gdy liczba parzysta

**Poziom:** ★☆☆
**Tagi:** `warunki`, `parzystość`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest parzysta — wypisz jej zapis
binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

* Jeśli `n % 2 == 0`: jedna linia z zapisem binarnym `n`
* W przeciwnym razie: brak wyjścia

### Przykład

**Wejście:**

```
7
```

**Wyjście:** *(brak)*

ZAD-02B — Wypisz binarnie tylko gdy liczba pierwsza

**Poziom:** ★☆☆
**Tagi:** `pierwszość`, `warunki`, `binarne`

### Treść

Wczytaj liczbę naturalną `n`. Jeśli `n` jest liczbą pierwszą — wypisz jej zapis
binarny. W przeciwnym razie nie wypisuj nic.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

* Jeśli `n` jest pierwsza: jedna linia z zapisem binarnym `n`
* W przeciwnym razie: brak wyjścia

### Przykład

**Wejście:**

```
7
```

**Wyjście:**

```
111
```

*/
#include <cassert>
#include <cmath>
#include <string>

std::string naBinarny(int liczba) {
  /*
   * Funkcja zamienia liczbe dziesietna na binarna.
   */
  std::string bin;

  while (liczba > 0) {
    bin.insert(0, std::to_string(liczba % 2));
    liczba /= 2;
  }

  return bin;
}

std::string zamienLiczbeParzysta(int liczba) {
  /*
   * Funkcja zamienia liczbe parzysta na liczbe binarna.
   */
  if (liczba % 2 == 0) return naBinarny(liczba);

  return "";
}

bool czyPierwsza(int n) {
  /*
   *  Funkcja sprawdza czy liczba jest pierwsza.
   */
  if (n <= 1) return false;

  if (n % 2 == 0 && n != 2) return false;

  for (int i = 3; i <= std::sqrt((double)n); i += 2) {
    if (n % i == 0) return false;
  }

  return true;
}

std::string zamienLiczbePierwsza(int liczba) {
  /*
   * Funkcja zamienia liczbe pierwsza na liczbe binarna.
   */
  if (czyPierwsza(liczba)) return naBinarny(liczba);

  return "";
}

void test1() {
  int liczba = 3;
  std::string wynik;

  assert(zamienLiczbeParzysta(liczba) == wynik);
}

void test2() {
  int liczba = 124;
  std::string wynik = "1111100";

  assert(zamienLiczbeParzysta(liczba) == wynik);
}

void test3() {
  int liczba = 124;
  std::string wynik;

  assert(zamienLiczbePierwsza(liczba) == wynik);
}

void test4() {
  int liczba = 3;
  std::string wynik = "11";

  assert(zamienLiczbePierwsza(liczba) == wynik);
}

int main() {
  test1();
  test2();
  test3();
  test4();

  return 0;
}
