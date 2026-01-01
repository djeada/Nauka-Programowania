/*
ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis z liter alfabetu łacińskiego. Zamień wszystkie wielkie litery na małe, używając operacji bitowych na kodach ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

ZAD-09B — Małe → wielkie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie małe litery na wielkie, używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po konwersji.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
TEST
```

ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery na przeciwną (mała↔wielka) używając operacji bitowych na ASCII.

### Wejście

* 1. linia: napis

### Wyjście

Jedna linia: napis po zmianie.

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

*/
public class Main {
  // Przy uzyciu operatorow bitowych:
  // a) Zamien wielkie litery na male.
  
  // Zlozonosc Czasowa: O(n), gdzie n to dlugosc napisu
  // Zlozonosc Pamieciowa: O(n)
  public static String wielkieNaMale(String slowo) {
    String wynik = "";

    for (int litera : slowo.toCharArray()) {
      wynik += (char) (litera | (int) ' ');
    }

    return wynik;
  }

  // b) Zamien male litery na wielkie.
  public static String maleNaWielkie(String slowo) {
    String wynik = "";

    for (int litera : slowo.toCharArray()) {
      wynik += (char) (litera & (int) '_');
    }

    return wynik;
  }

  // c) Zamien male litery na wielkie i wielkie na male.
  public static String odwrocWielkoscLiter(String slowo) {

    String wynik = "";

    for (int litera : slowo.toCharArray()) {

      if (litera >= 'a' && litera <= 'z') {
        wynik += (char) (litera ^ (int) ' ');
      } else if (litera >= 'A' && litera <= 'Z') {
        wynik += (char) (litera ^ (int) ' ');
      } else {
        wynik += (char) litera;
      }
    }

    return wynik;
  }

  public static void test1() {
    String slowo = "KURCZAKU";
    String wynik = "kurczaku";

    assert wynik.equals(wielkieNaMale(slowo));
  }

  public static void test2() {
    String slowo = "piesek";
    String wynik = "PIESEK";

    assert wynik.equals(maleNaWielkie(slowo));
  }

  public static void test3() {
    String slowo = "wszedl Kotek na PloteK i mrUga";
    String wynik = "WSZEDL kOTEK NA pLOTEk I MRuGA";

    assert wynik.equals(odwrocWielkoscLiter(slowo));
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

