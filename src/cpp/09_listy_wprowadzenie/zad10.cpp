/*
ZAD-10 — Czy punkty mogą być wierzchołkami trójkąta?

**Poziom:** ★★☆
**Tagi:** `geometria`, `warunki`, `listy`

### Treść

Wczytaj współrzędne trzech punktów `A(xA, yA)`, `B(xB, yB)`, `C(xC, yC)`.
Wypisz `Tak`, jeśli punkty **nie są współliniowe** (mogą tworzyć trójkąt), w
przeciwnym razie `Nie`.

### Wejście

Sześć liczb całkowitych (każda w osobnej linii):

1. `xA`
2. `yA`
3. `xB`
4. `yB`
5. `xC`
6. `yC`

### Wyjście

Jedno słowo: `Tak` lub `Nie`.

### Przykład

**Wejście:**

```
-3
-2
-3
1
-3
0
```

**Wyjście:**

```
Nie
```

### Uwagi

* Sprawdź pole trójkąta: jeśli równe `0`, punkty są współliniowe.

*/
#include <cmath>
#include <iostream>

int main() {
  int xA, yA, xB, yB, xC, yC;
  std::cin >> xA >> yA >> xB >> yB >> xC >> yC;

  // Oblicz pole trójkąta
  double pole = abs((xB - xA) * (yC - yA) - (xC - xA) * (yB - yA)) / 2.0;

  std::cout << (pole == 0 ? "Tak" : "Nie") << std::endl;

  return 0;
}
