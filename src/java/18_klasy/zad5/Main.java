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

public class Main {

  private double Re;
  private double Im;

  public Main() {
    Re = 0;
    Im = 0;
  }

  public Main(double a, double b) {
    Re = a;
    Im = b;
  }

  public Main(Main innaZespolona) {
    Re = innaZespolona.Re;
    Im = innaZespolona.Im;
  }

  public final double Modul() {
    return Math.sqrt(Re * Re + Im * Im);
  }

  public final void Sprzezenie() {
    Im *= -1;
  }

  public static Main suma(final Main z1, final Main z2) {
    Main z3 = new Main(z1.Re + z2.Re, z1.Im + z2.Im);
    return new Main(z3);
  }

  public static Main roznica(final Main z1, final Main z2) {
    Main z3 = new Main(z1.Re - z2.Re, z1.Im - z2.Im);
    return new Main(z3);
  }

  public static Main iloczyn(final Main z1, final Main z2) {
    Main z3 = new Main(z1.Re * z2.Re - z1.Im * z2.Im, z1.Im * z2.Re + z2.Im * z1.Re);
    return new Main(z3);
  }

  public Main podziel(final Main z2) {
    double a = (Re * z2.Re + Im * z2.Im) / (z2.Re * z2.Re + z2.Im * z2.Im);
    double b = (Re * z2.Im - Im * z2.Re) / (z2.Re * z2.Re + z2.Im * z2.Im);
    Main z3 = new Main(a, b);
    return new Main(z3);
  }

  public boolean equalsTo(final Main z1, final Main z2) {
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

    Main z1 = new Main();
    Main z2 = new Main(9, 12);

    System.out.print(z1);
    System.out.print("\n");

    System.out.print(z2);
    System.out.print("\n");

    System.out.print(Main.iloczyn(z1, z2));
    System.out.print("\n");

    Main z3 = new Main(-3, -3);

    System.out.print(Main.suma(z3, z2));
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

