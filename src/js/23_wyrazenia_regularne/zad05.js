/*
ZAD-05 — Wyodrębnij cyfry z tekstu

**Poziom:** ★☆☆
**Tagi:** `regex`, `string`

### Treść

Otrzymujesz napis zawierający różne znaki. Wyodrębnij wszystkie cyfry i wypisz je jako jeden napis (z zachowaniem kolejności).

### Wejście

Jedna linia:

* `tekst`

### Wyjście

Jedna linia:

* napis złożony tylko z cyfr z tekstu wejściowego

### Przykład

**Wejście:**

```
Terminator2001
```

**Wyjście:**

```
2001
```

*/

function wyodrebnij_cyfry(napis) {
  const cyfry = /[0-9]+/g;

  return napis.match(cyfry).join("");
}

function test_wyodrebnij_cyfry() {
  console.assert(wyodrebnij_cyfry("Terminator2001") === "2001");
  console.assert(wyodrebnij_cyfry("Terminator 2001") === "2001");
  console.assert(wyodrebnij_cyfry(" Terminator 2001 ") === "2001");
}

test_wyodrebnij_cyfry();

