/*
ZAD-07A — Pole trójkąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole trójkąta ze wzoru:
( P = \frac{1}{2} a h )

### Wejście

* 1 linia: `a`
* 2 linia: `h`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
6
4
```

**Wyjście:**

```
12.000
```

ZAD-07B — Pole prostokąta

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole prostokąta:
( P = ab )

### Wejście

* 1 linia: `a`
* 2 linia: `b`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2.5
4
```

**Wyjście:**

```
10.000
```

ZAD-07C — Pole rombu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz pole rombu z przekątnych:
( P = \frac{1}{2} d_1 d_2 )

### Wejście

* 1 linia: `d1`
* 2 linia: `d2`

### Wyjście

* 1 linia: `P` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
10
6
```

**Wyjście:**

```
30.000
```

ZAD-07D — Objętość kuli

**Poziom:** ★★☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Oblicz objętość kuli:
( V = \frac{4}{3}\pi r^3 )

### Wejście

* 1 linia: `r`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
1
```

**Wyjście:**

```
4.189
```

ZAD-07E — Objętość stożka

**Poziom:** ★★☆
**Tagi:** `geometria`, `pi`, `float`

### Treść

Oblicz objętość stożka:
( V = \frac{1}{3}\pi r^2 h )

### Wejście

* 1 linia: `r`
* 2 linia: `h`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2
3
```

**Wyjście:**

```
12.566
```

ZAD-07F — Objętość prostopadłościanu

**Poziom:** ★☆☆
**Tagi:** `geometria`, `float`

### Treść

Oblicz objętość prostopadłościanu:
( V = abc )

### Wejście

* 1 linia: `a`
* 2 linia: `b`
* 3 linia: `c`

### Wyjście

* 1 linia: `V` do **3 miejsc po przecinku**

### Przykład

**Wejście:**

```
2
3
4
```

**Wyjście:**

```
24.000
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {
    // Pobierz podstawe i wysokosc trojkata i wypisz pole.

    System.out.print("podaj podstawe i wysokosc trojkata: \n");

    Scanner s = new Scanner(System.in);

    float a = Float.parseFloat(s.nextLine());
    float h = Float.parseFloat(s.nextLine());

    System.out.print(
        "pole trojkata o podstawie "
            + a
            + " i wysokosci "
            + h
            + " jest rowne "
            + (a * h / 2)
            + "\n");

    // Pobierz dlogosci bokow prostokata i wypisz pole.

    System.out.print("podaj dlugosci bokow prostokata:\n");

    a = Float.parseFloat(s.nextLine());

    float b = Float.parseFloat(s.nextLine());

    System.out.print("pole prostokata o bokach " + a + " i " + b + " jest rowne " + (a * b) + "\n");
  }
}

