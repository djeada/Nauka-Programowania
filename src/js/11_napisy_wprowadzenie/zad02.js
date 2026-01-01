/*
ZAD-02 — Policz wystąpienia znaku

**Poziom:** ★☆☆
**Tagi:** `string`, `count`

### Treść

Wczytaj napis oraz jeden znak. Wypisz, ile razy ten znak występuje w napisie.

### Wejście

* 1. linia: napis
* 2. linia: pojedynczy znak

### Wyjście

* 1. linia: liczba wystąpień

### Przykład

**Wejście:**

```
klamra
a
```

**Wyjście:**

```
2
```

*/
// Funkcja liczy wystąpienia określonego znaku w napisie
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(1)
function policzWystapieniaZnaku(napis, znak) {
  let licznik = 0;
  for (let i = 0; i < napis.length; i++) {
    if (napis[i] === znak) {
      licznik++;
    }
  }
  return licznik;
}

// Testy

function test() {
  let input1 = "klamra";
  let input2 = "a";
  let expectedOutput = 2;
  let output = policzWystapieniaZnaku(input1, input2);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

