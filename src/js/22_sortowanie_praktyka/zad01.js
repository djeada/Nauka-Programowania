/*
ZAD-01 — Sortowanie znaków w napisie

**Poziom:** ★☆☆
**Tagi:** `sort`, `string`

### Treść

Otrzymujesz napis. Posortuj alfabetycznie wszystkie jego znaki i wypisz wynikowy napis.

### Wejście

* 1 linia: napis `s`

### Wyjście

* 1 linia: napis `s` po posortowaniu znaków rosnąco (porównanie znaków jak w Pythonie / Unicode)

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
 Aaaaklmot
```

### Uwagi o formatowaniu

* Spacje też są znakami i biorą udział w sortowaniu (dlatego w przykładzie wyjście zaczyna się od spacji).

*/

const sortowanieZnakow = (napis) => {
  return napis
    .split("")
    .sort((a, b) => a.localeCompare(b))
    .join("");
};

// Testy
const napis1 = "Ala ma kota";
const wynik1 = " Aaaaklmot";
const napis2 = "Javascript";
const wynik2 = "Jaaaciprstv";
const napis3 = "zazolc";
const wynik3 = "azlozz";

console.assert(sortowanieZnakow(napis1) === wynik1, "Test 1 nieudany");
console.assert(sortowanieZnakow(napis2) === wynik2, "Test 2 nieudany");
console.assert(sortowanieZnakow(napis3) === wynik3, "Test 3 nieudany");

