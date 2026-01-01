/*
ZAD-08 — Naiwny test pierwszości liczby

**Poziom:** ★★☆
**Tagi:** `pierwszość`, `pętle`, `dzielniki`

### Treść

Napisz funkcję `czy_pierwsza(n)`, która zwraca `True`, jeśli `n` jest liczbą pierwszą, w przeciwnym razie `False`.

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 2`)

### Wyjście

Funkcja zwraca wartość logiczną:

* `True` lub `False`

### Przykład

**Wywołanie funkcji:**

```python
print(czy_pierwsza(7))
print(czy_pierwsza(4))
```

**Wyjście:**

```
True
False
```

### Uwagi

* Dla prostego rozwiązania możesz sprawdzać dzielniki od `2` do `n-1`.
* Dla szybszego rozwiązania możesz sprawdzać dzielniki do `⌊sqrt(n)⌋`.

*/
public class Main {
  // Napisz funkcje, ktora dla otrzymanej liczby sprawdzi
  // czy jest ona liczba pierwsza.

  public static boolean czyPierwsza(int n) {

    if (n <= 1) {
      return false;
    }

    if (n % 2 == 0 && n != 2) {
      return false;
    }

    for (int i = 3; i <= Math.sqrt((double) n); i += 2) {
      if (n % i == 0) {
        return false;
      }
    }

    return true;
  }

  public static void test1() {
    int a = 15;
    assert !czyPierwsza(a);
  }

  public static void test2() {
    int a = 7;
    assert czyPierwsza(a);
  }

  public static void test3() {
    int a = -15;
    assert !czyPierwsza(a);
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

