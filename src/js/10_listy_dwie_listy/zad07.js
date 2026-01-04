/*
ZAD-07 — Różnica między dwoma listami

**Poziom:** ★☆☆
**Tagi:** `list`, `set`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz elementy, które występują **tylko w jednej** z list (różnica symetryczna).

* Kolejność elementów w wyniku może być **dowolna**.
* Jeśli wszystkie elementy są wspólne — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista elementów niewspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście (jedna z poprawnych odpowiedzi):**

```
[9, 5, 1]
```

*/

function znajdzRoznice(lista1, lista2) {
  let wynik = [];
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    let element1 = lista1[i] || 0;
    let element2 = lista2[i] || 0;
    if (element1 !== element2) {
      wynik.push(element1);
      wynik.push(element2);
    }
  }

  return wynik;
}

// Testy

function testZnajdzRoznice() {
  console.assert(
    znajdzRoznice([9, 2, 5, 4], [4, 2, 1]).toString() === [9, 5, 1].toString()
  );
  console.assert(
    znajdzRoznice([9, 2, 5, 4], [4, 2, 1, 9]).toString() === [5, 1].toString()
  );
  console.assert(
    znajdzRoznice([9, 2, 5, 4], [4, 2, 1, 9, 5]).toString() === [1].toString()
  );
  console.assert(
    znajdzRoznice([9, 2, 5, 4], [4, 2, 1, 9, 5, 2]).toString() ===
      [1].toString()
  );
}

testZnajdzRoznice();

