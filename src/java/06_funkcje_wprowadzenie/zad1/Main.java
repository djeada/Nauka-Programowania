/*
ZAD-01A — Zwracanie stałej wartości: liczba 3

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `int`

### Treść

Napisz funkcję (bez argumentów), która zwraca liczbę całkowitą `3`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `3`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_liczbe()
print(wynik)
```

**Wyjście:**

```
3
```

ZAD-01B — Zwracanie stałej wartości: napis „Tak”

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `string`

### Treść

Napisz funkcję (bez argumentów), która zwraca napis `Tak`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `Tak`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_napis()
print(wynik)
```

**Wyjście:**

```
Tak
```

ZAD-01C — Zwracanie stałej wartości: True

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `return`, `bool`

### Treść

Napisz funkcję (bez argumentów), która zwraca wartość logiczną `True`.

### Wejście

Brak.

### Wyjście

Funkcja ma zwrócić:

* `True`

### Przykład

**Wywołanie funkcji:**

```python
wynik = zwroc_prawda()
print(wynik)
```

**Wyjście:**

```
True
```

*/
public class Main {
  // Napisz funkcje ktora zwroci
  // a) liczbe 3

  public static int funkcja1() {
    return 3;
  }

  // b) napis "Tak"
  public static String funkcja2() {
    return "Tak";
  }

  // c) wartosc logiczna prawda
  public static boolean funkcja3() {
    return true;
  }

  public static void test1() {
    assert funkcja1() == 3;
  }

  public static void test2() {
    assert funkcja2().equals("Tak");
  }

  public static void test3() {
    assert funkcja3();
  }

  public static void main(String[] args) {

    test1();
    test2();
    test3();
  }
}

