/*
ZAD-03 — Z ilu słów składa się zdanie?

**Poziom:** ★☆☆
**Tagi:** `string`, `split`

### Treść

Wczytaj zdanie i policz, z ilu słów się składa. Znaki interpunkcyjne nie są słowami.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: liczba słów

### Przykład

**Wejście:**

```
gram na pianinie.
```

**Wyjście:**

```
3
```

### Uwagi o formatowaniu

* Najprościej: podziel po białych znakach, a z końców słów usuń interpunkcję.

*/
// Funkcja liczy słowa w zdaniu (interpunkcja nie jest słowem)
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(m), gdzie m to liczba słów
function policzSlowa(zdanie) {
  let slowa = zdanie.split(" ");
  let liczbaSlow = 0;
  for (let i = 0; i < slowa.length; i++) {
    let slowo = slowa[i].replace(/[.,/#!$%&;:{}=\-_`~()]/g, "");
    if (slowo.length > 0) {
      liczbaSlow++;
    }
  }
  return liczbaSlow;
}

// Testy

function test() {
  let input = "gram na pianinie.";
  let expectedOutput = 3;
  let output = policzSlowa(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

