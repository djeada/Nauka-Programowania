/*
ZAD-04 — Dodawanie i odejmowanie macierzy

**Poziom:** ★☆☆
**Tagi:** `macierze`, `arytmetyka`

### Treść

Wczytaj dwie macierze `n×m`.
a) Wypisz ich sumę.
b) Wypisz różnicę: (pierwsza − druga).

### Wejście

* 1. linia: `n`
* 2. linia: `m`
* potem `n` wierszy pierwszej macierzy (po `m` liczb)
* potem `n` wierszy drugiej macierzy (po `m` liczb)

### Wyjście

Najpierw `n` wierszy sumy, potem `n` wierszy różnicy (bez dodatkowych napisów).

### Przykład

**Wejście:**

```
2
2
1 2
-2 0
5 -3
1 7
```

**Wyjście:**

```
6 -1
-1 7
-4 5
-3 -7
```

*/

// Funkcja dodaje dwie macierze element po elemencie
// Złożoność czasowa: O(n*m), gdzie n to liczba wierszy, m to liczba kolumn
// Złożoność pamięciowa: O(n*m)
function dodajMacierze(macierzA, macierzB) {
  const wynik = [];
  for (let i = 0; i < macierzA.length; i++) {
    const wiersz = [];
    for (let j = 0; j < macierzA[i].length; j++) {
      wiersz.push(macierzA[i][j] + macierzB[i][j]);
    }
    wynik.push(wiersz);
  }
  return wynik;
}

// Funkcja odejmuje dwie macierze element po elemencie
// Złożoność czasowa: O(n*m), gdzie n to liczba wierszy, m to liczba kolumn
// Złożoność pamięciowa: O(n*m)
function odejmijMacierze(macierzA, macierzB) {
  const wynik = [];
  for (let i = 0; i < macierzA.length; i++) {
    const wiersz = [];
    for (let j = 0; j < macierzA[i].length; j++) {
      wiersz.push(macierzA[i][j] - macierzB[i][j]);
    }
    wynik.push(wiersz);
  }
  return wynik;
}

// test
function testDodajMacierze() {
  const macierzA = [
    [1, 2],
    [-2, 0],
  ];
  const macierzB = [
    [5, -3],
    [1, 7],
  ];
  const wynikDodawania = [
    [6, -1],
    [-1, 7],
  ];
  const dodawanie = dodajMacierze(macierzA, macierzB);
  for (let i = 0; i < dodawanie.length; i++) {
    for (let j = 0; j < dodawanie[i].length; j++) {
      console.assert(
        dodawanie[i][j] === wynikDodawania[i][j],
        `Element macierzy o indeksie (${i}, ${j}) nie jest taki sam jak w oczekiwanej macierzy. Oczekiwano: ${wynikDodawania[i][j]}, otrzymano: ${dodawanie[i][j]}.`
      );
    }
  }
}

function testOdejmijMacierze() {
  const macierzA = [
    [1, 2],
    [-2, 0],
  ];
  const macierzB = [
    [5, -3],
    [1, 7],
  ];
  const wynikOdejmowania = [
    [-4, 5],
    [-3, -7],
  ];
  const odejmowanie = odejmijMacierze(macierzA, macierzB);
  for (let i = 0; i < odejmowanie.length; i++) {
    for (let j = 0; j < odejmowanie[i].length; j++) {
      console.assert(
        odejmowanie[i][j] === wynikOdejmowania[i][j],
        "Element macierzy o indeksie (${i}, ${j}) nie jest taki sam jak w oczekiwanej macierzy. Oczekiwano: ${wynikOdejmowania[i][j]}, otrzymano: ${odejmowanie[i][j]}."
      );
    }
  }
}

testDodajMacierze();
testOdejmijMacierze();

