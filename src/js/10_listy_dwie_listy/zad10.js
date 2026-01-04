/*
ZAD-10 — Mediana dwóch posortowanych list

**Poziom:** ★★☆
**Tagi:** `list`, `median`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych:

* obie są posortowane rosnąco,
* obie mają tę samą, niezerową długość.

Znajdź medianę zbioru wszystkich elementów z obu list (czyli medianę po „złączeniu” obu list).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: mediana jako liczba zmiennoprzecinkowa
  (jeśli mediana jest całkowita, wypisz ją z `.0`, np. `4.0`)

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
4.5
```

*/

function znajdzMediane(lista1, lista2) {
  let wynik = [];
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    let element1 = lista1[i] || 0;
    let element2 = lista2[i] || 0;
    if (element1 !== element2) {
      wynik.push(element1);
      wynik.push(element2);
    }
  }

  return wynik;
}

// Testy

function testZnajdzMediane() {
  console.assert(znajdzMediane([2, 4, 7], [3, 5, 9]) === 4.5);
  console.assert(znajdzMediane([2, 4, 7], [3, 5, 9, 2]) === 4.5);
  console.assert(znajdzMediane([2, 4, 7], [3, 5, 9, 2, 4]) === 4.5);
  console.assert(znajdzMediane([2, 4, 7], [3, 5, 9, 2, 4, 7]) === 4.5);
}

testZnajdzMediane();

