/*
ZAD-02 — Usuń podnapis

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Dostajesz dwa napisy:

1. Napis główny,
2. Podnapis do usunięcia.

Usuń **wszystkie wystąpienia** podnapisu z napisu głównego.

### Wejście

* 1 linia: napis `S`
* 2 linia: napis `T` (do usunięcia)

### Wyjście

* 1 linia: wynikowy napis po usunięciu wszystkich wystąpień

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
```

**Wyjście:**

```
Le je na wie
```

*/
import java.util.*;

public class Main {

  // Usuwa wszystkie wystąpienia napis2 z napis1
  // Złożoność czasowa: O(n*m*k) gdzie n to długość napis1, m to długość napis2, k to liczba wystąpień
  // Złożoność pamięciowa: O(n)
  public static String usunWystapienia(String napis1, String napis2) {
    String wynik = napis1;

    while (wynik.contains(napis2)) {
      int indeks = wynik.indexOf(napis2);
      wynik = wynik.substring(0, indeks) + wynik.substring(indeks + napis2.length());
    }

    return wynik;
  }

  public static void test1() {
    String napis1 = "Lezy jezy na wiezy";
    String napis2 = "zy";
    String wynik = "Le je na wie";

    assert (usunWystapienia(napis1, napis2).equals(wynik));
  }

  public static void main(String[] args) {

    test1();
  }
}

