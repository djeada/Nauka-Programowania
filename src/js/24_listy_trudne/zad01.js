/*
ZAD-01 — Najdłuższy ciąg jedynek

**Poziom:** ★★☆
**Tagi:** `list`, `0/1`, `analiza`, `indeksy`

### Treść

Otrzymujesz listę składającą się wyłącznie z `0` i `1`. Znajdź **indeks zera**, które po zamianie na `1` da **najdłuższy ciąg kolejnych jedynek**.

Jeśli lista składa się wyłącznie z zer **albo** wyłącznie z jedynek — wypisz `-1`.

### Wejście

* 1 linia: lista `A` (tylko `0` i `1`)

### Wyjście

* 1 linia: indeks (liczba całkowita) albo `-1`

### Przykład

**Wejście:**

```
[0, 0, 1, 0, 1, 1, 1, 0, 1, 1]
```

**Wyjście:**

```
7
```

### Uwagi

* Jeśli kilka zer daje ten sam maksymalny wynik — wybierz to o **najmniejszym indeksie** (jeśli nie określono inaczej w testach).

*/

const najdluzszyCiagJedynek = (lista) => {
  let najdluzszyCiagJedynek = 0;
  let index = -1;
  let liczbaJedynek = 0;
  let indeks = 0;
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === 1) {
      liczbaJedynek++;
    } else {
      indeks = i;
    }
    if (liczbaJedynek > najdluzszyCiagJedynek) {
      najdluzszyCiagJedynek = liczbaJedynek;
      index = indeks;
    }
  }
  return index;
};

// Testy
const lista1 = [0, 0, 1, 0, 1, 1, 1, 0, 1, 1];
const wynik1 = 7;
const lista2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
const wynik2 = -1;

console.assert(najdluzszyCiagJedynek(lista1) === wynik1, "Test 1 nieudany");
console.assert(najdluzszyCiagJedynek(lista2) === wynik2, "Test 2 nieudany");

