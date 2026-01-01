/*
ZAD-01 — Warunek kończący pętlę

**Poziom:** ★☆☆
**Tagi:** `while`, `break`, `I/O`

### Treść

Wczytuj kolejne liczby naturalne, dopóki nie pojawi się liczba `7`.
Po wczytaniu liczby `7` program kończy działanie **bez wypisywania czegokolwiek**.

### Wejście

Dowolna liczba liczb naturalnych (każda w osobnej linii).

### Ograniczenia / gwarancje

* W danych wejściowych na pewno pojawi się co najmniej jedna liczba `7`.

### Wyjście

Brak.

### Przykład

**Wejście:**

```
3
10
5
7
```

**Wyjście:**

```
```

*(brak danych wyjściowych)*

### Uwagi o formatowaniu

* Nie wypisuj żadnych komunikatów typu „Podaj liczbę”.
* Liczba `7` kończy wczytywanie i nie jest dalej przetwarzana.

*/

// Pobieranie danych od uzytkownika
let liczba = parseInt(prompt("Podaj liczbe:"));

// Warunek konczacy petle
while (liczba !== 7) {
  liczba = parseInt(prompt("Podaj liczbe:"));
}

