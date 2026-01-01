/*
ZAD-14 — Napis z liczb od 1 do n

**Poziom:** ★☆☆
**Tagi:** `pętle`, `string`

### Treść

Wczytaj `n` i wypisz napis złożony z kolejnych liczb od 1 do `n`, bez separatorów.

### Wejście

* 1. linia: liczba naturalna `n` (n ≥ 1)

### Wyjście

* 1. linia: ciąg `1..n` bez spacji

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
123
```

*/
public class Main {
  // Otrzymujesz liczbe n. Zwroc napis skladajacy
  // sie z liczb naturalnych od 1 do n.

  // Zlozonosc Czasowa: O(n * log(n))
  // Zlozonosc Pamieciowa: O(n * log(n))
  public static String liczby(int n) {
    String wynik = "";

    for (int i = 1; i <= n; i++) {
      wynik += String.valueOf(i);
    }

    return wynik;
  }

  public static void test1() {
    int n = 5;
    String wynik = "12345";
    assert wynik.equals(liczby(n));
  }

  public static void test2() {
    int n = -1;
    String wynik = "";
    assert wynik.equals(liczby(n));
  }

  public static void main(String[] args) {
    test1();
    test2();
  }
}

