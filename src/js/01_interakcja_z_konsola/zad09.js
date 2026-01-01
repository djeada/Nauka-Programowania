/*
ZAD-09 — Kalkulator kredytowy (rata annuitetowa)

**Poziom:** ★★☆
**Tagi:** `finanse`, `float`, `formatowanie`

### Treść

Wczytaj:

* roczną stopę procentową `R` (w %),
* okres spłaty `Y` (w latach),
* kwotę kredytu `P`.

Oblicz miesięczną ratę `M` oraz całkowity koszt `C = M * n`, gdzie `n = 12 * Y`.

Dla `R > 0` użyj wzoru:
[
M = P \cdot \frac{r(1+r)^n}{(1+r)^n-1}
]
gdzie `r = R / (12*100)`.

Dla `R = 0` przyjmij:

* `M = P / n`.

### Wejście

3 liczby (w osobnych liniach):

1. `R` (float, `R ≥ 0`)
2. `Y` (int, `Y > 0`)
3. `P` (float, `P > 0`)

### Wyjście

Dwie linie (do **2 miejsc po przecinku**):

1. miesięczna rata `M`
2. całkowity koszt `C`

### Przykład

**Wejście:**

```
3.5
8
12000
```

**Wyjście:**

```
143.50
13776.00
```

*/

// Pobieranie danych od uzytkownika
const roczna_stopa_procentowa = parseFloat(
  prompt("Podaj roczna stope procentowa:")
);
const liczba_lat = parseInt(prompt("Podaj liczbe lat na splacenie kredytu:"));
const wysokosc_kredytu = parseInt(
  prompt("Podaj wysokosc udzielonego kredytu:")
);

// Obliczanie miesiecznej raty
const miesieczna_rata =
  (wysokosc_kredytu * (roczna_stopa_procentowa / 100)) / 12;

// Obliczanie calkowitego kosztu kredytu
const calkowity_koszt_kredytu = miesieczna_rata * liczba_lat * 12;

// Wypisanie wyniku
console.log(miesieczna_rata.toFixed(2));
console.log(calkowity_koszt_kredytu.toFixed(2));

