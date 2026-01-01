/*
ZAD-06 — Najmniejsza wspólna wielokrotność (NWW)

**Poziom:** ★☆☆
**Tagi:** `nww`, `nwd`, `arytmetyka`

### Treść

Napisz funkcję `nww(a, b)`, która zwraca najmniejszą wspólną wielokrotność liczb
`a` i `b`.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a > 0`)
* `b` (liczba naturalna, `b > 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `NWW(a, b)`.

### Przykład

**Wywołanie funkcji:**

```python
print(nww(7, 9))
```

**Wyjście:**

```
63
```

### Ograniczenia / gwarancje

* Możesz użyć zależności: `NWW(a, b) = (a * b) // NWD(a, b)`.

*/
#include <cassert>

int nwd(int a, int b) {
  int c;

  while (b != a % b) {
    c = b;
    b = a % b;
    a = c;

    if (b == 0) break;
  }

  return a;
}

int nww(int a, int b) { return a * b / nwd(a, b); }

void testNww() {
  assert(nww(12, 15) == 60);
  assert(nww(12, 16) == 48);
  assert(nww(12, 18) == 36);
}

int main() {
  testNww();

  return 0;
}
