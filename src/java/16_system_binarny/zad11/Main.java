/*
ZAD-11 — Palindrom w systemie binarnym

**Poziom:** ★★☆
**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej reprezentacja binarna (bez wiodących zer) jest palindromem.

Wypisz:

* `Prawda` — jeśli tak,
* `Fałsz` — jeśli nie.

### Wejście

* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda` lub `Fałsz`.

### Przykład

**Wejście:**

```
26
```

**Wyjście:**

```
Fałsz
```

### Uwagi (ważne)

* `26` ma zapis binarny `11010`, który **nie** jest palindromem.
  (W Twoim wcześniejszym przykładzie było to opisane błędnie — tu trzymamy się definicji palindromu 1:1.)

*/
import java.util.BitSet;

public class Main {
  // Czy liczba jest palindromem?

  public static final int liczbaBitow = 8;

  // Zlozonosc Czasowa: O(1) - stala liczba bitow
  // Zlozonosc Pamieciowa: O(1)
  public static boolean czyPalindromV1(int liczba) {
    BitSet bity = BitSet.valueOf(new long[] {liczba});

    for (int i = 0; i < liczbaBitow / 2 - 1; i++) {
      int val1 = bity.get(i) ? 1 : 0;
      int val2 = bity.get(liczbaBitow - 1 - i) ? 1 : 0;

      if ((val1 ^ val2) != 0) {
        return false;
      }
    }

    return true;
  }

  public static void test1() {
    int liczba = 231;
    assert czyPalindromV1(liczba);
  }

  public static void test2() {
    int liczba = 17;
    assert !czyPalindromV1(liczba);
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

