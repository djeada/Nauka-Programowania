/*
ZAD-01 — Słownik: liczby i ich kwadraty

**Poziom:** ★☆☆
**Tagi:** `dict`, `pętla`

### Treść

Wczytaj liczbę `n`. Utwórz słownik, gdzie klucze to liczby od `1` do `n-1`, a wartości to ich kwadraty.

### Wejście

* 1 linia: `n` (n ≥ 1)

### Wyjście

* Słownik w postaci: `{1: 1, 2: 4, ...}`

### Przykład

**Wejście:**

```
5
```

**Wyjście:**

```
{1: 1, 2: 4, 3: 9, 4: 16}
```

*/

function stworzSlownikKwadratow(n) {
  const slownik = {};
  for (let i = 1; i < n; i++) {
    slownik[i] = i * i;
  }
  return slownik;
}

function testSlownikKwadratow() {
  const slownik1 = stworzSlownikKwadratow(5);
  console.assert(slownik1[1] === 1, "Test 1 nie powiodl sie");
  console.assert(slownik1[2] === 4, "Test 2 nie powiodl sie");
  console.assert(slownik1[3] === 9, "Test 3 nie powiodl sie");
  console.assert(slownik1[4] === 16, "Test 4 nie powiodl sie");

  const slownik2 = stworzSlownikKwadratow(10);
  console.assert(slownik2[6] === 36, "Test 5 nie powiodl sie");
  console.assert(slownik2[9] === 81, "Test 6 nie powiodl sie");
}

testSlownikKwadratow();

