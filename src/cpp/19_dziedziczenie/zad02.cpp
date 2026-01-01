/*
ZAD-02 — Klasa Kształt oraz klasy Koło i Kwadrat

**Poziom:** ★★☆
**Tagi:** `dziedziczenie`, `polimorfizm`, `math`

### Treść

Zaprojektuj hierarchię klas:

* **Kształt** — klasa bazowa (ogólna) dla kształtów.
* **Koło** — dziedziczy po `Kształt`.
* **Kwadrat** — dziedziczy po `Kształt`.

Każda klasa ma mieć:

* metodę obliczającą **pole**,
* metodę wypisującą informacje o obiekcie: typ, parametry i pole.

Program:

* wczytuje promień `r` koła oraz bok `a` kwadratu,
* tworzy obiekty `Koło(r)` i `Kwadrat(a)`,
* wypisuje informacje o obu.

**Uwaga do formatowania:**
*Pole koła wypisz do 4 miejsc po przecinku.*
*Pole kwadratu wypisz bez wymuszania miejsc po przecinku (jak w przykładzie).*

### Wejście

* 1 linia: `r` (liczba rzeczywista)
* 2 linia: `a` (liczba rzeczywista)

### Wyjście

Blok informacji o kole, pusta linia, blok informacji o kwadracie.

### Przykład

**Wejście:**

```
5
4
```

**Wyjście:**

```
Kształt: Koło
Promień: 5
Pole powierzchni: 78.5398

Kształt: Kwadrat
Długość boku: 4
Pole powierzchni: 16
```

*/

#include <cassert>
#include <cmath>
#include <numbers>
#include <stdexcept>

class Ksztalt {
 public:
  virtual double obwod() = 0;
  virtual double pole() = 0;
};

class Kolo : public Ksztalt {
 public:
  Kolo(double _promien) {
    if (_promien <= 0)
      throw std::invalid_argument("Wartosc musi byc dodatnia.");

    promien = _promien;
  }

  double obwod() { return 2 * std::numbers::pi * promien; }

  double pole() { return std::numbers::pi * pow(promien, 2); }

 private:
  double promien;
};

class Kwadrat : public Ksztalt {
 public:
  Kwadrat(double _bok) {
    if (_bok <= 0) throw std::invalid_argument("Wartosc musi byc dodatnia.");

    bok = _bok;
  }

  double obwod() { return 4 * bok; }

  double pole() { return pow(bok, 2); }

 private:
  double bok;
};

void test1() {
  Kolo kolo(3);
  assert(abs(kolo.obwod() - 18.85) < 0.01);
  assert(abs(kolo.pole() - 28.27) < 0.01);
}

void test2() {
  Kwadrat kwadrat(3);
  assert(abs(kwadrat.obwod() - 12) < 0.01);
  assert(abs(kwadrat.pole() - 9) < 0.01);
}

int main() {
  test1();
  test2();

  return 0;
}
