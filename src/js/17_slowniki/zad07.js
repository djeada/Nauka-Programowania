/*
ZAD-07 — Histogram słów w tekście (ignoruj wielkość liter)

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`, `tekst`

### Treść

Wczytaj tekst. Policz częstość występowania słów (tylko litery), ignorując wielkość liter. Wypisz słownik: słowo (małe litery) → liczba wystąpień.

### Wejście

* 1 linia: tekst

### Wyjście

* Słownik

### Przykład

**Wejście:**

```
Ala ma kota. Ala lubi koty.
```

**Wyjście:**

```
{'ala': 2, 'ma': 1, 'kota': 1, 'lubi': 1, 'koty': 1}
```

*/

function histogramSlow(napis) {
  const slowa = napis.toLowerCase().match(/\b\w+\b/g);
  const slownik = {};
  for (let i = 0; i < slowa.length; i++) {
    const slowo = slowa[i];
    if (slownik[slowo]) {
      slownik[slowo]++;
    } else {
      slownik[slowo] = 1;
    }
  }
  return slownik;
}

function testHistogramSlow() {
  const napis1 =
    "Here, a tricksy corpus will exist; a very strange, a sometimes cryptic corpus will dumbfound you maybe, perhaps a bit; in particular since my tricksy corpus will not match the pattern you expect from it; nor will it look like a fish, a boat, a sunflower, or a very handsome kitten. The tricksy corpus will surprise a user named Ami Tavory; this tricksy corpus will be fun to follow a year or a month or a minute from now.";
  const wynik1 = histogramSlow(napis1);
  console.assert(wynik1["here"] === 1, "Test 1 nie powiodl sie");
  console.assert(wynik1["a"] === 12, "Test 2 nie powiodl sie");
  console.assert(wynik1["tricksy"] === 4, "Test 3 nie powiodl sie");
  console.assert(wynik1["corpus"] === 5, "Test 4 nie powiodl sie");
  console.assert(wynik1["will"] === 6, "Test 5 nie powiodl sie");

  const napis2 = "Ala ma kota, a kot ma Ale.";
  const wynik2 = histogramSlow(napis2);
  console.assert(wynik2["ala"] === 2, "Test 6 nie powiodl sie");
  console.assert(wynik2["ma"] === 2, "Test 7 nie powiodl sie");
  console.assert(wynik2["kota"] === 1, "Test 8 nie powiodl sie");
}

testHistogramSlow();

