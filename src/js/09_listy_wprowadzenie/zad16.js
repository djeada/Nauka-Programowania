/*
ZAD-16 — Indeksy pierwszej pary o sumie x

**Poziom:** ★★☆
**Tagi:** `hashmap`, `indeksy`, `2-sum`

### Treść

Wczytaj listę liczb całkowitych oraz liczbę `x`. Znajdź indeksy **pierwszej** pary `(i, j)` (z `i < j`) takiej, że `lista[i] + lista[j] == x`.

Jeśli nie istnieje taka para — wypisz `-1 -1`.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `x` (liczba całkowita)

### Wyjście

Dwie liczby całkowite w jednej linii (oddzielone spacją): `i j` albo `-1 -1`.

### Przykład

**Wejście:**

```
5
1
3
4
5
2
5
```

**Wyjście:**

```
0 2
```

*/

function znajdzPareSumujacaDo(lista, x) {
  const mapaIndeksow = new Map();

  for (let i = 0; i < lista.length; i++) {
    const komplement = x - lista[i];
    if (mapaIndeksow.has(komplement)) {
      return [mapaIndeksow.get(komplement), i];
    }
    mapaIndeksow.set(lista[i], i);
  }

  return [-1, -1];
}

// Testy

function testZnajdzPareSumujacaDo() {
  console.assert(
    JSON.stringify(znajdzPareSumujacaDo([1, 3, 4, 5, 2], 5)) ===
      JSON.stringify([0, 2])
  );
  console.assert(
    JSON.stringify(znajdzPareSumujacaDo([2, 5, 9, 4, 7], 12)) ===
      JSON.stringify([1, 4])
  );
  console.assert(
    JSON.stringify(znajdzPareSumujacaDo([2, 5, 9, 4, 7], 20)) ===
      JSON.stringify([-1, -1])
  );
}

testZnajdzPareSumujacaDo();

