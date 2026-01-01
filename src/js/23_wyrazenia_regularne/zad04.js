/*
ZAD-04 — Sprawdź, czy słowo występuje w zdaniu jako osobne słowo

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz dwa napisy: zdanie oraz słowo. Sprawdź, czy słowo występuje w zdaniu jako samodzielne słowo (nie jako fragment innego słowa).

### Wejście

Dwie linie:

1. `zdanie`
2. `slowo`

### Wyjście

Jedna linia:

* `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
Siała baba mak.
babcia
```

**Wyjście:**

```
Fałsz
```

*/

function czy_wystepuje_jako_slowo(zdanie, slowo) {
  const wyrazenie = new RegExp(`\\b${slowo}\\b`);

  return wyrazenie.test(zdanie);
}

function test_czy_wystepuje_jako_slowo() {
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", "babcia") === false
  );
  console.assert(czy_wystepuje_jako_slowo("Siala baba mak.", "baba") === true);
  console.assert(czy_wystepuje_jako_slowo("Siala baba mak.", "Siala") === true);
  console.assert(czy_wystepuje_jako_slowo("Siala baba mak.", "mak.") === true);
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", "Siala baba mak.") === true
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", "Siala baba mak") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", "Siala baba mak. ") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", " Siala baba mak.") === false
  );
  console.assert(
    czy_wystepuje_jako_slowo("Siala baba mak.", " Siala baba mak. ") === false
  );
}

test_czy_wystepuje_jako_slowo();

