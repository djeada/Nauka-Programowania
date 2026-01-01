/*
ZAD-10 — Ile bitów trzeba odwrócić (A → B)

**Poziom:** ★★☆
**Tagi:** `XOR`, `popcount`, `bitwise`

### Treść

Wczytaj dwie liczby naturalne `A` i `B`. Oblicz, ile bitów trzeba odwrócić w `A`, aby otrzymać `B`.

### Wejście

* 1. linia: `A`
* 2. linia: `B`

### Wyjście

Jedna liczba naturalna: liczba różniących się bitów.

### Przykład

**Wejście:**

```
34
73
```

**Wyjście:**

```
5
```

*/
public class Main {
  // Policz ile bitow nalezy odwrocic,
  // aby zamien liczbe A w liczbe B.

  // Zlozonosc Czasowa: O(log n)
  // Zlozonosc Pamieciowa: O(1)
  public static int bityDoZmiany(int liczbaA, int liczbaB) {

    int n = liczbaA ^ liczbaB;

    int licznik = 0;
    while (n != 0) {
      n &= (n - 1);
      licznik++;
    }

    return licznik;
  }

  public static void test1() {
    int liczbaA = 34;
    int liczbaB = 73;
    int wynik = 5;

    assert bityDoZmiany(liczbaA, liczbaB) == wynik;
  }

  public static void main(String[] args) {

    test1();
  }
}

