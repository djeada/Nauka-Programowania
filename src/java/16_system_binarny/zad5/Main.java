/*
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, `?:`) i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `min(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
2
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe.

ZAD-05B — Maksimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj `a` i `b`. Wypisz większą z nich **bez użycia instrukcji warunkowych** i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `max(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
3
```

*/
public class Main {
  // Znajdz min/maks dwoch liczb bez uzycia instrukcji warunkowej.

  // Zlozonosc Czasowa: O(1)
  // Zlozonosc Pamieciowa: O(1)
  public static int znak(int n) {

    return (n >> 31) & 0x01;
  }

  // a >= b : znakA = 1, znakB = 0;
  // a<b : znakA = 0, znakB = 1;
  // Zlozonosc Czasowa: O(1)
  // Zlozonosc Pamieciowa: O(1)
  public static int maks(int a, int b) {
    int znakB = znak(a - b);
    int znakA = znakB ^ 1;
    return znakA * a + znakB * b;
  }

  public static int min(int a, int b) {
    int znakB = znak(a - b);
    int znakA = znakB ^ 1;
    return znakB * a + znakA * b;
  }

  public static void test1() {
    int a = 10;
    int b = 8;
    int wynik = a;

    assert maks(a, b) == wynik;
  }

  public static void test2() {
    int a = 10;
    int b = 8;
    int wynik = b;

    assert min(a, b) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

