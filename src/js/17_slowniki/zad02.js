/*
ZAD-02 — Słownik z dwóch list (klucze i wartości)

**Poziom:** ★☆☆
**Tagi:** `dict`, `listy`

### Treść

Wczytaj dwie listy. Jeśli mają tę samą długość, utwórz słownik: klucz z pierwszej listy → wartość z drugiej listy.
Jeśli długości są różne, wypisz pusty słownik `{}`.

### Wejście

* 1 linia: `n`
* 2 linia: `m`
* następnie `n` liczb (pierwsza lista)
* następnie `m` liczb (druga lista)

### Wyjście

* Słownik albo `{}`

### Przykład

**Wejście:**

```
3
3
3 5 8
1 2 -1
```

**Wyjście:**

```
{3: 1, 5: 2, 8: -1}
```

*/

function stworzSlownik(list1, list2) {
  const slownik = {};
  const dlugosc1 = list1.length;
  const dlugosc2 = list2.length;
  if (dlugosc1 !== dlugosc2) {
    return slownik;
  }
  for (let i = 0; i < dlugosc1; i++) {
    slownik[list1[i]] = list2[i];
  }
  return slownik;
}

function testSlownik() {
  const slownik1 = stworzSlownik([3, 5, 8], [1, 2, -1]);
  console.assert(slownik1[3] === 1, "Test 1 nie powiodl sie");
  console.assert(slownik1[5] === 2, "Test 2 nie powiodl sie");
  console.assert(slownik1[8] === -1, "Test 3 nie powiodl sie");

  const slownik2 = stworzSlownik([1, 2, 3, 4], [10, 20, 30]);
  console.assert(Object.keys(slownik2).length === 0, "Test 4 nie powiodl sie");

  const slownik3 = stworzSlownik([], []);
  console.assert(Object.keys(slownik3).length === 0, "Test 5 nie powiodl sie");
}

testSlownik();

