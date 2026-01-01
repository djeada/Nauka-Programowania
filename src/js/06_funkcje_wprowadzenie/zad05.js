/*
ZAD-05 — Zamiana wartości miejscami

**Poziom:** ★☆☆
**Tagi:** `funkcje`, `krotka`, `zmienne`

### Treść

Napisz funkcję `zamien_wartosci(a, b)`, która zamienia wartości miejscami i zwraca je jako parę `(b, a)`.

### Wejście

Dwa argumenty: `a`, `b` (liczby naturalne)

### Wyjście

Dwie liczby naturalne zwrócone jako krotka / para:

* najpierw nowa wartość `a` (czyli stare `b`)
* potem nowa wartość `b` (czyli stare `a`)

### Przykład

**Wywołanie funkcji:**

```python
a, b = zamien_wartosci(8, 5)
print("a =", a)
print("b =", b)
```

**Wyjście:**

```
a = 5
b = 8
```

*/

// Funkcja zamieniajaca wartosci zmiennych
function zamienWartosciMiejscami(liczba_a, liczba_b) {
  let a = liczba_a;
  let b = liczba_b;
  let c = a;
  a = b;
  b = c;
  return [a, b];
}

// Pobieranie danych od uzytkownika
const a = parseInt(prompt("Podaj liczbe a:"));
const b = parseInt(prompt("Podaj liczbe b:"));

// Wywolanie funkcji
const wynik = zamienWartosciMiejscami(a, b);

// Wyswietlanie wyniku
console.log(wynik);

