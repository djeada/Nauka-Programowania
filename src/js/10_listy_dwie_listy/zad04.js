/*
ZAD-04 — Iloczyn skalarny dwóch wektorów 3D

**Poziom:** ★☆☆
**Tagi:** `list`, `wektory`, `math`

### Treść

Wczytaj dwie listy długości 3 (wektory 3D) i oblicz ich **iloczyn skalarny**:
[
A_xB_x + A_yB_y + A_zB_z
]

### Wejście

* 1 linia: wektor A (lista 3 liczb całkowitych)
* 2 linia: wektor B (lista 3 liczb całkowitych)

### Wyjście

* 1 linia: jedna liczba całkowita — iloczyn skalarny

### Przykład

**Wejście:**

```
[1, 2, 3]
[3, 1, 2]
```

**Wyjście:**

```
11
```

*/

function mnozWektory(lista1, lista2) {
  let wynik = 0;
  for (let i = 0; i < 3; i++) {
    wynik += lista1[i] * lista2[i];
  }
  return wynik;
}

// Testy

function testMnozWektory() {
  console.assert(mnozWektory([1, 2, 3], [3, 1, 2]) === 5);
  console.assert(mnozWektory([1, 2, 3], [3, 1, 2, 5]) === 5);
}

function main() {
  testMnozWektory();
}

main();

