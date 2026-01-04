/*
ZAD-08 — Iloraz w dół bez / i %

**Poziom:** ★★☆
**Tagi:** `funkcje`, `pętle`, `odejmowanie`

### Treść

Napisz funkcję `zaokraglij_w_dol(a, b)`, która zwraca wartość `a // b`, ale **nie używa** operatorów `/` ani `%`.

### Wejście

Dwa argumenty:

* `a` (liczba naturalna, `a ≥ 0`)
* `b` (liczba naturalna)

### Ograniczenia / gwarancje

* `b > 0`

### Wyjście

Funkcja zwraca liczbę naturalną — iloraz `a` przez `b` zaokrąglony w dół.

### Przykład

**Wywołanie funkcji:**

```python
print(zaokraglij_w_dol(7, 2))
```

**Wyjście:**

```
3
```

*/

const podziel = (liczba1, liczba2) => {
  if (liczba2 === 0) return NaN;

  let iloraz = 0;
  let suma = 0;
  let kierunek = liczba1 < 0 === liczba2 < 0 ? 1 : -1;
  let liczba1Abs = Math.abs(liczba1);
  let liczba2Abs = Math.abs(liczba2);

  while (suma + liczba2Abs <= liczba1Abs) {
    suma += liczba2Abs;
    iloraz++;
  }

  return iloraz * kierunek;
};

// Pobieranie danych od uzytkownika
const liczba1 = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba2 = parseInt(prompt("Podaj druga liczbe:"));

// Wypisanie wyniku
console.log(podziel(liczba1, liczba2));

