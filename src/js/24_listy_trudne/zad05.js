/*
ZAD-05 — Zbiór potęgowy listy

**Poziom:** ★★★
**Tagi:** `list`, `subsets`, `combinatorics`

### Treść

Otrzymujesz listę liczb naturalnych (mogą występować powtórzenia). Wygeneruj zbiór wszystkich możliwych podzbiorów tej listy.

Wynik ma zawierać wszystkie podzbiory (włącznie z pustym).

### Wejście

* 1 linia: lista liczb naturalnych `A`

### Wyjście

* 1 linia: lista list (wszystkie podzbiory)

### Przykład

**Wejście:**

```
[1, 2, 1]
```

**Wyjście:**

```
[[], [1], [2], [1, 2], [1, 1], [2, 1], [1, 1, 2], [1, 2, 1]]
```

### Uwagi

* Jeśli sprawdzarka wymaga konkretnej kolejności podzbiorów, musi być ona opisana w treści — w przeciwnym razie dopuszczalna może być dowolna. (Jeśli chcesz, mogę dopisać sztywną konwencję kolejności, ale bez rozwiązań.)

*/
function zbiorPotegowy(lista) {
  // wymaga sortowania O(nlogn)
  lista.sort();

  const N = Math.pow(2, lista.length);
  const zbiorPotegowy = new Set();

  for (let i = 0; i < N; i++) {
    const subset = lista.filter((_, j) => i & (1 << j));
    zbiorPotegowy.add(JSON.stringify(subset));
  }

  return Array.from(zbiorPotegowy, JSON.parse);
}

// Testy
const lista1 = [1, 2, 1];
const wynik1 = [[], [1], [2], [1, 2], [1, 1], [1, 1, 2]];
const lista2 = [1, 2, 3, 4];
const wynik2 = [
  [],
  [1],
  [2],
  [1, 2],
  [3],
  [1, 3],
  [2, 3],
  [1, 2, 3],
  [4],
  [1, 4],
  [2, 4],
  [1, 2, 4],
  [3, 4],
  [1, 3, 4],
  [2, 3, 4],
  [1, 2, 3, 4],
];

const sortSubsets = (a, b) =>
  a.length - b.length || a.toString().localeCompare(b.toString());

const sortedResult1 = zbiorPotegowy(lista1).sort(sortSubsets);
const sortedExpected1 = wynik1.sort(sortSubsets);
const sortedResult2 = zbiorPotegowy(lista2).sort(sortSubsets);
const sortedExpected2 = wynik2.sort(sortSubsets);

console.assert(
  JSON.stringify(sortedResult1) === JSON.stringify(sortedExpected1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortedResult2) === JSON.stringify(sortedExpected2),
  "Test 2 nieudany"
);

