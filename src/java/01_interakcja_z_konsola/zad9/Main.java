/*
ZAD-09 — Kalkulator kredytowy (rata annuitetowa)

**Poziom:** ★★☆
**Tagi:** `finanse`, `float`, `formatowanie`

### Treść

Wczytaj:

* roczną stopę procentową `R` (w %),
* okres spłaty `Y` (w latach),
* kwotę kredytu `P`.

Oblicz miesięczną ratę `M` oraz całkowity koszt `C = M * n`, gdzie `n = 12 * Y`.

Dla `R > 0` użyj wzoru:
[
M = P \cdot \frac{r(1+r)^n}{(1+r)^n-1}
]
gdzie `r = R / (12*100)`.

Dla `R = 0` przyjmij:

* `M = P / n`.

### Wejście

3 liczby (w osobnych liniach):

1. `R` (float, `R ≥ 0`)
2. `Y` (int, `Y > 0`)
3. `P` (float, `P > 0`)

### Wyjście

Dwie linie (do **2 miejsc po przecinku**):

1. miesięczna rata `M`
2. całkowity koszt `C`

### Przykład

**Wejście:**

```
3.5
8
12000
```

**Wyjście:**

```
143.50
13776.00
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    // Otrzymujesz roczna stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc
    // udzielonego kredytu. Oblicz miesieczna rate oraz calkowity koszt kredytu.

    System.out.print(
        "Podaj: stope procentowa, liczbe lat na splacenie kredytu oraz wysokosc udzielonego"
            + " kredytu");
    System.out.print("\n");

    float stopa;
    int lata;
    int kredyt;

    Scanner s = new Scanner(System.in);

    stopa = Float.parseFloat(s.nextLine());
    lata = Integer.parseInt(s.nextLine());
    kredyt = Integer.parseInt(s.nextLine());

    float r = (float) (stopa / 12 * 0.01);
    int n = lata * 12;

    float rata = (float) (kredyt * r * Math.pow((1 + r), n) / (Math.pow((1 + r), n) - 1));
    float calkKosz = rata * n;

    System.out.printf("rata mieieczna to ");
    System.out.printf("%.2f", rata);
    System.out.printf("\n");
    System.out.printf("calkowity koszt to ");
    System.out.printf("%.2f", calkKosz);
    System.out.printf("\n");
  }
}

