/*
ZAD-09A — Wielkie → małe (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `string`

### Treść

Wczytaj napis. Zamień wszystkie wielkie litery alfabetu łacińskiego (`A–Z`) na małe, używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)

### Wyjście

Jedna linia: napis po zamianie.

### Ograniczenia

* napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
test
```

### Uwagi

* Kody wielkiej i małej litery różnią się tylko bitem o wartości 32 (`0b100000`): `ord("A")` to `65`, a `ord("a")` to `97`. Ustawienie tego bitu: `ord(znak) | 32`.
* Zmieniaj tylko litery `A–Z` — np. `@` i `[` sąsiadują w tablicy ASCII z literami, ale mają pozostać bez zmian.
* Odwrotną zamianę (małe → wielkie) daje wyzerowanie tego bitu: `ord(znak) & ~32`.

ZAD-09B — Numer litery w alfabecie (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `maski`

### Treść

Wczytaj słowo złożone z liter alfabetu łacińskiego. Dla każdej litery wyznacz jej numer w alfabecie — `a` i `A` mają numer `1`, `b` i `B` numer `2`, …, `z` i `Z` numer `26` — używając operacji bitowej na kodzie ASCII zamiast porównań i odejmowania.

### Wejście

* 1. linia: słowo

### Wyjście

Jedna linia: numery kolejnych liter słowa oddzielone pojedynczymi spacjami.

### Ograniczenia

* słowo ma od 1 do 100 znaków i składa się wyłącznie z liter `a–z` i `A–Z`

### Przykład

**Wejście:**

```
Bit
```

**Wyjście:**

```
2 9 20
```

### Uwagi

* Zapisz kody binarnie: `ord("A")` to $65 = 1000001_2$, a `ord("a")` to $97 = 1100001_2$. Pięć najniższych bitów kodu każdej litery to właśnie jej numer w alfabecie — i to niezależnie od wielkości litery.
* Pięć najniższych bitów wydobędziesz **maską** $31 = 11111_2$: `ord(znak) & 31`. Operacja `&` z maską zeruje wszystkie bity poza tymi, które w masce są jedynkami.

ZAD-09C — Odwróć wielkość liter (bitowo)

**Poziom:** ★★☆
**Tagi:** `ASCII`, `bitwise`, `toggle case`

### Treść

Wczytaj napis. Zamień wielkość każdej litery alfabetu łacińskiego na przeciwną (mała ↔ wielka), używając operacji bitowych na kodach ASCII. Pozostałe znaki pozostaw bez zmian.

### Wejście

* 1. linia: napis (może zawierać spacje, cyfry i znaki interpunkcyjne)

### Wyjście

Jedna linia: napis po zmianie.

### Ograniczenia

* napis ma od 1 do 100 znaków i składa się wyłącznie ze znaków ASCII (bez polskich liter)

### Przykład

**Wejście:**

```
Test
```

**Wyjście:**

```
tEST
```

### Uwagi

* Odwrócenie bitu o wartości 32: `ord(znak) ^ 32`. Stosuj je tylko do liter `a–z` i `A–Z`.

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

  // b) Numery liter w alfabecie: piec najnizszych bitow kodu ASCII litery.
  public static String numeryLiter(String slowo) {
    StringBuilder wynik = new StringBuilder();

    for (int i = 0; i < slowo.length(); i++) {
      if (i > 0) {
        wynik.append(' ');
      }
      wynik.append(slowo.charAt(i) & 0b11111);
    }

    return wynik.toString();
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
    String slowo = "Bit";
    String wynik = "2 9 20";

    assert wynik.equals(numeryLiter(slowo));
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

