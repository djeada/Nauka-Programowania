/*
ZAD-09 — Rozdziel informacje o pracowniku

**Poziom:** ★☆☆
**Tagi:** `split`, `formatowanie`

### Treść

Wczytaj linię z danymi pracownika rozdzielonymi średnikami `;`:

1. Imię, 2) Nazwisko, 3) Miejsce urodzenia, 4) Stanowisko, 5) Zarobki

Wypisz każdą informację w osobnej linii z etykietą.

### Wejście

* 1. linia: dane w formacie `Imię; Nazwisko; Miasto; Zawód; Zarobki;`

### Wyjście

Pięć linii w formacie:

* `Imię: ...`
* `Nazwisko: ...`
* `Miejsce urodzenia: ...`
* `Zawód: ...`
* `Zarobki: ...`

### Przykład

**Wejście:**

```
Jan; Kowalski; Warszawa; Programista; 1000;
```

**Wyjście:**

```
Imię: Jan
Nazwisko: Kowalski
Miejsce urodzenia: Warszawa
Zawód: Programista
Zarobki: 1000
```

### Uwagi

* Po `split(';')` usuń ewentualne spacje z brzegów pól (np. `strip()`).
* Ostatni średnik może powodować pusty element na końcu — zignoruj go.

*/

// Funkcja rozdziela informacje o pracowniku zapisane w jednej linii
// Złożoność czasowa: O(n), gdzie n to długość stringu rekord
// Złożoność pamięciowa: O(n) dla przechowania tablicy danych i wyniku
function rozdzielRekord(rekord) {
  let dane = rekord.split(";");
  let imie = dane[0].trim();
  let nazwisko = dane[1].trim();
  let miejsceUrodzenia = dane[2].trim();
  let zawod = dane[3].trim();
  let zarobki = dane[4].trim();

  let lista = [
    "Imię: " + imie,
    "Nazwisko: " + nazwisko,
    "Miejsce urodzenia: " + miejsceUrodzenia,
    "Zawód: " + zawod,
    "Zarobki: " + zarobki,
  ];
  return lista;
}

// Test

function test() {
  let input = "Jan; Kowalski; Warszawa; Programista; 1000;";
  let expectedOutput = [
    "Imię: Jan",
    "Nazwisko: Kowalski",
    "Miejsce urodzenia: Warszawa",
    "Zawód: Programista",
    "Zarobki: 1000",
  ];
  let output = rozdzielRekord(input);

  console.assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiodl sie"
  );
  console.log("Test przeszedl pomyslnie");
}

test();

