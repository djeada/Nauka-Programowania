/*
ZAD-17 — Konwersja listy na napis

**Poziom:** ★☆☆
**Tagi:** `list`, `string`

### Treść

Otrzymujesz listę liczb naturalnych w zapisie tekstowym (np. `[2, 4, 7]`). Połącz liczby bez separatorów i wypisz jako napis.

### Wejście

* 1. linia: lista w formacie podobnym do Pythona, np. `[2, 4, 7]`

### Wyjście

* 1. linia: napis z połączonych liczb, np. `247`

### Przykład

**Wejście:**

```
[2, 4, 7]
```

**Wyjście:**

```
247
```

### Uwagi

* Najprościej: usuń nawiasy `[` `]`, rozdziel po przecinkach, `strip()`, potem sklej.

*/
import java.util.*;

public class Main {
  // Otrzymujesz liste liczb.
  // Zamien liste na napis.

  public static String liczby(final ArrayList<Integer> lista) {
    String wynik = "";

    for (var liczba : lista) {
      wynik += String.valueOf(liczba);
    }

    return wynik;
  }

  public static void test1() {
    ArrayList<Integer> lista = new ArrayList<Integer>(Arrays.asList(2, 4, 7));
    String wynik = "247";
    assert wynik.equals(liczby(lista));
  }

  public static void test2() {
    ArrayList<Integer> lista = new ArrayList<Integer>();
    String wynik = "";
    assert wynik.equals(liczby(lista));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

