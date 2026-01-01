/*
ZAD-09 — Usuń z pierwszej listy część wspólną obu list

**Poziom:** ★★☆
**Tagi:** `list`, `filter`

### Treść

Wczytaj dwie listy liczb całkowitych. Usuń z pierwszej listy wszystkie elementy, które występują również w drugiej liście.

* Zachowaj kolejność pozostałych elementów z pierwszej listy.
* Jeśli wszystko zostanie usunięte — wypisz `[]`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista 1 po usunięciu elementów wspólnych

### Przykład

**Wejście:**

```
[9, 2, 5, 4]
[4, 2, 1]
```

**Wyjście:**

```
[9, 5]
```

*/

// Funkcja zwracajaca liste elementow, ktore nie sa czescia wspolna obu list
function usunCzescWspolna(lista1, lista2) {
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

function testUsunCzescWspolna() {
  console.assert(
    usunCzescWspolna([9, 2, 5, 4], [4, 2, 1]).toString() === [9, 5].toString()
  );
  console.assert(
    usunCzescWspolna([9, 2, 5, 4], [4, 2, 1, 9]).toString() === [5].toString()
  );
  console.assert(
    usunCzescWspolna([9, 2, 5, 4], [4, 2, 1, 9, 5]).toString() ===
      [1].toString()
  );
  console.assert(
    usunCzescWspolna([9, 2, 5, 4], [4, 2, 1, 9, 5, 2]).toString() ===
      [1].toString()
  );
}

testUsunCzescWspolna();

