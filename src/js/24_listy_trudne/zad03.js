/*
ZAD-03 — Minimalny iloczyn trzech liczb

**Poziom:** ★★☆
**Tagi:** `list`, `min`, `math`

### Treść

Otrzymujesz listę liczb całkowitych. Znajdź **najmniejszy możliwy iloczyn trzech liczb** wybranych z tej listy.

Jeśli lista zawiera mniej niż 3 liczby — wypisz iloczyn wszystkich elementów listy.

### Wejście

* 1 linia: lista liczb całkowitych `A`

### Wyjście

* 1 linia: jedna liczba całkowita

### Przykład

**Wejście:**

```
[3, -1, -3, 2, 9, 4]
```

**Wyjście:**

```
-108
```

*/

const minimalnyIloczyn = (lista) => {
  let min = lista[0] * lista[1] * lista[2];
  for (let i = 0; i < lista.length; i++) {
    for (let j = i + 1; j < lista.length; j++) {
      for (let k = j + 1; k < lista.length; k++) {
        if (lista[i] * lista[j] * lista[k] < min) {
          min = lista[i] * lista[j] * lista[k];
        }
      }
    }
  }
  return min;
};

// Testy
const lista1 = [3, -1, -3, 2, 9, 4];
const wynik1 = -108;
const lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9];
const wynik2 = 6;

console.assert(minimalnyIloczyn(lista1) === wynik1, "Test 1 nieudany");
console.assert(minimalnyIloczyn(lista2) === wynik2, "Test 2 nieudany");

