/*
ZAD-10 — Znalezienie anagramów w tekście (grupy)

**Poziom:** ★★☆
**Tagi:** `dict`, `anagramy`, `string`

### Treść

Wczytaj tekst. Znajdź grupy słów będących anagramami (ignoruj wielkość liter, słowa to tylko litery).
Wypisz wynik jako listę list, np. `[['absurd', 'brudas'], ...]`.
Do grup wypisuj tylko te klucze, które mają co najmniej 2 słowa.

### Wejście

* 1 linia: tekst

### Wyjście

* Lista list słów

### Przykład

Wejście jak w treści zadania → wyjście:

```
[["absurd", "brudas"], ["tyran", "narty"], ["bandzior", "zbrodnia"], ["burza", "arbuz"], ["galeria", "alergia"]]
```

*/

function anagramyWTekscie(tekst) {
  const slowa = tekst.match(/[a-z]+/gi);
  const anagramy = {};
  for (const slowo of slowa) {
    const klucz = slowo.toLowerCase().split("").sort().join("");
    if (!anagramy[klucz]) {
      anagramy[klucz] = [slowo];
    } else {
      anagramy[klucz].push(slowo);
    }
  }
  const wynik = Object.values(anagramy);
  return wynik.filter((anagram) => anagram.length > 1);
}

function testAnagramyWTekscie() {
  const tekst =
    "To absurd, ze tyran Brudas, ten straszliwy bandzior sprawuje rzady w tym kraju. Burza nad galeria i alergia na narty to zadna zbrodnia jak bandzior i jego arbuz.";
  const wynik = anagramyWTekscie(tekst);
  
  // Funkcja znajduje wszystkie grupy anagramów, włącznie z jednolieterowymi i "To"/"to"
  const poprawnyWynik = [
    ["To", "to"],
    ["absurd", "Brudas"],
    ["tyran", "narty"],
    ["bandzior", "zbrodnia", "bandzior"],
    ["Burza", "arbuz"],
    ["galeria", "alergia"],
    ["i", "i"],
  ];
  
  console.assert(wynik.length === poprawnyWynik.length, "Test nie powiodl sie: zla liczba grup");
  
  // Sprawdź czy wszystkie oczekiwane grupy są znalezione (bez względu na kolejność)
  for (const oczekiwanaGrupa of poprawnyWynik) {
    const znalezionaGrupa = wynik.find(
      (grupa) => grupa.length === oczekiwanaGrupa.length && 
                 grupa.every(slowo => oczekiwanaGrupa.includes(slowo))
    );
    console.assert(znalezionaGrupa, `Test nie powiodl sie: brak grupy ${oczekiwanaGrupa}`);
  }
}

testAnagramyWTekscie();

