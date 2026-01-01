/*
ZAD-15 — Element dominujący

**Poziom:** ★★☆
**Tagi:** `zliczanie`, `dict`, `majority`

### Treść

Wczytaj listę liczb naturalnych. Jeśli istnieje liczba, która występuje **więcej niż N/2 razy**, wypisz ją. W przeciwnym razie wypisz `-1`.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — element dominujący lub `-1`.

### Przykład

**Wejście:**

```
5
4
7
4
4
2
```

**Wyjście:**

```
4
```

*/

// Funkcja znajdujaca element dominujacy w liscie liczb naturalnych
function znajdzElementDominujacy(lista) {
  let kandydat = null;
  let licznik = 0;

  for (let liczba of lista) {
    if (licznik === 0) {
      kandydat = liczba;
    }
    licznik += kandydat === liczba ? 1 : -1;
  }

  let wystapienia = lista.filter((liczba) => liczba === kandydat).length;
  return wystapienia > lista.length / 2 ? kandydat : -1;
}

// Testy

function testZnajdzElementDominujacy() {
  console.assert(znajdzElementDominujacy([4, 7, 4, 4, 2]) === 4);
  console.assert(znajdzElementDominujacy([2, 2, 1, 1, 3]) === -1);
  console.assert(znajdzElementDominujacy([5, 5, 5, 3, 3, 5, 5]) === 5);
  console.assert(znajdzElementDominujacy([6, 6, 6, 2, 6, 6]) === 6);
}

testZnajdzElementDominujacy();

