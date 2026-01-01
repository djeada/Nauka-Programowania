/*
ZAD-05A — Minimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Wypisz mniejszą z nich **bez użycia instrukcji warunkowych** (`if`, `?:`) i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `min(a, b)`.

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

ZAD-05B — Maksimum bez instrukcji warunkowych

**Poziom:** ★★☆
**Tagi:** `bit-trick`, `min/max`, `bez if`

### Treść

Wczytaj `a` i `b`. Wypisz większą z nich **bez użycia instrukcji warunkowych** i bez bibliotek.

### Wejście

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Jedna liczba naturalna: `max(a, b)`.

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
3
```

*/

// Funkcja zwracajaca mniejsza z dwoch liczb
function minimum(a, b) {
  return (a + b - Math.abs(a - b)) / 2;
}

// Funkcja zwracajaca wieksza z dwoch liczb
function maximum(a, b) {
  return (a + b + Math.abs(a - b)) / 2;
}

function test() {
  console.assert(minimum(3, 2) === 2, "Test 1 nie powiodl sie");
  console.assert(maximum(3, 2) === 3, "Test 2 nie powiodl sie");
  console.assert(minimum(5, 5) === 5, "Test 3 nie powiodl sie");
  console.assert(maximum(5, 5) === 5, "Test 4 nie powiodl sie");
}

test();

