/*
ZAD-07 — Pierwiastek metodą Newtona (Herona)

**Poziom:** ★★☆
**Tagi:** `Newton`, `float`, `pętle`, `dokładność`

### Treść

Napisz funkcję `pierwiastek(n)`, która dla `n ≥ 0` zwraca przybliżenie `sqrt(n)` metodą Newtona:

[
x_{k+1} = \frac{1}{2}\left(x_k + \frac{n}{x_k}\right)
]

Iteruj do momentu, aż:
[
|x_{k+1} - x_k| < 0.0001
]

### Wejście

Jeden argument funkcji:

* `n` (liczba naturalna, `n ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę zmiennoprzecinkową — przybliżony pierwiastek z `n`.

### Przykład

**Wywołanie funkcji:**

```python
print(pierwiastek(16))
```

**Wyjście:**

```
4.0
```

### Ograniczenia / gwarancje

* Dla `n = 0` funkcja ma zwrócić `0.0`.

*/

function pierwiastekLiczby(liczba) {
  var pierwiastek = liczba;
  while (pierwiastek * pierwiastek > liczba) {
    pierwiastek = (pierwiastek + liczba / pierwiastek) / 2;
  }
  return pierwiastek;
}

// Testy
function testPierwiastekLiczby() {
  console.assert(
    pierwiastekLiczby(4) === 2,
    "Niepoprawny pierwiastek z liczby 4"
  );
  console.assert(
    pierwiastekLiczby(9) === 3,
    "Niepoprawny pierwiastek z liczby 9"
  );
  console.assert(
    Math.abs(pierwiastekLiczby(2) - 1.41421356) < 0.0001,
    "Niepoprawny pierwiastek z liczby 2"
  );
}

testPierwiastekLiczby();

