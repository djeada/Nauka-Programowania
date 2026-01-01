/*
ZAD-12 — Porównanie dwóch słowników z listami (kolejność list bez znaczenia)

**Poziom:** ★★☆
**Tagi:** `dict`, `porównanie`, `list`

### Treść

Wczytaj dwa „słowniki” (opis w wejściu). Dla każdego klucza wartościami są listy liczb całkowitych, ale **kolejność w listach nie ma znaczenia**.
Wypisz `Prawda` jeśli słowniki są identyczne (te same klucze i te same wielozbiory wartości), w przeciwnym razie `Fałsz`.

### Wejście

* Najpierw:

  * 1 linia: `n`
  * następnie `n` linii: `klucz v1 v2 v3 ...` (co najmniej jedna wartość)
* Potem:

  * 1 linia: `m`
  * następnie `m` linii: `klucz v1 v2 v3 ...`

### Wyjście

* `Prawda` lub `Fałsz`

### Przykład

**Wejście:**

```
2
a 1 2 3
b 4 5
2
a 3 2 1
b 5 4
```

**Wyjście:**

```
Prawda
```

*/

function czySlownikiSaIdentyczne(slownik1, slownik2) {
  // Sprawdzamy czy liczba par w slownikach jest taka sama
  if (Object.keys(slownik1).length !== Object.keys(slownik2).length) {
    return false;
  }

  // Dla kazdej pary w slowniku 1 sprawdzamy czy istnieje rownowazna w slowniku 2
  for (const [klucz, wartosci] of Object.entries(slownik1)) {
    if (!Object.prototype.hasOwnProperty.call(slownik2, klucz)) {
      return false;
    }

    // Sprawdzamy czy listy sa identyczne niezaleznie od kolejnosci
    const lista1 = wartosci.sort();
    const lista2 = slownik2[klucz].sort();
    if (
      lista1.length !== lista2.length ||
      !lista1.every((el, i) => el === lista2[i])
    ) {
      return false;
    }
  }

  return true;
}

function testCzySlownikiSaIdentyczne() {
  const slownik1 = {
    a: [1, 2, 3],
    b: [4, 5],
  };
  const slownik2 = {
    a: [3, 2, 1],
    b: [5, 4],
  };
  const wynik1 = czySlownikiSaIdentyczne(slownik1, slownik2);
  console.assert(wynik1 === true, "Blad testu 1");

  const slownik3 = {
    a: [1, 2, 3],
    b: [4, 5],
  };
  const slownik4 = {
    a: [3, 2, 1],
    b: [5, 4],
    c: [6, 7],
  };
  const wynik2 = czySlownikiSaIdentyczne(slownik3, slownik4);
  console.assert(wynik2 === false, "Blad testu 2");
}

testCzySlownikiSaIdentyczne();

