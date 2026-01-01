/*
ZAD-09 — Najdłuższy wspólny podnapis

**Poziom:** ★★★
**Tagi:** `string`, `dp`, `substring`

### Treść

Otrzymujesz dwa napisy. Znajdź **najdłuższy wspólny podnapis** (ciągły fragment), który występuje w obu napisach.

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: najdłuższy wspólny podnapis
  (jeśli jest kilka o tej samej długości — wybierz ten, który występuje **najwcześniej w A**; jeśli nadal remis, najwcześniej w B)

### Przykład

**Wejście:**

```
ijkabcdl
xxxxabcd
```

**Wyjście:**

```
abcd
```

*/
import java.util.*;

public class Main {
  // Znajduje najdłuższy wspólny podnapis dwóch napisów
  // Złożoność czasowa: O(n*m) gdzie n i m to długości napisów
  // Złożoność pamięciowa: O(n*m)
  public static String najdluzszyPodnapis(String napis1, String napis2) {
    String wynik = "";
    String wynik_tmp = "";

    for (int i = 0; i < napis1.length(); i++) {
      wynik_tmp = "";
      for (int j = i; j < napis1.length(); j++) {
        wynik_tmp += napis1.charAt(j);
        if (napis2.contains(wynik_tmp)) {
          if (wynik_tmp.length() > wynik.length()) {
            wynik = wynik_tmp;
          }
        }
      }
    }

    return wynik;
  }

  public static void test1() {
    String napis1 = "abcdxyz";
    String napis2 = "xyzabcd";
    String wynik = "abcd";

    assert (najdluzszyPodnapis(napis1, napis2).equals(wynik));
  }

  public static void test2() {
    String napis1 = "hhaall";
    String napis2 = "hhaall";
    String wynik = "hhaall";

    assert (najdluzszyPodnapis(napis1, napis2).equals(wynik));
  }

  public static void test3() {
    String napis1 = "";
    String napis2 = "";
    String wynik = "";

    assert (najdluzszyPodnapis(napis1, napis2).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

