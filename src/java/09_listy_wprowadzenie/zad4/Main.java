/*
ZAD-04 — Minimum oraz maksimum

**Poziom:** ★☆☆
**Tagi:** `listy`, `min`, `max`

### Treść

Wczytaj `N` liczb całkowitych. Wypisz:

1. największą liczbę w liście
2. najmniejszą liczbę w liście

w jednej linii, oddzielone pojedynczą spacją.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite

### Wyjście

Jedna linia:

* `max min`

### Przykład

**Wejście:**

```
9
4
-7
8
5
6
-9
10
2
-8
```

**Wyjście:**

```
10 -9
```

*/

public class Main {

  public static int znajdzMaksV1(int[] tablica) {

    int maks = tablica[0];

    for (int elem : tablica) if (elem > maks) maks = elem;

    return maks;
  }

  public static int znajdzMaksV2(int[] tablica) {

    int maks = tablica[0];

    for (int elem : tablica) maks = Math.max(maks, elem);

    return maks;
  }

  private static void test1() {
    int[] tablica = new int[] {3, 5, -7, 4, 9, -11, 2};
    int wynik = 9;

    assert znajdzMaksV1(tablica) == wynik;
    assert znajdzMaksV2(tablica) == wynik;
  }

  private static void test2() {
    int[] tablica = new int[] {3, -2, 4, 29, -3, -40, 8, 5, -7, -1};
    int wynik = 29;

    assert znajdzMaksV1(tablica) == wynik;
    assert znajdzMaksV2(tablica) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

