/*
ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie wielkie litery alfabetu łacińskiego (`A–Z`) na małe, używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)

### Wyjście

Jedna linia: napis po zamianie.

### Ograniczenia

* napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

### Uwagi

* Kody wielkiej i małej litery różnią się tylko bitem o wartości 32 (`0b100000`): `ord("A")` to `65`, a `ord("a")` to `97`. Ustawienie tego bitu: `ord(znak) | 32`.
* Zmieniaj tylko litery `A–Z` — np. `@` i `[` sąsiadują w tablicy ASCII z literami, ale mają pozostać bez zmian.
* Odwrotną zamianę (małe → wielkie) daje wyzerowanie tego bitu: `ord(znak) & ~32`.

ZAD-09B — Numer litery w alfabecie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `maski`

### Treść

Wczytaj słowo złożone z liter alfabetu łacińskiego. Dla każdej litery wyznacz jej numer w alfabecie — `a` i `A` mają numer `1`, `b` i `B` numer `2`, …, `z` i `Z` numer `26` — używając operacji bitowej na kodzie ASCII zamiast porównań i odejmowania.

### Wejście

* 1. linia: słowo

### Wyjście

Jedna linia: numery kolejnych liter słowa oddzielone pojedynczymi spacjami.

### Ograniczenia

* słowo ma od 1 do 100 znaków i składa się wyłącznie z liter `a–z` i `A–Z`

### Przykład

**Wejście:**

```
Bit
```

**Wyjście:**

```
2 9 20
```

### Uwagi

* Zapisz kody binarnie: `ord("A")` to $65 = 1000001_2$, a `ord("a")` to $97 = 1100001_2$. Pięć najniższych bitów kodu każdej litery to właśnie jej numer w alfabecie — i to niezależnie od wielkości litery.
* Pięć najniższych bitów wydobędziesz **maską** $31 = 11111_2$: `ord(znak) & 31`. Operacja `&` z maską zeruje wszystkie bity poza tymi, które w masce są jedynkami.

ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery alfabetu łacińskiego na przeciwną (mała ↔ wielka), używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)

### Wyjście

Jedna linia: napis po zmianie.

### Ograniczenia

* napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

### Uwagi

* Odwrócenie bitu o wartości 32: `ord(znak) ^ 32`. Stosuj je tylko do liter `a–z` i `A–Z`.

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

std::string numeryLiter(const std::string &slowo) {
  /*
   * Funkcja zwraca numery liter w alfabecie (1-26) oddzielone spacjami:
   * piec najnizszych bitow kodu ASCII litery to jej numer.
   */
  std::string wynik = "";

  for (std::size_t i = 0; i < slowo.size(); i++) {
    if (i > 0) wynik += ' ';
    wynik += std::to_string(slowo[i] & 0b11111);
  }

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

void testNumeryLiter() {
  assert(numeryLiter("Bit") == "2 9 20");
  assert(numeryLiter("zZaA") == "26 26 1 1");
}

void testOdwrocWielkoscLiter() {
  std::string slowo = "wszedl Kotek na PloteK i mrUga";
  std::string wynik = "WSZEDL kOTEK NA pLOTEk I MRuGA";

  assert(odwrocWielkoscLiter(slowo) == wynik);
}

int main() {
  testWielkieNaMale();
  testNumeryLiter();
  testOdwrocWielkoscLiter();

  return 0;
}
