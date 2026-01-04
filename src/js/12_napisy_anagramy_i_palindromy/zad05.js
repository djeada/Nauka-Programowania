/*
ZAD-05 — Anagramy słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `anagram`, `string`, `zliczanie`

### Treść

Wczytaj zdanie oraz słowo-klucz. Wypisz wszystkie słowa ze zdania, które są anagramami słowa-klucza (ignoruj wielkość liter).

### Wejście

* 1. linia: zdanie
* 2. linia: słowo-klucz `k`

### Wyjście

Każde słowo ze zdania będące anagramem `k` — w osobnej linii (w kolejności występowania).

### Przykład

**Wejście:**

```
Sroga kara.
arak
```

**Wyjście:**

```
kara
```

### Uwagi

* Tak jak wyżej: usuń interpunkcję z brzegów słów.
* Porównuj np. posortowane litery w `lower()`.

*/

function czyAnagramy(slowo1, slowo2) {
  const slowo1Male = slowo1.toLowerCase();
  const slowo2Male = slowo2.toLowerCase();

  if (slowo1Male.length !== slowo2Male.length) {
    return false;
  }

  const posortowane1 = slowo1Male.split("").sort().join("");
  const posortowane2 = slowo2Male.split("").sort().join("");

  return posortowane1 === posortowane2;
}

// Funkcja znajduje wszystkie anagramy słowa-klucza w zdaniu
// Złożoność czasowa: O(n*m log m), gdzie n to liczba słów, m to długość słowa
// Złożoność pamięciowa: O(k), gdzie k to liczba anagramów
function anagramyWZdaniu(zdanie, kluczSlowo) {
  const slowa = zdanie.split(/\s+/);
  const anagramy = [];

  for (const slowo of slowa) {
    // Usuń interpunkcję z brzegów
    const czystoSlowo = slowo.replace(/^[^\w]+|[^\w]+$/g, "");
    if (czystoSlowo && czyAnagramy(czystoSlowo, kluczSlowo)) {
      anagramy.push(czystoSlowo);
    }
  }

  return anagramy;
}

// Test
function test() {
  const inputZdanie = "Sroga kara.";
  const inputSlowo = "arak";
  const expectedOutput = ["kara"];
  const output = anagramyWZdaniu(inputZdanie, inputSlowo);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    'Test nie powiodl sie dla "' +
      inputZdanie +
      '" i "' +
      inputSlowo +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedl pomyslnie");
}

test();
