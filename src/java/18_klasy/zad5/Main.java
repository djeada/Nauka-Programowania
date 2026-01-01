/*
ZAD-05 — Klasa Macierz

**Poziom:** ★★☆
**Tagi:** `class`, `macierze`, `operacje`

### Treść

Zaprojektuj klasę **Macierz**:

1. Konstruktor przyjmuje listę list (domyślnie pusta).
2. Operacje: dodawanie, odejmowanie, mnożenie.
3. Metoda wypisująca macierz (wierszami).
4. Porównania `==` i `!=`.

(Operację odwracania możesz pominąć w tym zadaniu, jeśli nie jest wymagana w sprawdzarce; najczęściej w podstawowych zadaniach nie ma testów na odwracanie.)

Program tworzy:

* A = [[1, 3], [4, 2]]
* B = [[5, 0], [1, 3]]

Wypisuje A, B, a potem A+B, A-B, A*B.

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Macierz A:
[1, 3]
[4, 2]

Macierz B:
[5, 0]
[1, 3]

Suma macierzy:
[6, 3]
[5, 5]

Różnica macierzy A - B:
[-4, 3]
[3, -1]

Iloczyn macierzy A * B:
[8, 9]
[22, 12]
```

*/
import java.text.MessageFormat;

public class Zespolona {

  private double Re;
  private double Im;

  public Zespolona() {
    Re = 0;
    Im = 0;
  }

  public Zespolona(double a, double b) {
    Re = a;
    Im = b;
  }

  public Zespolona(Zespolona innaZespolona) {
    Re = innaZespolona.Re;
    Im = innaZespolona.Im;
  }

  public final double Modul() {
    return Math.sqrt(Re * Re + Im * Im);
  }

  public final void Sprzezenie() {
    Im *= -1;
  }

  public static Zespolona suma(final Zespolona z1, final Zespolona z2) {
    Zespolona z3 = new Zespolona(z1.Re + z2.Re, z1.Im + z2.Im);
    return new Zespolona(z3);
  }

  public static Zespolona roznica(final Zespolona z1, final Zespolona z2) {
    Zespolona z3 = new Zespolona(z1.Re - z2.Re, z1.Im - z2.Im);
    return new Zespolona(z3);
  }

  public static Zespolona iloczyn(final Zespolona z1, final Zespolona z2) {
    Zespolona z3 = new Zespolona(z1.Re * z2.Re - z1.Im * z2.Im, z1.Im * z2.Re + z2.Im * z1.Re);
    return new Zespolona(z3);
  }

  public Zespolona podziel(final Zespolona z2) {
    double a = (Re * z2.Re + Im * z2.Im) / (z2.Re * z2.Re + z2.Im * z2.Im);
    double b = (Re * z2.Im - Im * z2.Re) / (z2.Re * z2.Re + z2.Im * z2.Im);
    Zespolona z3 = new Zespolona(a, b);
    return new Zespolona(z3);
  }

  public boolean equalsTo(final Zespolona z1, final Zespolona z2) {
    return z1.Re == z2.Re && z1.Im == z2.Im;
  }

  @Override
  public String toString() {

    if (Im >= 0) {
      return MessageFormat.format("{0} + j{1}", Re, Im);
    } else {
      return MessageFormat.format("{0} - j{1}", Re, Math.abs(Im));
    }
  }

  public static void main(String[] args) {

    Zespolona z1 = new Zespolona();
    Zespolona z2 = new Zespolona(9, 12);

    System.out.print(z1);
    System.out.print("\n");

    System.out.print(z2);
    System.out.print("\n");

    System.out.print(Zespolona.iloczyn(z1, z2));
    System.out.print("\n");

    Zespolona z3 = new Zespolona(-3, -3);

    System.out.print(Zespolona.suma(z3, z2));
    System.out.print("\n");

    System.out.print(z3.podziel(z2));
    System.out.print("\n");

    z2.Sprzezenie();

    System.out.print(z2);
    System.out.print("\n");

    System.out.print(z3.Modul());
    System.out.print("\n");
  }
}

