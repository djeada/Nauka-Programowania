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
2. Metodę statyczną `pole_wspolne(A, B)` zwracającą pole części wspólnej (albo 0).
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
public class Prostokat {

  private double lewo;
  private double prawo;
  private double gora;
  private double dol;

  public Prostokat(double _lewo, double _prawo, double _gora, double _dol) {
    this.lewo = _lewo;
    this.prawo = _prawo;
    this.gora = _gora;
    this.dol = _dol;
  }

  public final double getLewo() {
    return lewo;
  }

  public final double getPrawo() {
    return prawo;
  }

  public final double getGora() {
    return gora;
  }

  public final double getDol() {
    return dol;
  }

  public final double poleCzesciWspolnej(Prostokat innyProstokat) {
    double poleX =
        Math.max(
            0.00,
            Math.min(prawo, innyProstokat.getPrawo()) - Math.max(lewo, innyProstokat.getLewo()));
    double poleY =
        Math.max(
            0.00, Math.min(gora, innyProstokat.getGora()) - Math.max(dol, innyProstokat.getDol()));
    return poleX * poleY;
  }

  public static void test1() {
    Prostokat prostokatA = new Prostokat(2, 5, 7, 2);
    Prostokat prostokatB = new Prostokat(3, 6, 9, 4);
    double wynik = 6.00;

    assert prostokatA.poleCzesciWspolnej(prostokatB) == wynik;
  }

  public static void test2() {
    Prostokat prostokatA = new Prostokat(-9.5, 10.5, 6, 2);
    Prostokat prostokatB = new Prostokat(-4.5, 2.3, 3.8, -3.3);
    double wynik = 12.24;

    assert Math.abs(prostokatA.poleCzesciWspolnej(prostokatB) - wynik) < 0.01;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

