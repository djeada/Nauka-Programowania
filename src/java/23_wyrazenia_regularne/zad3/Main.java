/*
ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis. Sprawdź, czy składa się wyłącznie z cyfr (`0–9`).

### Wejście

Jedna linia:

* `s`

### Wyjście

Jedna linia:

* `Prawda` — jeśli napis zawiera tylko cyfry
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
1234
```

**Wyjście:**

```
Prawda
```

*/

public class Main {

  public static boolean tylkoCyfryV1(String slowo) {

    for (char ch : slowo.toCharArray()) {
      if (!Character.isDigit(ch)) return false;
    }

    return true;
  }

  public static boolean tylkoCyfryV2(String slowo) {
    return slowo.matches("[0-9]+");
  }

  public static boolean tylkoCyfryV3(String slowo) {

    return !slowo.chars().anyMatch(n -> !Character.isDigit(n));
  }

  public static void test1() {

    final String napis = "12345";
    final boolean oczekiwane = true;

    final boolean wynik = tylkoCyfryV1(napis);

    assert wynik == oczekiwane;
  }

  public static void test2() {

    final String napis = "12345a";
    final boolean oczekiwane = false;

    final boolean wynik = tylkoCyfryV1(napis);

    assert wynik == oczekiwane;
  }

  public static void test3() {

    final String napis = "12345";
    final boolean oczekiwane = true;

    final boolean wynik = tylkoCyfryV2(napis);

    assert wynik == oczekiwane;
  }

  public static void test4() {

    final String napis = "12345a";
    final boolean oczekiwane = false;

    final boolean wynik = tylkoCyfryV2(napis);

    assert wynik == oczekiwane;
  }

  public static void test5() {

    final String napis = "12345";
    final boolean oczekiwane = true;

    final boolean wynik = tylkoCyfryV3(napis);

    assert wynik == oczekiwane;
  }

  public static void test6() {

    final String napis = "12345a";
    final boolean oczekiwane = false;

    final boolean wynik = tylkoCyfryV3(napis);

    assert wynik == oczekiwane;
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
    test4();
    test5();
    test6();
  }
}

