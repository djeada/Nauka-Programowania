/*
ZAD-12 — Usuń spacje ze zdania

**Poziom:** ★☆☆
**Tagi:** `replace`, `string`

### Treść

Wczytaj zdanie i usuń z niego wszystkie spacje.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie bez spacji

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
Alamakota
```

*/

function usunSpacje(napis) {
  return napis.replace(/\s+/g, "");
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = "Alamakota";
  let output = usunSpacje(input);

  console.assert(
    output === expectedOutput,
    "Test nie powiodl sie dla " +
      input +
      ". Otrzymany wynik to " +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();

