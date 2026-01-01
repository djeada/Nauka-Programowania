/*
ZAD-05 — Wyodrębnij cyfry z tekstu

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis zawierający różne znaki. Wyodrębnij wszystkie cyfry i wypisz je jako jeden napis (z zachowaniem kolejności).

### Wejście

Jedna linia:

* `tekst`

### Wyjście

Jedna linia:

* napis złożony tylko z cyfr z tekstu wejściowego

### Przykład

**Wejście:**

```
Terminator2001
```

**Wyjście:**

```
2001
```

*/
import java.util.*;

public class Main {

  // Wyodrębnia wszystkie cyfry z tekstu - usuwa znaki niecyfrowe
  // Złożoność czasowa: O(n) gdzie n to długość napisu
  // Złożoność pamięciowa: O(n)
  public static String odfiltrujCyfryV1(String napis) {
    return napis.replaceAll("[^0-9]", "");
  }

  public static void test1() {
    String napis = "numer 32.19 wyzej niz 31.17";
    String wynik = "32193117";
    assert odfiltrujCyfryV1(napis).equals(wynik);
  }

  public static void test2() {
    String napis = "Lezy jerzy na wiezy";
    String wynik = "";
    assert odfiltrujCyfryV1(napis).equals(wynik);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

