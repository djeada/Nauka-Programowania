/*
ZAD-03 — Czy napis A jest początkiem napisu B?

**Poziom:** ★★☆
**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz dwa napisy:

1. Napis `A` — potencjalny przedrostek,
2. Napis `B` — napis testowany.

Sprawdź, czy `B` **zaczyna się** od `A`.

### Wejście

* 1 linia: `A`
* 2 linia: `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Dino
Dinozaur jest zly
```

**Wyjście:**

```
Prawda
```

*/
import java.util.*;

public class Main {

  public static boolean czyPoczatek(String napis1, String napis2) {
    if (napis1.length() < napis2.length()) return false;

    return napis1.substring(0, napis2.length()).equals(napis2);
  }

  public static void test1() {
    String napis1 = "Dinozaur jest zly";
    String napis2 = "Dino";
    boolean oczekiwane = true;
    boolean wynik = czyPoczatek(napis1, napis2);

    assert (oczekiwane == wynik);
  }

  public static void test2() {
    String napis1 = "Dinozaur jest zly";
    String napis2 = "Pies";
    boolean oczekiwane = false;
    boolean wynik = czyPoczatek(napis1, napis2);

    assert (oczekiwane == wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

