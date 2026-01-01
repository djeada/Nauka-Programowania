/*
ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz dwa napisy: zdanie oraz słowo. Sprawdź, czy słowo występuje w zdaniu jako samodzielne słowo (nie jako fragment innego słowa).

### Wejście

Dwie linie:

1. `zdanie`
2. `slowo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Siała baba mak.
babcia
```

**Wyjście:**

```
Fałsz
```

*/
import java.util.regex.Pattern;

public class Main {

  public static boolean czyNalezyV1(String napis, String podnapis) {
    return napis.matches("(?i).*" + Pattern.quote(podnapis) + ".*");
  }

  public static boolean czyNalezyV2(String napis, String podnapis) {
    return napis.indexOf(podnapis) != -1;
  }

  public static void test1() {
    String napis = "Mozart gra na skrzypcach";
    String podnapis = "skrzyp";
    boolean oczekiwane = true;
    boolean wynik = czyNalezyV1(napis, podnapis);
    assert wynik == oczekiwane;
  }

  public static void test2() {
    String napis = "Lezy jerzy na wiezy";
    String podnapis = "nan";
    boolean oczekiwane = true;
    boolean wynik = czyNalezyV1(napis, podnapis);
    assert wynik == oczekiwane;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

