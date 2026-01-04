/*
ZAD-02 — Zamiana kolejności liczb

**Poziom:** ★☆☆
**Tagi:** `I/O`, `zmienne`

### Treść

Wczytaj dwie liczby całkowite i wypisz je w odwrotnej kolejności (każda w osobnej linii).

### Wejście

Dwie liczby całkowite:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Dwie linie:

* 1. linia: `b`
* 2. linia: `a`

### Ograniczenia / gwarancje

* `a`, `b` mieszczą się w typowym zakresie int (np. 32-bit).

### Przykład

**Wejście:**

```
-7
4
```

**Wyjście:**

```
4
-7
```

*/

const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Zamiana kolejnosci liczb
console.log(liczba_b);
console.log(liczba_a);

