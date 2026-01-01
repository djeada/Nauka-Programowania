/*
ZAD-08 — Maksymalny zysk ze sprzedaży sznurka

**Poziom:** ★★★
**Tagi:** `dp`, `rod cutting`, `optymalizacja`

### Treść

Masz sznurek o długości `n` i cennik: ceny kawałków długości od `1` do `n`. Możesz pociąć sznurek na kawałki o całkowitych długościach. Znajdź maksymalny zysk.

### Wejście

* 1 linia: lista `prices` (długości 1..n)
* 2 linia: `n` (liczba naturalna)

### Wyjście

* 1 linia: maksymalny zysk (liczba całkowita)

### Przykład

**Wejście:**

```
[1, 5, 8, 9, 10, 17, 17, 20]
4
```

**Wyjście:**

```
10
```

*/

const sznurek = (lista, n) => {
  let max = 0;
  for (let i = 0; i < n; i++) {
    let suma = 0;
    for (let j = 0; j < n - i; j++) {
      suma += lista[j];
    }
    if (suma > max) {
      max = suma;
    }
  }
  return max;
};

// Testy
const lista1 = [1, 5, 8, 9, 10, 17, 17, 20];
const wynik1 = 10;
const lista2 = [3, 5, 8, 9, 10, 17, 17, 20];
const wynik2 = 22;

console.assert(sznurek(lista1, 4) === wynik1, "Test 1 nieudany");
console.assert(sznurek(lista2, 8) === wynik2, "Test 2 nieudany");

