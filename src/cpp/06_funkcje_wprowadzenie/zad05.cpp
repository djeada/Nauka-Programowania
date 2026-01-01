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
#include <cassert>

void swap(int &pierwszaLiczba, int &drugaLiczba) {
  int c = pierwszaLiczba;
  pierwszaLiczba = drugaLiczba;
  drugaLiczba = c;
}

void testSwap() {
  int pierwszaLiczba = 1;
  int drugaLiczba = 2;
  swap(pierwszaLiczba, drugaLiczba);
  assert(pierwszaLiczba == 2);
  assert(drugaLiczba == 1);
}

int main() {
  testSwap();

  return 0;
}
