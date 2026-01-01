/*
ZAD-08 — Najdłuższy wspólny przedrostek

**Poziom:** ★★★
**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz listę napisów (w kolejnych liniach). Znajdź najdłuższy przedrostek wspólny dla wszystkich.

### Wejście

* 1 linia: `n` — liczba napisów
* kolejne `n` linii: napisy

### Wyjście

* 1 linia: najdłuższy wspólny przedrostek (może być pusty)

### Przykład

**Wejście:**

```
3
Remolada
Remux
Remmy
```

**Wyjście:**

```
Rem
```

*/
import java.util.*;

public class Main {
  // Znajduje najdłuższy wspólny przedrostek dla wszystkich napisów z listy
  // Złożoność czasowa: O(n*m) gdzie n to liczba napisów, m to długość przedrostka
  // Złożoność pamięciowa: O(m)
  public static String najdluzszyPrzedrostek(List<String> napisy) {
    String wynik = "";
    String wynik_tmp = "";

    for (int i = 0; i < napisy.size(); i++) {
      wynik_tmp = "";
      for (int j = 0; j < napisy.get(i).length(); j++) {
        wynik_tmp += napisy.get(i).charAt(j);
        if (wynik_tmp.length() > wynik.length()) {
          wynik = wynik_tmp;
        }
      }
    }

    return wynik;
  }

  public static void test1() {
    List<String> napisy = Arrays.asList("abcdefgh", "abcefgh", "abcd");
    String wynik = "abc";

    assert (najdluzszyPrzedrostek(napisy).equals(wynik));
  }

  public static void test2() {
    List<String> napisy = Arrays.asList("flower", "flow", "flight", "flix");
    String wynik = "fl";

    assert (najdluzszyPrzedrostek(napisy).equals(wynik));
  }

  public static void test3() {
    List<String> napisy = Arrays.asList("student", "studio", "stress", "lol");
    String wynik = "";

    assert (najdluzszyPrzedrostek(napisy).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

