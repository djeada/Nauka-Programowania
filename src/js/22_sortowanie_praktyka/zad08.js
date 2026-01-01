/*
ZAD-08 — Indeks klucza w cyklicznie posortowanej liście

**Poziom:** ★★☆
**Tagi:** `binary search`, `rotacja`, `list`

### Treść

Otrzymujesz cyklicznie posortowaną listę liczb całkowitych (lista była rosnąca, ale została przesunięta) oraz klucz. Znajdź indeks **pierwszego** wystąpienia klucza. Jeśli klucza nie ma — wypisz `-1`.

### Wejście

* 1 linia: liczba naturalna `N`
* 2 linia: `N` liczb całkowitych oddzielonych spacjami
* 3 linia: liczba całkowita `x` (szukany klucz)

### Wyjście

* 1 linia: indeks pierwszego wystąpienia `x` albo `-1`

### Przykład

**Wejście:**

```
6
3 4 5 6 1 2
4
```

**Wyjście:**

```
1
```

### Ograniczenia / gwarancje

* Lista jest wynikiem rotacji listy posortowanej niemalejąco (mogą wystąpić duplikaty).

*/

const szukaj = (lista, klucz) => {
  let start = 0;
  let koniec = lista.length - 1;

  while (start <= koniec) {
    const srodek = Math.floor((start + koniec) / 2);

    if (lista[srodek] === klucz) {
      return srodek;
    }

    if (lista[start] <= lista[srodek]) {
      if (lista[start] <= klucz && klucz < lista[srodek]) {
        koniec = srodek - 1;
      } else {
        start = srodek + 1;
      }
    } else {
      if (lista[srodek] < klucz && klucz <= lista[koniec]) {
        start = srodek + 1;
      } else {
        koniec = srodek - 1;
      }
    }
  }

  return -1;
};

// Testy
const lista1 = [3, 4, 5, 6, 1, 2];
const klucz1 = 4;
const wynik1 = 1;

const lista2 = [4, 5, 6, 7, 8, 9, 1, 2, 3];
const klucz2 = 6;
const wynik2 = 2;

console.assert(szukaj(lista1, klucz1) === wynik1, "Test 1 nieudany");
console.assert(szukaj(lista2, klucz2) === wynik2, "Test 2 nieudany");

