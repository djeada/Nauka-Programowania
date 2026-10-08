/*
ZAD-04 — Wszystkie wystąpienia podnapisu

**Poziom:** ★★☆
**Tagi:** `string`, `substring`, `find`

### Treść

Otrzymujesz napis `S` i napis `W` (wzorzec). Znajdź **wszystkie** pozycje w `S`, od których zaczyna się wystąpienie `W`, i wypisz je w kolejności rosnącej.

Wystąpienia mogą na siebie nachodzić: w napisie `aaaa` wzorzec `aa` zaczyna się na pozycjach `0`, `1` i `2`.

### Wejście

* 1. linia: napis `S`
* 2. linia: wzorzec `W`

### Wyjście

Jedna linia: indeksy początków wszystkich wystąpień `W` w `S`, oddzielone pojedynczymi spacjami.
Jeśli `W` nie występuje w `S`, wypisz `Brak`.

### Ograniczenia

* `1 ≤ |S| ≤ 1000`
* `1 ≤ |W| ≤ 100`

### Przykład

**Wejście:**

```
abrakadabra
abra
```

**Wyjście:**

```
0 7
```

### Uwagi

* Spróbuj nie używać metod `find` ani `count`: dla każdej pozycji `i` od `0` do `len(S) - len(W)` sprawdź, czy od tego miejsca zaczyna się `W` — tak jak sprawdzałeś przedrostek w zadaniu ZAD-03.
* W przeciwieństwie do zadań ZAD-01 i ZAD-02 po znalezieniu wystąpienia **nie przeskakujemy** go — kolejną sprawdzaną pozycją jest `i + 1`.

*/
const linie = require("fs").readFileSync(0, "utf8").split("\n");
const napis = (linie[0] || "").replace(/\r$/, "");
const wzorzec = (linie[1] || "").replace(/\r$/, "");

// Indeksy wszystkich (także nachodzących) wystąpień wzorca w napisie.
// Indeksy liczone po znakach Unicode, tak jak w Pythonie.
// Złożoność czasowa: O(n * m), pamięciowa: O(n + m)
function wystapienia(napis, wzorzec) {
  const s = Array.from(napis);
  const w = Array.from(wzorzec);
  const pozycje = [];
  for (let i = 0; i + w.length <= s.length; i++) {
    let pasuje = true;
    for (let j = 0; j < w.length; j++) {
      if (s[i + j] !== w[j]) {
        pasuje = false;
        break;
      }
    }
    if (pasuje) {
      pozycje.push(i);
    }
  }
  return pozycje;
}

const pozycje = wystapienia(napis, wzorzec);
console.log(pozycje.length > 0 ? pozycje.join(" ") : "Brak");
