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

* `m` i `n` są liczbami całkowitymi (np. nieujemnymi), aby potęgowanie było jednoznaczne w typowych językach.

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
const x1 = parseFloat(prompt("Podaj wspolrzedna x:"));
console.log((3 * x1 + 10).toFixed(3));

// b) Pobierz wspolczynniki $a$, $b$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax + b$ w tym punkcie.
const a2 = parseFloat(prompt("Podaj wspolczynnik a:"));
const b2 = parseFloat(prompt("Podaj wspolczynnik b:"));
const x2 = parseFloat(prompt("Podaj wspolrzedna x:"));
console.log((a2 * x2 + b2).toFixed(3));

// c) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = x^3 + 22 - 20$ w tym punkcie.
const x3 = parseFloat(prompt("Podaj wspolrzedna x:"));
console.log((x3 ** 3 + 2).toFixed(3));

// d) Pobierz wspolczynniki $a$, $b$, $c$, $m$, $n$ oraz punkt $x$. Wyznacz wartosc funkcji $y = ax^m + bx^n + c - a$ w tym punkcie.
const a4 = parseFloat(prompt("Podaj wspolczynnik a:"));
const b4 = parseFloat(prompt("Podaj wspolczynnik b:"));
const c4 = parseFloat(prompt("Podaj wspolczynnik c:"));
const m4 = parseFloat(prompt("Podaj wspolczynnik m:"));
const n4 = parseFloat(prompt("Podaj wspolczynnik n:"));
const x4 = parseFloat(prompt("Podaj wspolrzedna x:"));
console.log((a4 * x4 ** m4 + b4 * x4 ** n4 + c4 - a4).toFixed(3));

// e) Otrzymujesz wspolrzedna $x$. Wyznacz wartosc funkcji $y = sin^3(x) \cdot cos^2(x) + e^(x^2) + log(x^3 + 2x^2 - x - 3)$ w tym punkcie.
const x5 = parseFloat(prompt("Podaj wspolrzedna x:"));
console.log(
  (Math.sin(x5) ** 3 * Math.cos(x5) ** 2 +
    Math.exp(x5 ** 2) +
    Math.log(x5 ** 3 + 2 * x5 ** 2 - x5 - 3)).toFixed(3)
);

