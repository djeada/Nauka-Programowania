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
// Zaprojektuj klase Ksztalt oraz klasy pochodne Kolo oraz Kwadrat.

public class Main {

  private static interface Ksztalt {
    double obwod();

    double pole();
  }

  private static class Kolo implements Ksztalt {
    public Kolo(double _promien) {
      if (_promien <= 0) {
        throw new IllegalArgumentException("Wartosc musi byc dodatnia.");
      }

      promien = _promien;
    }

    public final double obwod() {
      return 2 * Math.PI * promien;
    }

    public final double pole() {
      return Math.PI * Math.pow(promien, 2);
    }

    private double promien;
  }

  private static class Kwadrat implements Ksztalt {
    public Kwadrat(double _bok) {
      if (_bok <= 0) {
        throw new IllegalArgumentException("Wartosc musi byc dodatnia.");
      }

      bok = _bok;
    }

    public final double obwod() {
      return 4 * bok;
    }

    public final double pole() {
      return Math.pow(bok, 2);
    }

    private double bok;
  }

  public static void test1() {
    Kolo kolo = new Kolo(3);
    assert Math.abs(kolo.obwod() - 18.85) < 0.01;
    assert Math.abs(kolo.pole() - 28.27) < 0.01;
  }

  public static void test2() {
    Kwadrat kwadrat = new Kwadrat(3);
    assert Math.abs(kwadrat.obwod() - 12) < 0.01;
    assert Math.abs(kwadrat.pole() - 9) < 0.01;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

