/*
ZAD-09 — Najdłuższy naprzemienny podciąg

**Poziom:** ★★★
**Tagi:** `dp`, `subsequence`, `naprzemienny`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź najdłuższy podciąg naprzemienny, w którym różnice między kolejnymi elementami zmieniają znak (raz dodatnia, raz ujemna, itd.).

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: lista liczb — najdłuższy naprzemienny podciąg

### Przykład

**Wejście:**

```
[1, -2, 6, 4, -3, 2, -4, -3]
```

**Wyjście:**

```
[1, -2, 6, -3, 2, -4]
```

### Uwagi

* Jeśli istnieje kilka podciągów o tej samej maksymalnej długości — wybierz ten, który pojawia się „najwcześniej” (najmniejszy możliwy indeks startu), o ile sprawdzarka tego wymaga.

*/

const najdluzszyNaprzemiennyPodciag = (lista) => {
  let result = [];
  let temp = [];
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] > lista[i + 1]) {
      temp.push(lista[i]);
      if (temp.length > result.length) {
        result = temp;
      }
    } else {
      temp = [];
    }
  }
  return result;
};

// Testy
const lista1 = [1, -2, 6, 4, -3, 2, -4, -3];
const wynik1 = [1, -2, 6, -3, 2, -4];
const lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const wynik2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];

console.assert(
  JSON.stringify(najdluzszyNaprzemiennyPodciag(lista1)) ===
    JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(najdluzszyNaprzemiennyPodciag(lista2)) ===
    JSON.stringify(wynik2),
  "Test 2 nieudany"
);

