/*
ZAD-03A — Mnożenie przy pomocy dodawania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `dodawanie`, `mnożenie`

### Treść

Napisz funkcję `iloczyn(a, b)`, która oblicza `a * b` używając **tylko dodawania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna, `b ≥ 0`)

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a * b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloczyn(3, 2))
```

**Wyjście:**

```
6
```

ZAD-03B — Dzielenie całkowite przy pomocy odejmowania

**Poziom:** ★☆☆
**Tagi:** `pętle`, `odejmowanie`, `dzielenie`

### Treść

Napisz funkcję `iloraz(a, b)`, która oblicza `a // b` używając **tylko odejmowania** i pętli.

### Wejście

Dwa argumenty funkcji:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca jedną liczbę naturalną — `a // b`.

### Przykład

**Wywołanie funkcji:**

```python
print(iloraz(3, 2))
```

**Wyjście:**

```
1
```

*/

// Funkcja zwracajaca iloczyn dwoch liczb
function zwracajIloczynLiczb(liczba_a, liczba_b) {
  var wynik = 0;
  for (var i = 0; i < liczba_b; i++) {
    wynik += liczba_a;
  }
  return wynik;
}

// Funkcja zwracajaca iloraz dwoch liczb
function zwracajIlorazLiczb(liczba_a, liczba_b) {
  if (liczba_b === 0) {
    return NaN;
  }

  var wynik = 0;
  while (liczba_a >= liczba_b) {
    liczba_a -= liczba_b;
    wynik++;
  }
  return wynik;
}

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Wypisanie wynikow
console.log(zwracajIloczynLiczb(liczba_a, liczba_b));
console.log(zwracajIlorazLiczb(liczba_a, liczba_b));

