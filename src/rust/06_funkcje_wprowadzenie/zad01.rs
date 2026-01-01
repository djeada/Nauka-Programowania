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

// Podpunkt a) zwraca liczbę 3
fn zwroc_liczbe() -> i32 {
    3
}

// Podpunkt b) zwraca napis "Tak"
fn zwroc_napis() -> &'static str {
    "Tak"
}

// Podpunkt c) zwraca wartość logiczną true
fn zwroc_prawda() -> bool {
    true
}

fn main() {
    println!("{}", zwroc_liczbe());
    println!("{}", zwroc_napis());
    println!("{}", zwroc_prawda());
}
