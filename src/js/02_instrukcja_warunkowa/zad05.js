/*
ZAD-05 — Sortowanie trzech liczb

**Poziom:** ★★☆
**Tagi:** `sort`, `warunki`, `porządkowanie`

### Treść

Wczytaj trzy liczby naturalne `a`, `b`, `c` i wypisz je w kolejności rosnącej.

### Wejście

* 1 linia: `a` (całkowita, `a ≥ 0`)
* 2 linia: `b` (całkowita, `b ≥ 0`)
* 3 linia: `c` (całkowita, `c ≥ 0`)

### Wyjście

Jedna linia: trzy liczby rosnąco, oddzielone pojedynczymi spacjami.

### Przykład

**Wejście:**

```
2
1
4
```

**Wyjście:**

```
1 2 4
```

### Uwagi

* Możesz użyć wbudowanego sortowania, ale da się też rozwiązać czystymi warunkami.

*/

// Pobieranie danych od uzytkownika
const liczba_a = parseInt(prompt("Podaj pierwsza liczbe:"));
const liczba_b = parseInt(prompt("Podaj druga liczbe:"));
const liczba_c = parseInt(prompt("Podaj trzecia liczbe:"));

// Porownanie ze zmienna
const liczby = [liczba_a, liczba_b, liczba_c].sort((a, b) => a - b);
console.log(liczby[0] + " " + liczby[1] + " " + liczby[2]);

