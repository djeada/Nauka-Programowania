/*
ZAD-03 — Czy napis A jest początkiem napisu B?

**Poziom:** ★★☆
**Tagi:** `string`, `prefix`

### Treść

Otrzymujesz dwa napisy:

1. Napis `A` — potencjalny przedrostek,
2. Napis `B` — napis testowany.

Sprawdź, czy `B` **zaczyna się** od `A`.

### Wejście

* 1 linia: `A`
* 2 linia: `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Dino
Dinozaur jest zly
```

**Wyjście:**

```
Prawda
```

*/

function czyPoczatek(napisA, napisB) {
  return napisB.startsWith(napisA);
}

function testCzyPoczatek() {
  const napisA = "Dino";
  const napisB = "Dinozaur jest zly";
  const wynik = true;
  console.assert(czyPoczatek(napisA, napisB) === wynik, "Test nieudany");
}

testCzyPoczatek();

