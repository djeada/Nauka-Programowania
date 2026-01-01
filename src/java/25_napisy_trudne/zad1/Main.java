/*
ZAD-01 — Podmiana słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Masz trzy napisy:

1. Zdanie (tekst do modyfikacji),
2. Słowo A (podnapis do znalezienia),
3. Słowo B (podnapis zastępujący).

Zamień **wszystkie wystąpienia** słowa/podnapisu **A** na **B** w podanym zdaniu.

> Uwaga: A może być częścią innych słów — zamiana dotyczy **każdego wystąpienia podnapisu**.

### Wejście

* 1 linia: zdanie `S`
* 2 linia: napis `A`
* 3 linia: napis `B`

### Wyjście

* 1 linia: zdanie po zamianie

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
rzy
```

**Wyjście:**

```
Lerzy jerzy na wierzy
```

*/
import java.util.*;

public class Main {
  // Podmienia wszystkie wystąpienia słowaA na słowoB w napisie
  // Złożoność czasowa: O(n*m) gdzie n to długość napisu, m to długość słowa
  // Złożoność pamięciowa: O(n)
  public static String podmienNapis(String napis, String slowoA, String slowoB) {
    String wynik = napis.replaceAll(slowoA, slowoB);
    return wynik;
  }

  // Testy Poprawnosci
  public static void test1() {
    String napis = "Ala ma kota, kot ma Ale";
    String slowoA = "kot";
    String slowoB = "pies";
    String wynik = "Ala ma piesa, pies ma Ale";

    assert (podmienNapis(napis, slowoA, slowoB).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
  }
}

