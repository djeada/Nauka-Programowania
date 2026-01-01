/*
ZAD-12 — Usuń spacje ze zdania

**Poziom:** ★☆☆
**Tagi:** `replace`, `string`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie bez spacji

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Alamakota
```

*/

public class Main {

  public static String usunSpacjeV1(String zdanie) {
    return zdanie.replaceAll("\\s", "");
  }

  public static void main(String[] args) {

    String zdanie = "lezy jezy na wierzy";
    String wynik = "lezyjezynawierzy";

    assert usunSpacjeV1(zdanie).equals(wynik);

    zdanie = "d";
    wynik = "d";

    assert usunSpacjeV1(zdanie).equals(wynik);
  }
}

