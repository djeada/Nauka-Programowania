/*
ZAD-03 — Sprawdzanie warunków logicznych

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `bool`, `warunki`

### Treść

Napisz funkcję `sprawdz_warunki(a, b)`, która dla dwóch liczb naturalnych zwraca cztery wartości logiczne (np. jako krotkę) odpowiadające warunkom:

a) Czy `a > b`?
b) Czy `a + b < 10`?
c) Czy obie liczby są nieparzyste?
d) Czy `max(a, b) < a^2`?

### Wejście

Dwa argumenty funkcji:

* `a` (liczba całkowita, `a ≥ 0`)
* `b` (liczba całkowita, `b ≥ 0`)

### Wyjście

Cztery wartości logiczne w kolejności a), b), c), d).

### Przykład

**Wywołanie funkcji:**

```python
A, B, C, D = sprawdz_warunki(3, 2)
print(A)
print(B)
print(C)
print(D)
```

**Wyjście:**

```
True
True
False
True
```

*/

function czyPierwszaWiekszaOdDrugiej(liczba_a, liczba_b) {
  return liczba_a > liczba_b;
}

// Funkcja sprawdzajaca czy suma liczb jest mniejsza niz 10
function czySumaMniejszaOd10(liczba_a, liczba_b) {
  return liczba_a + liczba_b < 10;
}

// Funkcja sprawdzajaca czy obie liczby sa nieparzyste
function czyObieNieparzyste(liczba_a, liczba_b) {
  return liczba_a % 2 !== 0 && liczba_b % 2 !== 0;
}

// Funkcja sprawdzajaca czy wieksza liczba jest mniejsza od pierwszej liczby podniesionej do kwadratu
function czyWiekszaMniejszaOdPierwszejDoKwadratu(liczba_a, liczba_b) {
  return Math.max(liczba_a, liczba_b) < Math.pow(liczba_a, 2);
}

// Pobieranie danych od uzytkownika
var liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
var liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Wyswietlanie wynikow
console.log(czyPierwszaWiekszaOdDrugiej(liczba_a, liczba_b) ? "True" : "False");
console.log(czySumaMniejszaOd10(liczba_a, liczba_b) ? "True" : "False");
console.log(czyObieNieparzyste(liczba_a, liczba_b) ? "True" : "False");
console.log(czyWiekszaMniejszaOdPierwszejDoKwadratu(liczba_a, liczba_b) ? "True" : "False");

