/*
ZAD-04A — Liczba zer w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `binarne`, `zliczanie`

### Treść

Wczytaj liczbę naturalną `n`. Policz, ile znaków `0` zawiera jej binarna reprezentacja (bez wiodących zer).

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba zer w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
0
```

### Uwagi

* Dla `n = 0` binarnie to `0`, więc liczba zer wynosi `1`.

ZAD-04B — Liczba jedynek w zapisie binarnym

**Poziom:** ★☆☆
**Tagi:** `popcount`, `binarne`

### Treść

Wczytaj `n`. Policz, ile bitów `1` ma liczba w zapisie binarnym.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: liczba jedynek w zapisie binarnym `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
2
```

*/

function iloscZerLiczby(liczba) {
  let binarna = liczba.toString(2);
  let iloscZer = 0;
  for (let i = 0; i < binarna.length; i++) {
    if (binarna[i] === "0") {
      iloscZer++;
    }
  }
  return iloscZer;
}

// Funkcja obliczajaca ilosc jedynek w reprezentacji binarnej liczby
function iloscJedynekLiczby(liczba) {
  let binarna = liczba.toString(2);
  let iloscJedynek = 0;
  for (let i = 0; i < binarna.length; i++) {
    if (binarna[i] === "1") {
      iloscJedynek++;
    }
  }
  return iloscJedynek;
}

// Testy
function test() {
  let input = 3;
  let expectedOutput1 = 0;
  let expectedOutput2 = 2;
  let output1 = iloscZerLiczby(input);
  let output2 = iloscJedynekLiczby(input);

  console.assert(output1 === expectedOutput1, "Test nie powiodl sie");
  console.assert(output2 === expectedOutput2, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

