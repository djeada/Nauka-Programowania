/*
ZAD-05 — Liczba dni w miesiącu (rok nieprzestępny)

**Poziom:** ★☆☆
**Tagi:** `if`, `tablice`, `walidacja`

### Treść

Wczytaj numer miesiąca `m`. Zakładając rok **nieprzestępny**, wypisz liczbę dni w tym miesiącu.
Jeśli `m` nie jest w zakresie 1–12, wypisz:
`Niepoprawny numer miesiąca.`

### Wejście

* 1 linia: `m` (liczba całkowita, `m ≥ 0`)

### Wyjście

* liczba dni (jedna linia) **albo**
* komunikat o błędzie (jedna linia)

### Przykład

**Wejście:**

```
2
```

**Wyjście:**

```
28
```

*/

// Pobieranie danych od uzytkownika
const miesiac = parseInt(prompt("Podaj miesiac:"));

// Sprawdzenie, czy liczba jest poprawna
if (miesiac >= 1 && miesiac <= 12) {
  // Sprawdzenie, ktory miesiac odpowiada liczbie
  if (
    miesiac === 1 ||
    miesiac === 3 ||
    miesiac === 5 ||
    miesiac === 7 ||
    miesiac === 8 ||
    miesiac === 10 ||
    miesiac === 12
  ) {
    console.log(31);
  } else if (
    miesiac === 4 ||
    miesiac === 6 ||
    miesiac === 9 ||
    miesiac === 11
  ) {
    console.log(30);
  } else {
    console.log(28);
  }
} else {
  console.log("Niepoprawny numer miesiąca.");
}

