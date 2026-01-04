/*
ZAD-02 — Wszystkie permutacje słowa

**Poziom:** ★★☆
**Tagi:** `rekurencja`, `permutacje`, `backtracking`

### Treść

Wczytaj słowo z **unikalnych liter** i wypisz wszystkie jego permutacje — każdą w osobnej linii.

### Wejście

* 1. linia: słowo (litery nie powtarzają się)

### Wyjście

Wiele linii — wszystkie permutacje słowa, każda w osobnej linii.

### Przykład

**Wejście:**

```
abc
```

**Wyjście:**

```
abc
acb
bac
bca
cab
cba
```

### Uwagi o formatowaniu

* Kolejność wypisywania permutacji nie musi być dokładnie taka jak w przykładzie, o ile są wszystkie i bez powtórzeń.

*/

function permutacje(slowo) {
  if (slowo.length <= 1) {
    return [slowo];
  }

  const wynik = [];
  for (let i = 0; i < slowo.length; i++) {
    const pierwszyZnak = slowo[i];
    const pozostaleZnaki = slowo.slice(0, i) + slowo.slice(i + 1);
    const permutacjePozostałych = permutacje(pozostaleZnaki);

    for (const perm of permutacjePozostałych) {
      wynik.push(pierwszyZnak + perm);
    }
  }

  return wynik;
}

// Test
function test() {
  const input = "abc";
  const expectedOutput = ["abc", "acb", "bac", "bca", "cab", "cba"];
  const output = permutacje(input);

  // Sortujemy obie tablice dla porównania
  const outputSorted = output.sort();
  const expectedSorted = expectedOutput.sort();

  console.assert(
    JSON.stringify(outputSorted) === JSON.stringify(expectedSorted),
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedl pomyslnie");
}

test();
