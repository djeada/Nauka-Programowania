/*
ZAD-04 — Usuń powtórzenia znaków

**Poziom:** ★★★
**Tagi:** `string`, `set`, `unique`, `kolejność`

### Treść

Otrzymujesz napis. Usuń wszystkie powtórzenia znaków tak, aby **każdy znak wystąpił tylko raz**, zachowując **kolejność pierwszych wystąpień**.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: napis z unikalnymi znakami

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
AB
```

*/
import java.util.*;

public class Main {

  public static String usunPowtorzeniaV1(String napis) {
    String wynik = "";

    for (int i = 0; i < napis.length(); i++) {
      if (!wynik.contains(String.valueOf(napis.charAt(i)))) {
        wynik += napis.charAt(i);
      }
    }

    return wynik;
  }

  public static void test1() {
    String napis = "AAAAAAAAAABBBBBBBBA";
    String wynik = "AB";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void test2() {
    String napis = "XXXYYASFBY";
    String wynik = "XYASFB";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void test3() {
    String napis = "CCCCCCCCCCCCCCCCCCCCCCCCCCCC";
    String wynik = "C";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void test4() {
    String napis = "XAZYBP";
    String wynik = "XAZYBP";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void test5() {
    String napis = "";
    String wynik = "";

    assert (usunPowtorzeniaV1(napis).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
    test4();
    test5();
  }
}

