/*
ZAD-08 — Koszt pokrycia podłogi płytkami

**Poziom:** ★★☆
**Tagi:** `ceil`, `arytmetyka`, `formatowanie`, `geometria`

### Treść

Dane są:

* cena jednej płytki `p`,
* bok płytki `t` (płytka kwadratowa),
* długość podłogi `L`,
* szerokość podłogi `W`.

Oblicz liczbę płytek potrzebnych do pokrycia całej podłogi, zakładając układ bez docinania „na styk” (czyli wzdłuż każdego wymiaru zaokrąglasz w górę), a następnie podaj koszt całkowity.

### Wejście

4 liczby (każda w osobnej linii): `p`, `t`, `L`, `W`

### Wyjście

Jedna liczba: całkowity koszt do **2 miejsc po przecinku**.

### Ograniczenia / gwarancje

* `p > 0`, `t > 0`, `L > 0`, `W > 0`
* Liczba płytek:

  * `nL = ceil(L / t)`
  * `nW = ceil(W / t)`
  * `n = nL * nW`
* Koszt: `n * p`

### Przykład

**Wejście:**

```
2
3
20
40
```

**Wyjście:**

```
196.00
```

*/
import java.util.*;

public class Main {
  public static void main(String[] args) {

    Scanner s = new Scanner(System.in);
    double p = Double.parseDouble(s.nextLine());
    double t = Double.parseDouble(s.nextLine());
    double L = Double.parseDouble(s.nextLine());
    double W = Double.parseDouble(s.nextLine());

    int nL = (int) Math.ceil(L / t);
    int nW = (int) Math.ceil(W / t);
    int n = nL * nW;

    double cost = n * p;

    System.out.printf("%.2f%n", cost);
  }
}

