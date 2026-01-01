/*
ZAD-06 — Konwersja między dowolnymi systemami (2..36)

**Poziom:** ★★☆
**Tagi:** `konwersja`, `base`, `string`

### Treść

Wczytaj:

1. liczbę `X` zapisaną w systemie o podstawie `p`
2. podstawę `p` (2..36)
3. podstawę docelową `q` (2..36)

i wypisz reprezentację `X` w systemie o podstawie `q`.

### Wejście

Trzy linie:

1. `X` (zapis liczby; dla podstaw >10 może zawierać litery `A-Z`)
2. `p` (2..36)
3. `q` (2..36)

### Wyjście

Jedna linia: zapis liczby w systemie o podstawie `q` (używaj `0–9` i `A–Z`).

### Przykład

**Wejście:**

```
4301
10
4
```

**Wyjście:**

```
1003031
```

### Uwagi o formacie

* `X` może być duże — traktuj jako napis, a nie typ int „na wejściu”.
* Dla wartości 10..35 stosuj `A..Z`.

*/
public class Main {
  // Konwersja miedzy dowolnymi systemami liczbowymi.
  
  // Zlozonosc Czasowa: O(n), gdzie n to dlugosc napisu
  // Zlozonosc Pamieciowa: O(1)
  public static int naDec(String liczba, int podstawa) {
    int wartoscDec = 0;

    for (int i = liczba.length() - 1; i >= 0; i--) {

      if (liczba.charAt(i) >= 'A' && liczba.charAt(i) < 'Z') {
        wartoscDec += (liczba.charAt(i) - 'A' + 10) * Math.pow(podstawa, (liczba.length() - 1 - i));
      } else {
        wartoscDec += (liczba.charAt(i) - '0') * Math.pow(podstawa, (liczba.length() - 1 - i));
      }
    }

    return wartoscDec;
  }

  public static String zmianaPodstawy(String liczba, int podstawa, int nowaPodstawa) {

    if (podstawa > (10 + 'Z' - 'A')) {
      return "";
    }

    int wartoscDec = naDec(liczba, podstawa);
    podstawa = nowaPodstawa;
    liczba = "";

    while (wartoscDec > 0) {
      int reszta = wartoscDec % podstawa;
      wartoscDec /= podstawa;

      char nowyZnak = (char) ('0' + reszta);

      if (nowyZnak > '9') {
        nowyZnak = (char) ('A' + (nowyZnak - '9') - 1);
      }

      liczba += nowyZnak;
    }

    return new StringBuilder(liczba).reverse().toString();
  }

  public static void test1() {
    String liczba = "4301";
    String wynik = "1003031";

    assert wynik.equals(zmianaPodstawy(liczba, 10, 4));
  }

  public static void main(String[] args) {

    test1();
  }
}

