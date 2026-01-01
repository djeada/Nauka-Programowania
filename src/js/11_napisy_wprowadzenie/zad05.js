/*
ZAD-05 — Co k-ty znak poziomo i pionowo

**Poziom:** ★☆☆
**Tagi:** `string`, `slicing`, `pętle`

### Treść

Wczytaj napis i liczbę `k`.

a) Wypisz co `k`-ty znak w jednym wierszu, oddzielając znaki spacjami.
b) Wypisz co `k`-ty znak pionowo (każdy w osobnej linii).

### Wejście

* 1. linia: napis
* 2. linia: liczba naturalna `k` (k ≥ 1)

### Wyjście

* (a) 1 linia: znaki oddzielone spacjami
* (b) wiele linii: każdy znak osobno

### Przykład

**Wejście:**

```
Grzechotnik
3
```

**Wyjście:**

```
z h n
z
h
n
```

### Uwagi o formatowaniu

* Dokładnie jedna spacja między znakami w punkcie (a), bez spacji na końcu linii.

*/

function coKtyPoziomo(napis, k) {
  let wynik = "";
  for (let i = k - 1; i < napis.length; i += k) {
    wynik += napis[i] + " ";
  }
  return wynik.trim();
}

function coKtyPionowo(napis, k) {
  let wynik = "";
  for (let i = k - 1; i < napis.length; i += k) {
    wynik += napis[i] + "\n";
  }
  return wynik.trim();
}

// Testy

function test() {
  let input1 = "Grzechotnik";
  let input2 = 3;
  let expectedOutput1 = "z h n";
  let expectedOutput2 = "z\nh\nn";
  let output1 = coKtyPoziomo(input1, input2);
  let output2 = coKtyPionowo(input1, input2);

  console.assert(output1 === expectedOutput1, "Test nie powiodl sie");
  console.assert(output2 === expectedOutput2, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

