/*
ZAD-07 — Powtarzające się podnapisy

**Poziom:** ★★★
**Tagi:** `string`, `substrings`, `count`

### Treść

Otrzymujesz napis. Znajdź wszystkie **podnapisy**, które występują w nim **więcej niż jeden raz**.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: lista napisów — wszystkie powtarzające się podnapisy

### Przykład

**Wejście:**

```
pythonpython
```

**Wyjście:**

```
['python']
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności (np. rosnąco po długości/alfabetycznie) — musi to być opisane. W przeciwnym razie dopuszczalna może być dowolna kolejność.

*/
import java.util.*;

public class Main {
  public static String najdluzszePowtorzenie(String napis) {
    String wynik = "";
    String wynik_tmp = "";

    for (int i = 0; i < napis.length(); i++) {
      wynik_tmp = "";
      for (int j = i; j < napis.length(); j++) {
        wynik_tmp += napis.charAt(j);
        if (wynik_tmp.length() > wynik.length()) {
          wynik = wynik_tmp;
        }
      }
    }

    return wynik;
  }

  public static void test1() {
    String slowo = "98432934021742343230";
    String wynik = "432";

    assert (najdluzszePowtorzenie(slowo).equals(wynik));
  }

  public static void test2() {
    String slowo = "abcdef";
    String wynik = "";

    assert (najdluzszePowtorzenie(slowo).equals(wynik));
  }

  public static void test3() {
    String slowo = "Arnold i Arnold";
    String wynik = "Arnold";

    assert (najdluzszePowtorzenie(slowo).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

