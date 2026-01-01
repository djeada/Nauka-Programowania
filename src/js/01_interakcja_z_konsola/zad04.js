/*
ZAD-04 — Podstawowe operacje arytmetyczne

**Poziom:** ★☆☆
**Tagi:** `arytmetyka`, `I/O`

### Treść

Wczytaj dwie liczby naturalne `a` i `b` i wypisz kolejno:

1. `a + b`
2. `a - b`
3. `a * b`
4. `a // b` (dzielenie całkowite)
5. `a % b`
6. `a^b`

### Wejście

* 1. linia: `a` (liczba całkowita)
* 2. linia: `b` (liczba całkowita)

### Wyjście

6 linii — wyniki działań w kolejności 1–6.

### Ograniczenia / gwarancje

* `a ≥ 0`
* `b > 0` (żeby dzielenie i modulo były poprawne)

### Przykład

**Wejście:**

```
3
2
```

**Wyjście:**

```
5
1
6
1
1
9
```

*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Wyswietlenie wynikow

// a) suma tych liczb
console.log(liczba_a + liczba_b);

// b) roznica pierwszej i drugiej liczby
console.log(liczba_a - liczba_b);

// c) iloczyn tych liczb
console.log(liczba_a * liczba_b);

// d) iloraz pierwszej liczby przez druga
console.log(Math.floor(liczba_a / liczba_b));

// e) reszta z dzielenia pierwszej liczby przez druga
console.log(liczba_a % liczba_b);

// f) pierwsza liczba podniesiona do potegi rownej drugiej liczbie
console.log(liczba_a ** liczba_b);

