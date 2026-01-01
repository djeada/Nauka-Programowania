/*
ZAD-05 — Sortowanie szybkie

**Poziom:** ★★☆
**Tagi:** `sorting`, `quick-sort`, `recursion`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **Quick Sort**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
2. Wybierz **pivot** (np. pierwszy element).
3. Podziel elementy na trzy grupy:

   * mniejsze od pivota,
   * równe pivotowi,
   * większe od pivota.
4. Rekurencyjnie posortuj część mniejszych i większych.
5. Sklej wynik: `mniejsze + równe + większe`.

### Wejście

* 1 linia: lista liczb całkowitych

### Wyjście

* 1 linia: posortowana lista rosnąco

### Przykład

**Wejście:**

```
[6, 2, 1, 4, 27]
```

**Wyjście:**

```
[1, 2, 4, 6, 27]
```

### Uwagi o algorytmie

* Średnio: `O(n log n)`, w pesymistycznym przypadku: `O(n^2)`.
* Wybór pivota ma wpływ na wydajność.

*/

const sortowanieSzybkie = (lista) => {
  if (lista.length < 2) {
    return lista;
  }

  const pivotIndeks = Math.floor(Math.random() * lista.length);
  const pivot = lista[pivotIndeks];

  const mniejsze = [];
  const wieksze = [];
  const pivots = [];

  for (const element of lista) {
    if (element < pivot) {
      mniejsze.push(element);
    } else if (element > pivot) {
      wieksze.push(element);
    } else {
      pivots.push(element);
    }
  }

  return sortowanieSzybkie(mniejsze)
    .concat(pivots)
    .concat(sortowanieSzybkie(wieksze));
};

// Testy
const lista1 = [6, 2, 1, 4, 27];
const wynik1 = [1, 2, 4, 6, 27];
const lista2 = [5, 4, 3, 2, 1];
const wynik2 = [1, 2, 3, 4, 5];
const lista3 = [-3, 0, 15, -7, 23];
const wynik3 = [-7, -3, 0, 15, 23];

console.assert(
  JSON.stringify(sortowanieSzybkie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieSzybkie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
console.assert(
  JSON.stringify(sortowanieSzybkie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);

