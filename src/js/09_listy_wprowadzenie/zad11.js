/*
ZAD-11 — Samochody jadące w przeciwnych kierunkach

**Poziom:** ★★☆
**Tagi:** `listy`, `zliczanie`, `string`

### Treść

Wczytaj `N` oraz napis długości `N` złożony z liter `A` i `B`:

* `A` oznacza samochód jadący na wschód,
* `B` oznacza samochód jadący na zachód.

Policz, ile par samochodów minie się, gdy uznamy, że para mija się wtedy, gdy `A` stoi **przed** `B` w ciągu.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* 2. linia: napis długości `N`, tylko `A` i `B` (bez spacji)

### Wyjście

Jedna liczba naturalna — liczba mijających się par.

### Przykład

**Wejście:**

```
5
ABABB
```

**Wyjście:**

```
5
```

*/

function liczbaMijajacychSieSamochodow(listaSamochodow) {
  var samochodyA = 0;
  var liczbaMijajacych = 0;

  for (var i = 0; i < listaSamochodow.length; i++) {
    if (listaSamochodow[i] === "A") {
      samochodyA++;
    } else if (listaSamochodow[i] === "B") {
      liczbaMijajacych += samochodyA;
    }
  }

  return liczbaMijajacych;
}

// Testy

function testLiczbaMijajacychSieSamochodow() {
  console.assert(
    liczbaMijajacychSieSamochodow(["A", "B", "A", "B", "B"]) === 5
  );
  console.assert(
    liczbaMijajacychSieSamochodow(["A", "A", "A", "B", "B"]) === 6
  );
  console.assert(
    liczbaMijajacychSieSamochodow(["A", "B", "A", "A", "B"]) === 4
  );
  console.assert(
    liczbaMijajacychSieSamochodow(["B", "B", "A", "A", "A"]) === 0
  );
  console.assert(
    liczbaMijajacychSieSamochodow(["A", "A", "A", "A", "A"]) === 0
  );
}

testLiczbaMijajacychSieSamochodow();

