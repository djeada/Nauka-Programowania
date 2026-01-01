/*
ZAD-08 — Koszt pokrycia podłogi płytkami

**Poziom:** ★★☆
**Tagi:** `ceil`, `arytmetyka`, `formatowanie`, `geometria`

### Treść

Dane są:

* cena jednej płytki `p`,
* bok płytki `t` (płytka kwadratowa),
* długość podłogi `L`,
* szerokość podłogi `W`.

Oblicz liczbę płytek potrzebnych do pokrycia całej podłogi, zakładając układ bez docinania „na styk” (czyli wzdłuż każdego wymiaru zaokrąglasz w górę), a następnie podaj koszt całkowity.

### Wejście

4 liczby (każda w osobnej linii): `p`, `t`, `L`, `W`

### Wyjście

Jedna liczba: całkowity koszt do **2 miejsc po przecinku**.

### Ograniczenia / gwarancje

* `p > 0`, `t > 0`, `L > 0`, `W > 0`
* Liczba płytek:

  * `nL = ceil(L / t)`
  * `nW = ceil(W / t)`
  * `n = nL * nW`
* Koszt: `n * p`

### Przykład

**Wejście:**

```
2
3
20
40
```

**Wyjście:**

```
196.00
```

*/

// Pobieranie danych od uzytkownika

const cena_plytki = parseInt(prompt("Podaj cene plytki:"));
const dlugosc_boku_plytki = parseInt(prompt("Podaj dlugosc boku plytki:"));
const dlugosc_podlogi = parseInt(prompt("Podaj dlugosc podlogi:"));
const szerokosc_podlogi = parseInt(prompt("Podaj szerokosc podlogi:"));

// Obliczanie wymiarow podlogi
const wymiary_podlogi = dlugosc_podlogi * szerokosc_podlogi;
const wymiary_plytki = dlugosc_boku_plytki ** 2;

// Obliczanie ilosci plytek
const ilosc_plytek = wymiary_podlogi / wymiary_plytki;

// Obliczanie ceny podlogi
const cena_podlogi = ilosc_plytek * cena_plytki;

// Wypisanie wyniku
console.log(cena_podlogi);

