/*
ZAD-04 — Sortowanie przez scalanie

**Poziom:** ★★☆
**Tagi:** `sorting`, `merge-sort`, `recursion`

### Treść

Wczytaj listę liczb całkowitych i posortuj ją rosnąco algorytmem **sortowania przez scalanie**:

1. Jeśli lista ma mniej niż 2 elementy — jest posortowana.
2. Podziel listę na dwie (w miarę) równe części.
3. Rekurencyjnie posortuj obie części.
4. **Scal** dwie posortowane listy w jedną posortowaną.

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

* Złożoność czasowa: `O(n log n)`.

*/

const scalanie = (lewa, prawa) => {
  let scalonaLista = [];
  let lewyIndeks = 0;
  let prawyIndeks = 0;

  while (lewyIndeks < lewa.length && prawyIndeks < prawa.length) {
    if (lewa[lewyIndeks] < prawa[prawyIndeks]) {
      scalonaLista.push(lewa[lewyIndeks]);
      lewyIndeks++;
    } else {
      scalonaLista.push(prawa[prawyIndeks]);
      prawyIndeks++;
    }
  }

  return scalonaLista
    .concat(lewa.slice(lewyIndeks))
    .concat(prawa.slice(prawyIndeks));
};

const sortowaniePrzezScalanie = (lista) => {
  if (lista.length < 2) {
    return lista;
  }

  const srodek = Math.floor(lista.length / 2);
  const lewa = lista.slice(0, srodek);
  const prawa = lista.slice(srodek);

  return scalanie(
    sortowaniePrzezScalanie(lewa),
    sortowaniePrzezScalanie(prawa)
  );
};

// Testy
const lista1 = [6, 2, 1, 4, 27];
const wynik1 = [1, 2, 4, 6, 27];
const lista2 = [5, 4, 3, 2, 1];
const wynik2 = [1, 2, 3, 4, 5];
const lista3 = [-3, 0, 15, -7, 23];
const wynik3 = [-7, -3, 0, 15, 23];

console.assert(
  JSON.stringify(sortowaniePrzezScalanie(lista1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowaniePrzezScalanie(lista2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);
console.assert(
  JSON.stringify(sortowaniePrzezScalanie(lista3)) === JSON.stringify(wynik3),
  "Test 3 nieudany"
);

