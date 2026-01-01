/*
ZAD-18 — Odwróć słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `split`, `string`, `pętle`

### Treść

Wczytaj zdanie i odwróć litery **w każdym słowie osobno**, zachowując kolejność słów.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie z odwróconymi słowami

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
alA am atok
```

*/

import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class Main {

  public static String odwrocNapisyV1(String napis) {

    String[] slowa = napis.split(" ");
    StringBuilder odwrocony = new StringBuilder();

    for (String word : slowa) {

      StringBuilder reverseWord = new StringBuilder();

      for (int i = word.length() - 1; i >= 0; i--) {
        reverseWord.append(word.charAt(i));
      }

      odwrocony.append(reverseWord).append(" ");
    }

    return odwrocony.toString().trim();
  }

  public static String odwrocNapisyV2(String napis) {
    return Pattern.compile(" +")
        .splitAsStream(napis)
        .map(w -> new StringBuilder(w).reverse())
        .collect(Collectors.joining(" "));
  }

  public static void main(String[] args) {

    String napis = "Cameron Diaz";
    String wynik = "noremaC zaiD";

    assert odwrocNapisyV1(napis).equals(wynik);
    assert odwrocNapisyV2(napis).equals(wynik);
  }
}

