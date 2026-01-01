/*
ZAD-07 — Zamień znaki na kody ASCII

**Poziom:** ★☆☆
**Tagi:** `ASCII`, `ord`, `string`

### Treść

Wczytaj napis i wypisz kody ASCII wszystkich jego znaków, oddzielone przecinkiem i spacją `", "`.

### Wejście

* 1. linia: napis

### Wyjście

* 1. linia: kody ASCII oddzielone `, `

### Przykład

**Wejście:**

```
Robot
```

**Wyjście:**

```
82, 111, 98, 111, 116
```

*/
public class Main {
  // Otrzymujesz napis. Zamien wszystkie znaki napisu
  // na odpowiadajace im numery w tablicy ASCII. Podmien
  // otrzymany napis na uzyskane numery oddzielone przecinkami.

  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n)
  public static String zamienV1(String napis) {

    if (napis.length() == 0) {
      return "";
    }

    String wynik = "";

    for (int numer : napis.toCharArray()) {
      wynik += String.valueOf(numer) + ", ";
    }

    return wynik.substring(0, wynik.length() - 2);
  }

  public static void test1() {
    String napis = "pacZka!";
    String wynik = "112, 97, 99, 90, 107, 97, 33";

    assert zamienV1(napis).equals(wynik);
  }

  public static void test2() {
    String napis = "";
    String wynik = "";

    assert zamienV1(napis).equals(wynik);
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

