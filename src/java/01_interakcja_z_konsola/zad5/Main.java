/*
ZAD-05A — Funkcja liniowa: y = 3x + 10

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`, `formatowanie`

### Wejście

1 liczba: `x` (może być całkowita lub zmiennoprzecinkowa)

### Wyjście

1 liczba: `y` wypisana z dokładnością do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
19.000
```

ZAD-05B — Funkcja liniowa: y = ax + b

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`

### Wejście

3 liczby (każda w osobnej linii): `a`, `b`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Przykład

**Wejście:**

```
1
2
3
```

**Wyjście:**

```
5.000
```

ZAD-05C — Funkcja sześcienna: y = x³ + 2

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Treść

Oblicz: `y = x^3 + 22 - 20`, czyli równoważnie `y = x^3 + 2`.

### Wejście

1 liczba: `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
127.000
```

ZAD-05D — Wielomian z potęgami: y = a·x^m + b·x^n + c − a

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Wejście

6 liczb (w osobnych liniach): `a`, `b`, `c`, `m`, `n`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* `m` i `n` są liczbami całkowitymi (np. nieujemnymi), aby potęgowanie było jednoznaczne w typowych językach.

### Przykład

**Wejście:**

```
1
1
1
1
1
1
```

**Wyjście:**

```
2.000
```

ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem

**Poziom:** ★★★☆
**Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`

### Treść

Dla `x` (w radianach) oblicz:
[
y=\sin^3(x)\cdot\cos^2(x)+e^{x^2}+\ln(x^3+2x^2-x-3)
]

### Wejście

1 liczba zmiennoprzecinkowa: `x` (w radianach)

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* Dane testowe spełniają warunek dziedziny logarytmu:

  * (x^3+2x^2-x-3 > 0)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
57.179
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // ZAD-05A: Wyznacz wartosc funkcji y = 3x + 10 w zadanym punkcie.

    Scanner s = new Scanner(System.in);
    double x = Double.parseDouble(s.nextLine());
    double y = 3 * x + 10;
    System.out.printf("%.3f%n", y);

    // ZAD-05B: Pobierz wspolczynniki a, b oraz punkt x i wyznacz wartosc funkcji y = ax + b w
    // zadanym punkcie.

    double a = Double.parseDouble(s.nextLine());
    double b = Double.parseDouble(s.nextLine());
    x = Double.parseDouble(s.nextLine());
    y = a * x + b;
    System.out.printf("%.3f%n", y);

    // ZAD-05C: Wyznacz wartosc funkcji y = x^3 + 2 w zadanym punkcie.

    x = Double.parseDouble(s.nextLine());
    y = Math.pow(x, 3) + 2;
    System.out.printf("%.3f%n", y);

    // ZAD-05D: Pobierz wspolczynniki a, b, c, m, n oraz punkt x i wyznacz wartosc funkcji y =
    // a*x^m + b*x^n + c - a w zadanym punkcie.

    a = Double.parseDouble(s.nextLine());
    b = Double.parseDouble(s.nextLine());
    double c = Double.parseDouble(s.nextLine());
    int m = Integer.parseInt(s.nextLine());
    int n = Integer.parseInt(s.nextLine());
    x = Double.parseDouble(s.nextLine());
    y = a * Math.pow(x, m) + b * Math.pow(x, n) + c - a;
    System.out.printf("%.3f%n", y);

    // ZAD-05E: Wyznacz wartosc funkcji y = sin^3(x)*cos^2(x) + e^(x^2) + ln(x^3+2x^2-x-3) w
    // zadanym punkcie.

    x = Double.parseDouble(s.nextLine());
    y =
        Math.pow(Math.sin(x), 3) * Math.pow(Math.cos(x), 2)
            + Math.exp(Math.pow(x, 2))
            + Math.log(Math.pow(x, 3) + 2 * Math.pow(x, 2) - x - 3);
    System.out.printf("%.3f%n", y);
  }
}

