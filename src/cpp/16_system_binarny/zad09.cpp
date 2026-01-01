/*
ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis z liter alfabetu łacińskiego. Zamień wszystkie wielkie litery na
małe, używając operacji bitowych na kodach ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

ZAD-09B — Małe → wielkie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie małe litery na wielkie, używając operacji
bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
TEST
```

ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery na przeciwną (mała↔wielka) używając
operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po zmianie.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

*/
#include <cassert>
#include <string>

std::string wielkieNaMale(std::string slowo) {
  /*
   * Funkcja zamienia wielkie litery na male litery.
   */
  std::string wynik = "";

  for (const int &litera : slowo) wynik += (char)(litera | (int)' ');

  return wynik;
}

std::string maleNaWielkie(std::string slowo) {
  /*
   * Funkcja zamienia male litery na wielkie litery.
   */
  std::string wynik = "";

  for (const int &litera : slowo) wynik += (char)(litera & (int)'_');

  return wynik;
}

std::string odwrocWielkoscLiter(std::string slowo) {
  /*
   * Funkcja zamienia male litery na wielkie litery i wielkie litery na male
   * litery.
   */
  std::string wynik = "";

  for (const int &litera : slowo) {
    if (litera >= 'a' and litera <= 'z')
      wynik += (char)(litera ^ (int)' ');

    else if (litera >= 'A' and litera <= 'Z')
      wynik += (char)(litera ^ (int)' ');

    else
      wynik += (char)litera;
  }

  return wynik;
}

void testWielkieNaMale() {
  std::string slowo = "KURCZAKU";
  std::string wynik = "kurczaku";

  assert(wielkieNaMale(slowo) == wynik);
}

void testMaleNaWielkie() {
  std::string slowo = "piesek";
  std::string wynik = "PIESEK";

  assert(maleNaWielkie(slowo) == wynik);
}

void testOdwrocWielkoscLiter() {
  std::string slowo = "wszedl Kotek na PloteK i mrUga";
  std::string wynik = "WSZEDL kOTEK NA pLOTEk I MRuGA";

  assert(odwrocWielkoscLiter(slowo) == wynik);
}

int main() {
  testWielkieNaMale();
  testMaleNaWielkie();
  testOdwrocWielkoscLiter();

  return 0;
}
