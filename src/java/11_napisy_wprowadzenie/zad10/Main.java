/*
ZAD-10 — Najdłuższe i najkrótsze słowo

**Poziom:** ★☆☆
**Tagi:** `string`, `min/max`, `len`

### Treść

Wczytaj zdanie i znajdź:

a) najdłuższe słowo,
b) najkrótsze słowo.

Jeśli jest remis, wybierz słowo, które występuje wcześniej.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: najdłuższe słowo
* 2. linia: najkrótsze słowo

### Przykład

**Wejście:**

```
Kaczka lubi wiosnę.
```

**Wyjście:**

```
Kaczka
lubi
```

*/
import java.util.*;

public class Main {
  // Otrzymujesz napis reprezuntajacy zdanie.
  // Znajdz najdluzsze oraz najkrotsze slowo w zdaniu.
  // Jesli wiecej niz jedno slowo ma ekstremalna dlugosc,
  // zwroc te, ktore wystepuje w zdaniu jako pierwsze.
  // Znaki interpunkcyjne nie sa liczone jako slowa.

  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n)
  public static String wyczysc(String napis) {
    napis = napis.trim();

    return napis.replaceAll("\\p{Punct}", "");
  }

  public static String najdluzsze(String napis) {
    String wynik = null;
    int dlugosc = 0;
    int pocz = 0;
    int konc = 0;
    while ((konc = napis.indexOf(' ', pocz)) != -1) {
      if (konc != pocz) {
        var slowo = napis.substring(pocz, konc);
        slowo = wyczysc(slowo);

        if (slowo.length() > dlugosc) {
          wynik = slowo;
          dlugosc = slowo.length();
        }
      }
      pocz = konc + 1;
    }
    if (konc != pocz) {
      var slowo = napis.substring(pocz);
      slowo = wyczysc(slowo);
      if (slowo.length() > dlugosc) {
        wynik = slowo;
        dlugosc = slowo.length();
      }
    }

    return wynik;
  }

  public static String najkrotsze(String napis) {
    String wynik = null;
    int dlugosc = napis.length();
    int pocz = 0;
    int konc = 0;
    while ((konc = napis.indexOf(' ', pocz)) != -1) {
      if (konc != pocz) {
        var slowo = napis.substring(pocz, konc);
        slowo = wyczysc(slowo);

        if (slowo.length() < dlugosc) {
          wynik = slowo;
          dlugosc = slowo.length();
        }
      }
      pocz = konc + 1;
    }
    if (konc != pocz) {
      var slowo = napis.substring(pocz);
      slowo = wyczysc(slowo);
      if (slowo.length() < dlugosc) {
        wynik = slowo;
        dlugosc = slowo.length();
      }
    }

    return wynik;
  }

  public static void test1() {
    String napis = "Kaczka lubi wiosne.";
    String wynik = "Kaczka";
    assert wynik.equals(najdluzsze(napis));
  }

  public static void test2() {
    String napis = "Kaczka lubi wiosne.";
    String wynik = "lubi";
    assert wynik.equals(najkrotsze(napis));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

