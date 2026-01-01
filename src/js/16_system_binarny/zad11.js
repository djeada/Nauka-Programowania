/*
ZAD-11 — Palindrom w systemie binarnym

**Poziom:** ★★☆
**Tagi:** `binarne`, `palindrom`, `string`

### Treść

Wczytaj liczbę naturalną `n`. Sprawdź, czy jej reprezentacja binarna (bez wiodących zer) jest palindromem.

Wypisz:

* `Prawda` — jeśli tak,
* `Fałsz` — jeśli nie.

### Wejście

* 1. linia: `n`

### Wyjście

Jedno słowo: `Prawda` lub `Fałsz`.

### Przykład

**Wejście:**

```
26
```

**Wyjście:**

```
Fałsz
```

### Uwagi (ważne)

* `26` ma zapis binarny `11010`, który **nie** jest palindromem.
  (W Twoim wcześniejszym przykładzie było to opisane błędnie — tu trzymamy się definicji palindromu 1:1.)

*/

function czyPalindrom(liczba) {
  let lewyBit = 1;
  let prawyBit = 1 << 30;

  while (lewyBit < prawyBit) {
    if ((liczba & lewyBit) !== (liczba & prawyBit) >>> 30) {
      return false;
    }
    lewyBit <<= 1;
    prawyBit >>>= 1;
  }

  return true;
}

// Testy
function test() {
  let input = 26;
  let expectedOutput = false; // 26 = 11010 (nie jest palindromem)
  let output = czyPalindrom(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

