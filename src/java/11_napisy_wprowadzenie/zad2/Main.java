/*
ZAD-02 — Policz wystąpienia znaku

**Poziom:** ★☆☆
**Tagi:** `string`, `count`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.

### Wejście

* 1. linia: napis
* 2. linia: pojedynczy znak

### Wyjście

* 1. linia: liczba wystąpień

### Przykład

**Wejście:**

```
klamra
a
```

**Wyjście:**

```
2
```

*/
import java.util.*;

public class Main {
  // Dla otrzymanego napisu oraz znaku,
  // znajdz liczbe wystapien znaku w napisie.

  // Zlozonosc Czasowa O(n)
  // Zlozonosc Pamieciowa O(1)
  public static int policzZnakV1(final String slowo, final char znak) {

    int licznik = 0;

    for (char x : slowo.toCharArray()) {
      if (x == znak) {
        licznik++;
      }
    }

    return licznik;
  }

  public static void test1() {
    String napis = "adam";
    char znak = 'a';
    int wynik = 2;

    assert policzZnakV1(napis, znak) == wynik;
  }

  public static void main(String[] args) {
    test1();
  }
}

