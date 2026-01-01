/*
ZAD-03 — Pierwsze wystąpienie klucza

**Poziom:** ★☆☆
**Tagi:** `listy`, `wyszukiwanie`, `indeksy`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `klucz`. Wypisz indeks pierwszego wystąpienia `klucz` w liście.
Jeśli `klucz` nie występuje — wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna liczba całkowita — indeks (od `0`) lub `-1`.

### Przykład

**Wejście:**

```
5
2
9
-1
3
8
-1
```

**Wyjście:**

```
2
```

*/
import java.util.stream.IntStream;

public class Main {

  public static int znajdzKluczV1(int[] tablica, int klucz) {

    for (int i = 0; i < tablica.length; i++) if (tablica[i] == klucz) return i;

    return -1;
  }

  public static int znajdzKluczV2(int[] tablica, int klucz) {

    return IntStream.range(0, tablica.length)
        .filter(i -> klucz == tablica[i])
        .findFirst()
        .orElse(-1);
  }

  private static void test1() {
    int[] tablica = new int[] {3, 5, -7, 4, 9, -11, 2};
    int klucz = 2;
    int wynik = 6;

    assert znajdzKluczV1(tablica, klucz) == wynik;
    assert znajdzKluczV2(tablica, klucz) == wynik;
  }

  private static void test2() {
    int[] tablica = new int[] {3, -2, 4, 9, -3, -40, 8, 5, -7, -1};
    int klucz = 2;
    int wynik = -1;

    assert znajdzKluczV1(tablica, klucz) == wynik;
    assert znajdzKluczV2(tablica, klucz) == wynik;
  }

  public static void main(String[] args) {

    test1();
    test2();
  }
}

