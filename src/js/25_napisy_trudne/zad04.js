/*
ZAD-04 — Usuń powtórzenia znaków

**Poziom:** ★★★
**Tagi:** `string`, `set`, `unique`, `kolejność`

### Treść

Otrzymujesz napis. Usuń wszystkie powtórzenia znaków tak, aby **każdy znak wystąpił tylko raz**, zachowując **kolejność pierwszych wystąpień**.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: napis z unikalnymi znakami

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
AB
```

*/

function usunPowtorzenia(napis) {
  const unikalneZnaki = new Set(napis);
  return Array.from(unikalneZnaki).join("");
}

function testUsunPowtorzenia() {
  const napis = "AAAAAAAAAABBBBBBBBA";
  const wynik = "AB";
  console.assert(usunPowtorzenia(napis) === wynik, "Test nieudany");
}

testUsunPowtorzenia();

