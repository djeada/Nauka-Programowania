/*
ZAD-03 — Sprawdź, czy napis składa się wyłącznie z cyfr

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis. Sprawdź, czy składa się wyłącznie z cyfr (`0–9`).

### Wejście

Jedna linia:

* `s`

### Wyjście

Jedna linia:

* `Prawda` — jeśli napis zawiera tylko cyfry
* `Fałsz` — w przeciwnym razie

### Przykład

**Wejście:**

```
1234
```

**Wyjście:**

```
Prawda
```

*/

function czy_tylko_cyfry(napis) {
  const cyfry = /^[0-9]+$/;

  return cyfry.test(napis);
}

function test_czy_tylko_cyfry() {
  console.assert(czy_tylko_cyfry("1234") === true);
  console.assert(czy_tylko_cyfry("1234a") === false);
  console.assert(czy_tylko_cyfry("a1234") === false);
  console.assert(czy_tylko_cyfry("1234 ") === false);
  console.assert(czy_tylko_cyfry(" 1234") === false);
  console.assert(czy_tylko_cyfry(" 1234 ") === false);
  console.assert(czy_tylko_cyfry("1234.5") === false);
  console.assert(czy_tylko_cyfry("1234,5") === false);
}
test_czy_tylko_cyfry();

