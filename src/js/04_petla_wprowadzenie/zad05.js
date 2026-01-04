/*
ZAD-05 — Liczby z przedziału

**Poziom:** ★☆☆
**Tagi:** `pętle`, `przedziały`, `modulo`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`. Najpierw ustal:

* `lo = min(a, b)`
* `hi = max(a, b)`

Następnie:

a) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` (każda w osobnej linii).

b) Wypisz wszystkie liczby naturalne `x` takie, że `lo < x < hi` oraz `x` jest podzielne przez `3` (każda w osobnej linii).

### Wejście

Dwie liczby naturalne:

* 1. linia: `a`
* 2. linia: `b`

### Wyjście

Najpierw wyniki podpunktu (a), potem wyniki podpunktu (b), każda liczba w osobnej linii.

### Przykład

**Wejście:**

```
9
5
```

**Wyjście:**

```
6
7
8
6
```

### Uwagi o formatowaniu

* Nie wypisuj nagłówków typu „a)” i „b)”.
* Jeśli w którymś podpunkcie nie ma liczb do wypisania, w tej części nie wypisuj nic.
* Nie dodawaj pustej linii między podpunktami.

*/

const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Porownanie ze zmienna
const min = Math.min(liczba_a, liczba_b);
const max = Math.max(liczba_a, liczba_b);

// Petla
for (let i = min + 1; i < max; i++) {
  console.log(i);
}

// Petla
for (let i = min + 1; i < max; i++) {
  if (i % 3 === 0) {
    console.log(i);
  }
}

