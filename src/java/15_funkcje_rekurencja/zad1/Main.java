/*
ZAD-01 — Wartość wielomianu w punkcie

**Poziom:** ★☆☆
**Tagi:** `wielomiany`, `Horner`, `I/O`

### Treść

Wczytaj współczynniki wielomianu ( a_nx^n + a_{n-1}x^{n-1} + \dots + a_0 ) oraz liczbę ( x ). Oblicz wartość wielomianu w punkcie ( x ).

### Wejście

* 1. linia: `n` — stopień wielomianu (`n ≥ 0`)
* 2. linia: `n+1` liczb całkowitych: `a_n a_{n-1} ... a_0`
* 3. linia: `x` — liczba całkowita

### Wyjście

Jedna liczba całkowita — wartość wielomianu w punkcie `x`.

### Przykład

**Wejście:**

```
2
3 2 1
1
```

**Wyjście:**

```
6
```

### Uwagi o formatowaniu

* Użyj schematu Hornera (jest najprostszy i najszybszy).

*/
public class Main {

  public static String mniejszeLiczbyV1(int n) {

    if (n < 0) {
      return "";
    }

    if (n == 0) {
      return String.valueOf(n);
    }

    return String.valueOf(n) + ", " + mniejszeLiczbyV1(n - 1);
  }

  public static void main(String[] args) {
    int n = 10;
    String wynik = "10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0";
    System.out.print(mniejszeLiczbyV1(n));
    System.out.print("\n");
  }
}

