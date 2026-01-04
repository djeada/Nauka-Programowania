/*
ZAD-04 — Klasy Wektor2D i Wektor3D

**Poziom:** ★★☆
**Tagi:** `class`, `operatory`, `math`

### Treść

Zaprojektuj klasy **Wektor2D** i **Wektor3D**:

Wspólne:

* konstruktor z domyślnymi współrzędnymi 0,
* dodawanie, odejmowanie,
* iloczyn skalarny,
* porównania `==` i `!=`,
* moduł (długość),
* metoda wypisująca wektor.

Dodatkowo dla **Wektor3D**:

* iloczyn wektorowy.

Program tworzy:

* A = (-3, -3, -3)
* B = (5, 5, 5)

Wypisuje A, B oraz:

* A + B
* A - B
* A · B
* A × B

### Wejście

Brak.

### Wyjście

Jak w przykładzie.

### Przykład

**Wyjście:**

```
Wektor A: (-3, -3, -3)
Wektor B: (5, 5, 5)
Suma wektorów: (2, 2, 2)
Różnica wektorów A - B: (-8, -8, -8)
Iloczyn skalarny: -45
Iloczyn wektorowy: (0, 0, 0)
```

*/
import java.text.MessageFormat;

public class Main {

  private double x;
  private double y;
  private double z;

  public Main() {
    this(0, 0, 0);
  }

  public Main(double _x) {
    this(_x, 0, 0);
  }

  public Main(double _x, double _y) {
    this(_x, _y, 0);
  }

  public Main(double _x, double _y, double _z) {
    this.x = _x;
    this.y = _y;
    this.z = _z;
  }

  public Main(Main innyWektor) {
    this.x = innyWektor.getX();
    this.y = innyWektor.getY();
    this.z = innyWektor.getZ();
  }

  public final void setX(double _x) {
    x = _x;
  }

  public final void setY(double _y) {
    y = _y;
  }

  public final void setZ(double _z) {
    z = _z;
  }

  public final double getX() {
    return x;
  }

  public final double getY() {
    return y;
  }

  public final double getZ() {
    return z;
  }

  public final double modul() {
    double kwadratX = Math.pow(x, 2);
    double kwadratY = Math.pow(y, 2);
    double kwadratZ = Math.pow(z, 2);

    return Math.sqrt(kwadratX + kwadratY + kwadratZ);
  }

  public static Main suma(final Main w1, final Main w2) {
    Main w3 = new Main(w1.x + w2.x, w1.y + w2.y, w1.z + w2.z);
    return new Main(w3);
  }

  public static Main roznica(final Main w1, final Main w2) {
    Main w3 = new Main(w1.x - w2.x, w1.y - w2.y, w1.z - w2.z);
    return new Main(w3);
  }

  public static Main iloczyn(final Main w1, final Main w2) {
    double x = w1.y * w2.z - w1.z * w2.y;
    double y = w1.z * w2.x - w1.x * w2.z;
    double z = w1.x * w2.y - w1.y * w2.x;

    return new Main(x, y, z);
  }

  @Override
  public String toString() {

    return MessageFormat.format("({0}, {1}, {2})", this.x, this.y, this.z);
  }

  public boolean equalsTo(final Main w1, final Main w2) {
    return w1.x == w2.x && w1.y == w2.y && w1.z == w2.z;
  }

  public boolean notEqualsTo(final Main w1, final Main w2) {
    return w1.x != w2.x || w1.y != w2.y || w1.z != w2.z;
  }

  public static void main(String[] args) {

    Main wektorA = new Main(5, 5, 5);
    Main wektorB = new Main(-3, -3, -3);

    var suma = Main.suma(wektorA, wektorB);
    var roznica = Main.roznica(wektorA, wektorB);
    var iloczynWek = Main.iloczyn(wektorA, wektorB);

    System.out.print("Dla wektorow A: ");
    System.out.print(wektorA);
    System.out.print("\noraz B: ");
    System.out.print(wektorB);
    System.out.print("\notrzymujemy sume: ");
    System.out.print(suma);
    System.out.print("\nroznice: ");
    System.out.print(roznica);
    System.out.print("\niloczyn wektorowy: ");
    System.out.print(iloczynWek);
  }
}

