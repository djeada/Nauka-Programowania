/*
ZAD-04 — Zamień wszystkie małe litery na duże

**Poziom:** ★☆☆
**Tagi:** `string`, `upper`

### Treść

Wczytaj napis i zamień wszystkie litery na wielkie.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: napis po konwersji

### Przykład

**Wejście:**

```
Rumcajs
```

**Wyjście:**

```
RUMCAJS
```

*/
import java.util.*;

public class Main {
  // Otrzymujesz napis. Zamien wszystkie
  // male litery na wielkie.

  public static String naWielkieV1(String slowo) {

    return slowo.toUpperCase();
  }

  public static void test1() {
    String napis = "pacZka!";
    String wynik = "PACZKA!";

    assert naWielkieV1(napis).equals(wynik);
  }

  public static void main(String[] args) {
    test1();
  }
}

