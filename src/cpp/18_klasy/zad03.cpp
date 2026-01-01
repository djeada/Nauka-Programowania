/*
ZAD-03 — Pole nałożenia się dwóch prostokątów

**Poziom:** ★★☆
**Tagi:** `class`, `static`, `geometria`

### Treść

Zaprojektuj klasę **Prostokąt** opisaną przez dwa przeciwległe wierzchołki:

* lewy dolny `(x1, y1)`
* prawy górny `(x2, y2)`
  Boki równoległe do osi.

Klasa ma mieć:

1. Konstruktor `(x1, y1, x2, y2)`
2. Metodę statyczną `pole_wspolne(A, B)` zwracającą pole części wspólnej (albo
0).
3. Metodę wypisującą informacje o prostokącie.

Program tworzy:

* A: (3, 4) i (9, 6)
* B: (2, 2) i (7, 5)

Wypisuje oba i pole części wspólnej.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Prostokąt A: lewy dolny (3, 4), prawy górny (9, 6)
Prostokąt B: lewy dolny (2, 2), prawy górny (7, 5)
Pole części wspólnej: 6
```

*/

#include <cassert>
#include <cmath>

class Prostokat {
 public:
  Prostokat(double _lewo, double _prawo, double _gora, double _dol)
      : lewo(_lewo), prawo(_prawo), gora(_gora), dol(_dol) {}

  double getLewo() { return lewo; }

  double getPrawo() { return prawo; }

  double getGora() { return gora; }

  double getDol() { return dol; }

  double poleCzesciWspolnej(Prostokat &innyProstokat) {
    double poleX = std::max(0.00, std::min(prawo, innyProstokat.getPrawo()) -
                                      std::max(lewo, innyProstokat.getLewo()));
    double poleY = std::max(0.00, std::min(gora, innyProstokat.getGora()) -
                                      std::max(dol, innyProstokat.getDol()));
    return poleX * poleY;
  }

 private:
  double lewo, prawo, gora, dol;
};

void test1() {
  Prostokat prostokatA(2, 5, 7, 2);
  Prostokat prostokatB(3, 6, 9, 4);
  double wynik = 6.00;

  assert(prostokatA.poleCzesciWspolnej(prostokatB) == wynik);
}

void test2() {
  Prostokat prostokatA(-9.5, 10.5, 6, 2);
  Prostokat prostokatB(-4.5, 2.3, 3.8, -3.3);
  double wynik = 12.24;

  assert(abs(prostokatA.poleCzesciWspolnej(prostokatB) - wynik) < 0.01);
}

int main() {
  test1();
  test2();

  return 0;
}
