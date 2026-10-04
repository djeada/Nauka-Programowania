/*
ZAD-06 — Klasa LiczbaZespolona

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasę `LiczbaZespolona` opisującą liczbę zespoloną $a + bi$:

* konstruktor `__init__(self, re=0, im=0)` — część rzeczywista i urojona,
* operatory `+`, `-`, `*`, `/` (metody `__add__`, `__sub__`, `__mul__`, `__truediv__`) zwracające nową liczbę zespoloną:
  * $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$,
  * $\frac{a + bi}{c + di} = \frac{ac + bd}{c^2 + d^2} + \frac{bc - ad}{c^2 + d^2}i$ (dzielnik jest różny od zera),
* porównanie `==` (metoda `__eq__`) — liczby są równe, gdy mają równe części rzeczywiste i urojone,
* metodę `modul()` zwracającą moduł liczby: $|a + bi| = \sqrt{a^2 + b^2}$,
* metodę `__str__()` zwracającą napis `a + bi` albo `a - bi` (gdy część urojona jest ujemna, wypisz minus i jej wartość bezwzględną). Obie części wypisz z dokładnością do 2 miejsc po przecinku, np. `9.00 + 12.00i`, `-3.00 - 3.00i`.

Program wczytuje liczby $A$ i $B$ i wypisuje wyniki działań.

### Wejście

* 1. linia: dwie liczby całkowite — część rzeczywista i urojona liczby $A$
* 2. linia: dwie liczby całkowite — część rzeczywista i urojona liczby $B$

### Wyjście

Osiem linii:

```
Liczba A: <A>
Liczba B: <B>
Suma: <A + B>
Różnica A - B: <A - B>
Iloczyn: <A * B>
Iloraz A / B: <A / B>
Moduł liczby A: <|A|>
Liczby są równe.
```

* Jeśli $B = 0 + 0i$, zamiast ilorazu wypisz `Iloraz A / B: nie można dzielić przez zero`.
* Moduł wypisz z dokładnością do 2 miejsc po przecinku.
* W ostatniej linii wypisz `Liczby są równe.` albo `Liczby są różne.`

### Ograniczenia

* Części rzeczywiste i urojone są liczbami całkowitymi z przedziału $[-100, 100]$.

### Przykład

**Wejście:**

```
9 12
-3 -3
```

**Wyjście:**

```
Liczba A: 9.00 + 12.00i
Liczba B: -3.00 - 3.00i
Suma: 6.00 + 9.00i
Różnica A - B: 12.00 + 15.00i
Iloczyn: 9.00 - 63.00i
Iloraz A / B: -3.50 - 0.50i
Moduł liczby A: 15.00
Liczby są różne.
```

Iloczyn: $(9 + 12i)(-3 - 3i) = (-27 + 36) + (-27 - 36)i = 9 - 63i$.

### Kod startowy

```python
import math


class LiczbaZespolona:
    def __init__(self, re=0, im=0):
        # Uzupełnij.
        pass

    def __add__(self, other):
        # Uzupełnij.
        pass

    def __sub__(self, other):
        # Uzupełnij.
        pass

    def __mul__(self, other):
        # Uzupełnij.
        pass

    def __truediv__(self, other):
        # Uzupełnij.
        pass

    def __eq__(self, other):
        # Uzupełnij.
        pass

    def modul(self):
        # Uzupełnij.
        pass

    def __str__(self):
        # Uzupełnij: zwróć napis "a + bi" albo "a - bi".
        pass


re, im = input().split()
a = LiczbaZespolona(int(re), int(im))
re, im = input().split()
b = LiczbaZespolona(int(re), int(im))

print(f"Liczba A: {a}")
print(f"Liczba B: {b}")
print(f"Suma: {a + b}")
print(f"Różnica A - B: {a - b}")
print(f"Iloczyn: {a * b}")
if b == LiczbaZespolona(0, 0):
    print("Iloraz A / B: nie można dzielić przez zero")
else:
    print(f"Iloraz A / B: {a / b}")
print(f"Moduł liczby A: {a.modul():.2f}")
if a == b:
    print("Liczby są równe.")
else:
    print("Liczby są różne.")
```

*/
import java.util.Locale;
import java.util.Objects;
import java.util.Scanner;

public class Main {

  // Liczba zespolona a + bi. Działania zwracają nową liczbę.
  private static class LiczbaZespolona {
    private final double re;
    private final double im;

    public LiczbaZespolona() {
      this(0, 0);
    }

    public LiczbaZespolona(final double re, final double im) {
      // Dodanie 0.0 zamienia -0.0 na 0.0 (inaczej wypisalibyśmy "-0.00").
      this.re = re + 0.0;
      this.im = im + 0.0;
    }

    public double getRe() {
      return re;
    }

    public double getIm() {
      return im;
    }

    public LiczbaZespolona dodaj(final LiczbaZespolona inna) {
      return new LiczbaZespolona(re + inna.re, im + inna.im);
    }

    public LiczbaZespolona odejmij(final LiczbaZespolona inna) {
      return new LiczbaZespolona(re - inna.re, im - inna.im);
    }

    // (a + bi)(c + di) = (ac - bd) + (ad + bc)i
    public LiczbaZespolona pomnoz(final LiczbaZespolona inna) {
      return new LiczbaZespolona(re * inna.re - im * inna.im, re * inna.im + im * inna.re);
    }

    // (a + bi) / (c + di) = (ac + bd) / (c² + d²) + (bc - ad) / (c² + d²) i
    public LiczbaZespolona podziel(final LiczbaZespolona inna) {
      double mianownik = inna.re * inna.re + inna.im * inna.im;

      if (mianownik == 0) {
        throw new ArithmeticException("Nie można dzielić przez zero.");
      }

      return new LiczbaZespolona(
          (re * inna.re + im * inna.im) / mianownik, (im * inna.re - re * inna.im) / mianownik);
    }

    public double modul() {
      return Math.sqrt(re * re + im * im);
    }

    public boolean czyZero() {
      return re == 0 && im == 0;
    }

    @Override
    public boolean equals(final Object obiekt) {
      if (this == obiekt) {
        return true;
      }
      if (!(obiekt instanceof LiczbaZespolona)) {
        return false;
      }
      LiczbaZespolona inna = (LiczbaZespolona) obiekt;
      return re == inna.re && im == inna.im;
    }

    @Override
    public int hashCode() {
      return Objects.hash(re, im);
    }

    @Override
    public String toString() {
      if (im < 0) {
        return String.format(Locale.ROOT, "%.2f - %.2fi", re, -im);
      }
      return String.format(Locale.ROOT, "%.2f + %.2fi", re, im);
    }
  }

  private static boolean prawieRowne(final double a, final double b) {
    return Math.abs(a - b) < 1e-9;
  }

  public static void testDzialania() {
    LiczbaZespolona a = new LiczbaZespolona(9, 12);
    LiczbaZespolona b = new LiczbaZespolona(-3, -3);

    assert a.dodaj(b).equals(new LiczbaZespolona(6, 9));
    assert a.odejmij(b).equals(new LiczbaZespolona(12, 15));
    assert a.pomnoz(b).equals(new LiczbaZespolona(9, -63));

    LiczbaZespolona iloraz = a.podziel(b);
    assert prawieRowne(iloraz.getRe(), -3.5) && prawieRowne(iloraz.getIm(), -0.5);
    assert prawieRowne(a.modul(), 15);
  }

  public static void testDzieleniePrzezZero() {
    try {
      new LiczbaZespolona(3, 4).podziel(new LiczbaZespolona());
      assert false;
    } catch (ArithmeticException e) {
      assert true;
    }
  }

  public static void testNapis() {
    assert new LiczbaZespolona(9, 12).toString().equals("9.00 + 12.00i");
    assert new LiczbaZespolona(-3, -3).toString().equals("-3.00 - 3.00i");
    assert new LiczbaZespolona(-0.0, -0.0).toString().equals("0.00 + 0.00i");
  }

  public static void testRownosc() {
    assert new LiczbaZespolona(1, 1).equals(new LiczbaZespolona(1, 1));
    assert !new LiczbaZespolona(1, 1).equals(new LiczbaZespolona(1, -1));
  }

  public static void main(String[] args) {
    testDzialania();
    testDzieleniePrzezZero();
    testNapis();
    testRownosc();

    Scanner scanner = new Scanner(System.in);
    LiczbaZespolona a = new LiczbaZespolona(scanner.nextInt(), scanner.nextInt());
    LiczbaZespolona b = new LiczbaZespolona(scanner.nextInt(), scanner.nextInt());
    scanner.close();

    System.out.println("Liczba A: " + a);
    System.out.println("Liczba B: " + b);
    System.out.println("Suma: " + a.dodaj(b));
    System.out.println("Różnica A - B: " + a.odejmij(b));
    System.out.println("Iloczyn: " + a.pomnoz(b));

    if (b.czyZero()) {
      System.out.println("Iloraz A / B: nie można dzielić przez zero");
    } else {
      System.out.println("Iloraz A / B: " + a.podziel(b));
    }

    System.out.println(String.format(Locale.ROOT, "Moduł liczby A: %.2f", a.modul()));

    if (a.equals(b)) {
      System.out.println("Liczby są równe.");
    } else {
      System.out.println("Liczby są różne.");
    }
  }
}
