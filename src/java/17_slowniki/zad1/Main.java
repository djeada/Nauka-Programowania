/*
ZAD-01 — Słownik: liczby i ich kwadraty

**Poziom:** ★☆☆
**Tagi:** `dict`, `pętla`

### Treść

Wczytaj liczbę `n`. Utwórz słownik, gdzie klucze to liczby od `1` do `n-1`, a wartości to ich kwadraty.

### Wejście

* 1 linia: `n` (n ≥ 1)

### Wyjście

* Słownik w postaci: `{1: 1, 2: 4, ...}`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
{1: 1, 2: 4, 3: 9, 4: 16}
```

*/
import java.util.*;

public class Main {
  // Otrzymujesz liczbe naturalna. Zbuduj slownik skladajacy sie
  // z kluczy bedacych kolejnymi liczbami naturalnymi mniejszymi
  // od otrzymanej liczby oraz wartosci bedacych kwadratami swoich kluczy.

  // Zlozonosc Czasowa: O(n)
  // Zlozonosc Pamieciowa: O(n)
  public static HashMap<Integer, Integer> budujSlownik(int liczba) {
    HashMap<Integer, Integer> slownik = new HashMap<Integer, Integer>();

    for (int i = 1; i < liczba; i++) {
      slownik.put(i, (int) Math.pow(i, 2));
    }

    return new HashMap<Integer, Integer>(slownik);
  }

  public static void test1() {
    int liczba = 5;
    HashMap<Integer, Integer> wynik =
        new HashMap<Integer, Integer>(
            Map.ofEntries(Map.entry(1, 1), Map.entry(2, 4), Map.entry(3, 9), Map.entry(4, 16)));

    assert wynik.equals(budujSlownik(liczba));
  }

  public static void test2() {
    int liczba = -1;
    HashMap<Integer, Integer> wynik = new HashMap<Integer, Integer>();

    assert wynik.equals(budujSlownik(liczba));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

