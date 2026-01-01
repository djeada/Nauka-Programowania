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
#include <iostream>
#include <string>

// ZAD-01A
int zwroc3() { return 3; }

// ZAD-01B
std::string zwrocTak() { return "Tak"; }

// ZAD-01C
bool zwrocTrue() { return true; }

int main() {
  std::cout << zwroc3() << std::endl;
  std::cout << zwrocTak() << std::endl;
  std::cout << (zwrocTrue() ? "True" : "False") << std::endl;

  return 0;
}
