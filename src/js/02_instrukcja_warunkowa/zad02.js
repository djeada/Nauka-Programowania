/*
ZAD-02 — Porównanie dwóch liczb

**Poziom:** ★☆☆
**Tagi:** `if-else`, `równość`, `string`

### Treść

Wczytaj dwie liczby naturalne `a` i `b`.
Jeśli są równe, wypisz:
`Liczby są identyczne.`
W przeciwnym razie wypisz:
`Liczby są różne.`

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)

### Wyjście

Jedna linia — dokładnie jeden z komunikatów.

### Przykład 1

**Wejście:**

```
7
4
```

**Wyjście:**

```
Liczby są różne.
```

### Przykład 2

**Wejście:**

```
5
5
```

**Wyjście:**

```
Liczby są identyczne.
```

*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));

// Porownanie ze zmienna
if (liczba_a === liczba_b) {
  console.log("Liczby sa identyczne");
} else {
  console.log("Liczby sa rozne");
}

