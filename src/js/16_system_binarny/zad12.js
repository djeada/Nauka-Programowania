/*
ZAD-12 — Najdłuższy ciąg zer otoczony jedynkami

**Poziom:** ★★★
**Tagi:** `binarne`, `binary gap`, `pętle`

### Treść

Wczytaj liczbę naturalną `n`. W jej reprezentacji binarnej znajdź długość najdłuższego ciągu kolejnych zer, który jest **z obu stron otoczony jedynkami** (tzw. *binary gap*).

Jeśli nie ma takiego ciągu — wypisz `0`.

### Wejście

* 1. linia: `n`

### Wyjście

Jedna liczba naturalna: długość najdłuższego „gapu”.

### Przykład

**Wejście:**

```
14
```

**Wyjście:**

```
0
```

### Uwagi (ważne)

* `14` ma zapis `1110` — zero na końcu **nie jest otoczone jedynkami z prawej**, więc wynik to `0`.
  Dla przykładu `20` (`10100`) najdłuższy gap ma długość `1` (między `1` i `1`).

*/

// Funkcja obliczajaca najdluzszy ciag zer w liczbie binarnej
function najdluzszyCiagZer(liczba) {
  let binarna = liczba.toString(2);
  let najdluzszyCiag = 0;
  let aktualnyCiag = 0;
  for (let i = 0; i < binarna.length; i++) {
    if (binarna[i] === "0") {
      aktualnyCiag++;
    } else {
      if (aktualnyCiag > najdluzszyCiag) {
        najdluzszyCiag = aktualnyCiag;
      }
      aktualnyCiag = 0;
    }
  }
  return najdluzszyCiag;
}

// Testy
function test() {
  let input = 14;
  let expectedOutput = 1;
  let output = najdluzszyCiagZer(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

