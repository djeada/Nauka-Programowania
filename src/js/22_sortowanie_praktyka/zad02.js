/*
ZAD-02 — Sortowanie słów w zdaniu

**Poziom:** ★★☆
**Tagi:** `sort`, `string`, `split`

### Treść

Otrzymujesz zdanie. Podziel je na słowa, traktując znaki interpunkcyjne jako separatory, a następnie posortuj słowa alfabetycznie i wypisz listę.

### Wejście

* 1 linia: napis `zdanie`

### Wyjście

* 1 linia: lista słów w formacie jak w przykładzie, np. `['Ala', 'kota', 'ma']`

### Przykład

**Wejście:**

```
Lemur wygina śmiało ciało
```

**Wyjście:**

```
['Lemur', 'ciało', 'wygina', 'śmiało']
```

### Uwagi o formatowaniu

* Ignoruj znaki interpunkcyjne (np. `.,!?;:`) — nie są częścią słów.
* Wielkość liter pozostaje bez zmian (nie zamieniaj na małe/duże), sortujesz to, co w tekście.

*/

const sortowanieSlow = (napis) => {
  return napis.split(" ").sort((a, b) => a.localeCompare(b));
};

// Testy
const napis1 = "Lemur wygina smialo cialo";
const wynik1 = ["Lemur", "cialo", "smialo", "wygina"];
const napis2 = "Ala ma kota a kot ma Ale";
const wynik2 = ["Ala", "Ale", "a", "kot", "kota", "ma", "ma"];

console.assert(
  JSON.stringify(sortowanieSlow(napis1)) === JSON.stringify(wynik1),
  "Test 1 nieudany"
);
console.assert(
  JSON.stringify(sortowanieSlow(napis2)) === JSON.stringify(wynik2),
  "Test 2 nieudany"
);

