/*
ZAD-01A — Dziesiętny → binarny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `binarne`, `pętle`

### Treść

Wczytaj liczbę naturalną w systemie dziesiętnym i wypisz jej reprezentację binarną.

### Wejście

* 1. linia: `n` (liczba naturalna)

### Wyjście

Jedna linia: zapis binarny `n`.

### Przykład

**Wejście:**

```
3
```

**Wyjście:**

```
11
```

### Uwagi o formacie

* Dla `n = 0` wypisz `0`.

ZAD-01B — Binarny → dziesiętny

**Poziom:** ★☆☆
**Tagi:** `konwersja`, `string`, `binarne`

### Treść

Wczytaj liczbę naturalną w systemie binarnym (ciąg `0/1`) i wypisz jej wartość w systemie dziesiętnym.

### Wejście

* 1. linia: `b` (ciąg znaków `0` i `1`)

### Wyjście

Jedna linia: liczba w systemie dziesiętnym.

### Przykład

**Wejście:**

```
101
```

**Wyjście:**

```
5
```

*/

// a) Konwersja liczby dziesietnej na binarna
function dziesietnaNaBinarna(dziesietna) {
  let binarna = "";
  while (dziesietna > 0) {
    binarna = (dziesietna % 2) + binarna;
    dziesietna = Math.floor(dziesietna / 2);
  }
  return binarna === "" ? "0" : binarna;
}

// b) Konwersja liczby binarnej na dziesietna
function binarnaNaDziesietna(binarna) {
  let dziesietna = 0;
  for (let i = 0; i < binarna.length; i++) {
    dziesietna += parseInt(binarna[i]) * Math.pow(2, binarna.length - i - 1);
  }
  return dziesietna;
}

// Testy
function test() {
  // Test konwersji dziesietnej na binarna
  let dziesietna = 3;
  let oczekiwanaBinarna = "11";
  let binarna = dziesietnaNaBinarna(dziesietna);
  console.assert(binarna === oczekiwanaBinarna, "Blad dla ${dziesietna}");

  // Test konwersji binarnej na dziesietna
  let binarna2 = "101";
  let oczekiwanaDziesietna = 5;
  let dziesietna2 = binarnaNaDziesietna(binarna2);
  console.assert(dziesietna2 === oczekiwanaDziesietna, "Blad dla ${binarna2}");
}

test();

