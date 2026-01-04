/*
ZAD-06 — Sumowanie elementów ciągu

**Poziom:** ★☆☆
**Tagi:** `ciągi`, `sumowanie`, `pętle`

### Treść

Wczytaj liczbę naturalną `n` (`n ≥ 1`) i oblicz:

a) ( \sum_{k=1}^{n} (k^2 + k + 1) )

b) ( \sum_{k=1}^{n} (k^2 + 5k) )

c) ( \sum_{k=1}^{n} (k + 2k) )  (czyli ( \sum_{k=1}^{n} 3k ))

Wypisz trzy sumy w kolejności a), b), c).

### Wejście

Jedna liczba naturalna:

* 1. linia: `n` (`n ≥ 1`)

### Wyjście

Trzy liczby naturalne — każda w oddzielnej linii:

1. suma dla (a)
2. suma dla (b)
3. suma dla (c)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
10
16
9
```

### Uwagi o formatowaniu

* Wyniki są liczbami całkowitymi — nie stosuj żadnego dodatkowego zaokrąglania.

*/

const liczba = parseInt(prompt("Podaj liczbe:"));

// Petla $$a_n = n^2 + n + 1$$
let suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i ** 2 + i + 1;
}

// Wypisanie wyniku
console.log(suma);

// Petla $$a_n = n^2 + 5n$$
suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i ** 2 + 5 * i;
}

// Wypisanie wyniku
console.log(suma);

// Petla $$a_n = n + 2n$$
suma = 0;
for (let i = 1; i <= liczba; i++) {
  suma += i + 2 * i;
}

// Wypisanie wyniku
console.log(suma);

