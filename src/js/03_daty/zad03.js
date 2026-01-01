/*
ZAD-03 — Rok przestępny

**Poziom:** ★☆☆
**Tagi:** `modulo`, `if`, `kalendarz`

### Treść

Wczytaj rok `y` i sprawdź, czy jest przestępny w kalendarzu gregoriańskim.

Wypisz:

* `Rok jest przestępny.`
* `Rok nie jest przestępny.`

### Wejście

* 1 linia: `y` (liczba całkowita, `y ≥ 0`)

### Wyjście

Jedna linia — odpowiedni komunikat.

### Definicja

Rok jest przestępny, gdy:

* jest podzielny przez 400 **lub**
* jest podzielny przez 4 i **nie** jest podzielny przez 100.

### Przykład

**Wejście:**

```
2100
```

**Wyjście:**

```
Rok nie jest przestępny.
```

*/

// Pobieranie danych od uzytkownika
const rok = parseInt(prompt("Podaj rok:"));

// Sprawdzenie, czy rok jest przestepny
if ((rok % 4 === 0 && rok % 100 !== 0) || rok % 400 === 0) {
  console.log("Rok jest przestepny");
} else {
  console.log("Rok nie jest przestepny");
}

