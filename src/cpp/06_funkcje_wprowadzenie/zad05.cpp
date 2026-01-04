/*
ZAD-05 — Zamiana wartości miejscami

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `krotka`, `zmienne`

### Treść

Napisz funkcję `zamien_wartosci(a, b)`, która zamienia wartości miejscami i
zwraca je jako parę `(b, a)`.

### Wejście

Dwa argumenty: `a`, `b` (liczby naturalne)

### Wyjście

Dwie liczby naturalne zwrócone jako krotka / para:

* najpierw nowa wartość `a` (czyli stare `b`)
* potem nowa wartość `b` (czyli stare `a`)

### Przykład

**Wywołanie funkcji:**

```python
a, b = zamien_wartosci(8, 5)
print("a =", a)
print("b =", b)
```

**Wyjście:**

```
a = 5
b = 8
```

*/
#include <iostream>

void zamien(int &a, int &b) {
  int temp = a;
  a = b;
  b = temp;
}

int main() {
  int a, b;
  std::cin >> a >> b;

  zamien(a, b);

  std::cout << a << std::endl;
  std::cout << b << std::endl;

  return 0;
}
