/*
ZAD-05A — Funkcja liniowa: y = 3x + 10

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`, `formatowanie`

### Wejście

1 liczba: `x` (może być całkowita lub zmiennoprzecinkowa)

### Wyjście

1 liczba: `y` wypisana z dokładnością do **3 miejsc po przecinku**.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
19.000
```

ZAD-05B — Funkcja liniowa: y = ax + b

**Poziom:** ★★☆
**Tagi:** `arytmetyka`, `float`

### Wejście

3 liczby (każda w osobnej linii): `a`, `b`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Przykład

**Wejście:**

```
1
2
3
```

**Wyjście:**

```
5.000
```

ZAD-05C — Funkcja sześcienna: y = x³ + 2

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Treść

Oblicz: `y = x^3 + 22 - 20`, czyli równoważnie `y = x^3 + 2`.

### Wejście

1 liczba: `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
127.000
```

ZAD-05D — Wielomian z potęgami: y = a·x^m + b·x^n + c − a

**Poziom:** ★★☆
**Tagi:** `potęgi`, `float`

### Wejście

6 liczb (w osobnych liniach): `a`, `b`, `c`, `m`, `n`, `x`

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* `m` i `n` są liczbami całkowitymi (np. nieujemnymi), aby potęgowanie było
jednoznaczne w typowych językach.

### Przykład

**Wejście:**

```
1
1
1
1
1
1
```

**Wyjście:**

```
2.000
```

ZAD-05E — Funkcja z trygonometrią, wykładniczą i logarytmem

**Poziom:** ★★★☆
**Tagi:** `math`, `trygonometria`, `log`, `exp`, `float`

### Treść

Dla `x` (w radianach) oblicz:
[
y=\sin^3(x)\cdot\cos^2(x)+e^{x^2}+\ln(x^3+2x^2-x-3)
]

### Wejście

1 liczba zmiennoprzecinkowa: `x` (w radianach)

### Wyjście

`y` do 3 miejsc po przecinku.

### Ograniczenia / gwarancje

* Dane testowe spełniają warunek dziedziny logarytmu:

  * (x^3+2x^2-x-3 > 0)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
57.179
```

*/
#include <cmath>
#include <iostream>

int main() {
  std::cout << "podaj x" << std::endl;
  int x;
  std::cin >> x;

  std::cout << "3*x+10" << std::endl;
  std::cout << 3 * x + 10 << std::endl;

  std::cout << "podaj a" << std::endl;
  int a;
  std::cin >> a;

  std::cout << "podaj b" << std::endl;
  int b;
  std::cin >> b;

  std::cout << "podaj x" << std::endl;
  std::cin >> x;

  std::cout << "a*x+b" << std::endl;
  std::cout << a * x + b << std::endl;

  std::cout << "podaj x" << std::endl;
  std::cin >> x;

  std::cout << "y = x**3 + 2x**2 - 20" << std::endl;
  std::cout << pow(x, 3) + 2 * pow(x, 2) - 20 << std::endl;

  std::cout << "podaj a" << std::endl;
  std::cin >> a;

  std::cout << "podaj b" << std::endl;
  std::cin >> b;

  std::cout << "podaj c" << std::endl;
  int c;
  std::cin >> c;

  std::cout << "podaj d" << std::endl;
  int d;
  std::cin >> d;

  std::cout << "podaj m" << std::endl;
  int m;
  std::cin >> m;

  std::cout << "podaj n" << std::endl;
  int n;
  std::cin >> n;

  std::cout << "podaj x" << std::endl;
  std::cin >> x;

  std::cout << "a*x**m + b*x**n + c - a" << std::endl;
  std::cout << a * pow(x, m) + b * pow(x, n) + c - a << std::endl;

  std::cout << "podaj x" << std::endl;

  std::cin >> x;

  std::cout << "sin(3*x)*cos(2*X) + e**x**2 + log(x**3 + 2*x**2 - x - 3)"
            << std::endl;
  std::cout << sin(3 * x) * cos(2 * x) + exp(pow(x, 2)) +
                   log(pow(x, 3) + 2 * pow(x, 2) - x - 3)
            << std::endl;

  return 0;
}
