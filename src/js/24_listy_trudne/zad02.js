/*
ZAD-02 — Przesuń zera na koniec listy

**Poziom:** ★★☆
**Tagi:** `list`, `stabilność`, `przekształcenie`

### Treść

Otrzymujesz listę liczb całkowitych. Przenieś wszystkie zera na koniec listy, **zachowując kolejność** pozostałych elementów.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista po przekształceniu

### Przykład

**Wejście:**

```
[0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0]
```

**Wyjście:**

```
[1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0]
```

*/

const przesunZera = (lista) => {
  let zero = [];
  let result = [];
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === 0) {
      zero.push(lista[i]);
    } else {
      result.push(lista[i]);
    }
  }
  return result.concat(zero);
};

// Testy
const lista1 = [0, 1, 3, 0, 8, 12, 0, 4, 0, 7, 0];
const wynik1 = [1, 3, 8, 12, 4, 7, 0, 0, 0, 0, 0];
const lista2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
const wynik2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

console.assert(
  JSON.stringify(przesunZera(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(przesunZera(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

