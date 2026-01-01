/*
ZAD-04 — Maksimum i minimum z dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `max`, `min`, `if`, `formatowanie`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Wypisz je w jednej linii w kolejności: **większa, potem mniejsza**, oddzielone pojedynczą spacją.
Jeśli `a = b`, wypisz `a b` (czyli dwie takie same liczby).

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia:
`max(a, b) min(a, b)`

### Przykłady

**Wejście:**

```
1
4
```

**Wyjście:**

```
4 1
```

**Wejście:**

```
5
5
```

**Wyjście:**

```
5 5
```

*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Porownanie ze zmienna
if (liczba_a > liczba_b) {
  console.log(liczba_a + " " + liczba_b);
} else {
  console.log(liczba_b + " " + liczba_a);
}

