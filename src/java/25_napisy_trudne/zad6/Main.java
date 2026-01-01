/*
ZAD-06 — Rotacje napisów

**Poziom:** ★★★
**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy jeden z nich jest **rotacją** drugiego (mają tę samą długość i da się uzyskać jeden przez przesunięcie cykliczne drugiego).

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
malpka
pkamal
```

**Wyjście:**

```
Prawda
```

*/
import java.util.*;

public class Main {
  // Sprawdza czy napis2 jest rotacją napis1
  // Złożoność czasowa: O(n) gdzie n to długość napisów
  // Złożoność pamięciowa: O(n) - tworzenie zduplikowanego napisu
  public static boolean czyRotacja(String napis1, String napis2) {
    if (napis1.length() != napis2.length()) return false;

    String napis1_rot = napis1 + napis1;
    return napis1_rot.contains(napis2);
  }

  public static void test1() {
    String napis1 = "malpka";
    String napis2 = "kamapl";
    boolean oczekiwane = false;
    boolean wynik = czyRotacja(napis1, napis2);

    assert (wynik == oczekiwane);
  }

  public static void test2() {
    String napis1 = "malpka";
    String napis2 = "pkamal";
    boolean oczekiwane = true;
    boolean wynik = czyRotacja(napis1, napis2);

    assert (wynik == oczekiwane);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

