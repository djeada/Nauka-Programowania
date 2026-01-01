/*
ZAD-02A — Suma dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `suma(a, b)`, która zwraca sumę dwóch liczb całkowitych.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita)
* `b` (liczba całkowita)

### Wyjście

Funkcja zwraca:

* `a + b`

### Przykład

**Wywołanie funkcji:**

```python
print(suma(3, 5))
```

**Wyjście:**

```
8
```

ZAD-02B — Różnica: b − a

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `roznica(a, b)`, która zwraca różnicę: `b - a`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Wyjście

Funkcja zwraca:

* `b - a`

### Przykład

**Wywołanie funkcji:**

```python
print(roznica(3, 5))
```

**Wyjście:**

```
2
```

ZAD-02C — Iloczyn dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `arytmetyka`

### Treść

Napisz funkcję `iloczyn(a, b)`, która zwraca iloczyn `a * b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Wyjście

Funkcja zwraca:

* `a * b`

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 5))
```

**Wyjście:**

```
15
```

ZAD-02D — Iloraz całkowity: a // b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `dzielenie`, `//`

### Treść

Napisz funkcję `iloraz(a, b)`, która zwraca iloraz całkowity `a // b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Ograniczenia / gwarancje

* `b ≠ 0`

### Wyjście

Funkcja zwraca:

* `a // b`

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 5))
```

**Wyjście:**

```
0
```

ZAD-02E — Reszta z dzielenia: a % b

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `modulo`, `%`

### Treść

Napisz funkcję `reszta(a, b)`, która zwraca resztę z dzielenia `a % b`.

### Wejście

Dwa argumenty funkcji: `a`, `b` (liczby całkowite)

### Ograniczenia / gwarancje

* `b ≠ 0`

### Wyjście

Funkcja zwraca:

* `a % b`

### Przykład

**Wywołanie funkcji:**

```python
print(reszta(3, 5))
```

**Wyjście:**

```
3
```

*/
import java.util.*;

public class Main {
  // Pobierz dwie liczby od uzytkownika. Napisz funkcje, ktora
  // dla otrzymanych dwoch liczb zwroci:

  // a) ich sume
  public static int suma(int a, int b) {
    return a + b;
  }

  // b) roznice drugiej i pierwszej
  public static int roznica(int a, int b) {
    return b - a;
  }

  // c) ich iloczyn
  public static int iloczyn(int a, int b) {
    return a * b;
  }

  // d) reszte z dzielenia pierwszej przez druga
  public static int reszta(int a, int b) {
    return a % b;
  }

  public static void main(String[] args) {

    System.out.print("Podaj dwie liczby: \n");

    Scanner s = new Scanner(System.in);

    int a = Integer.parseInt(s.nextLine());
    int b = Integer.parseInt(s.nextLine());

    System.out.print("suma liczb to: " + suma(a, b) + "\n");
    System.out.print("roznice drugiej i pierwszej to: " + roznica(a, b) + "\n");
    System.out.print("iloczyn liczb to: " + iloczyn(a, b) + "\n");
    System.out.print("reszte z dzielenia pierwszej przez druga to: " + reszta(a, b) + "\n");
  }
}

