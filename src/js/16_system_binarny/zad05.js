/*
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby całkowite `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `min`, `max`, `abs`, `sorted`.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba całkowita: mniejsza z liczb `a` i `b` (gdy są równe — ich wspólna wartość).

### Ograniczenia

* $-10^9 \le a, b \le 10^9$ — w tym zadaniu liczby **mogą być ujemne**

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
2
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe.
* Wskazówka: dla `d = a - b` wyrażenie `d >> 63` daje `-1` (same jedynki w zapisie binarnym), gdy `d < 0`, oraz `0`, gdy `d ≥ 0`. Wtedy `d & (d >> 63)` jest równe `d` albo `0`.
* Tą samą sztuczką otrzymasz maksimum: `a - (d & (d >> 63))`.

ZAD-05B — Wartość bezwzględna bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `maski`, `bez if`

### Treść

Wczytaj liczbę całkowitą `x` i wypisz jej wartość bezwzględną $|x|$ **bez użycia instrukcji warunkowych** (`if`, wyrażenia `x if warunek else y`) i bez funkcji `abs`, `min`, `max`, `sorted`.

### Wejście

* 1. linia: `x`

### Wyjście

Jedna liczba naturalna: $|x|$.

### Ograniczenia

* $-10^9 \le x \le 10^9$ — liczba **może być ujemna**

### Przykład

**Wejście:**

```
-12
```

**Wyjście:**

```
12
```

### Uwagi

* Dopuszczalne są operacje arytmetyczne i bitowe; porównania (`<`, `>`) nie są potrzebne.
* Tak jak w ZAD-05A, **maska znaku** `m = x >> 63` jest równa `-1` (same jedynki), gdy `x < 0`, oraz `0`, gdy `x ≥ 0`.
* XOR z maską `0` nic nie zmienia, a XOR z maską `-1` odwraca wszystkie bity, czyli daje $-x - 1$ (tak liczby ujemne zapisuje kod uzupełnień do dwóch). Wystarczy więc obliczyć `(x ^ m) - m`.

*/
function minimum(a, b) {
  return (a + b - Math.abs(a - b)) / 2;
}

// ZAD-05B: wartosc bezwzgledna bez instrukcji warunkowych.
// Maska znaku m = x >> 31 (operatory bitowe JS dzialaja na 32 bitach):
// -1 dla x < 0, 0 dla x >= 0; (x ^ m) - m to x albo -x.
function wartoscBezwzgledna(x) {
  const maska = x >> 31;
  return (x ^ maska) - maska;
}

function test() {
  console.assert(minimum(3, 2) === 2, "Test 1 nie powiodl sie");
  console.assert(wartoscBezwzgledna(-12) === 12, "Test 2 nie powiodl sie");
  console.assert(minimum(5, 5) === 5, "Test 3 nie powiodl sie");
  console.assert(wartoscBezwzgledna(0) === 0, "Test 4 nie powiodl sie");
  console.assert(
    wartoscBezwzgledna(-1000000000) === 1000000000,
    "Test 5 nie powiodl sie",
  );
}

test();
