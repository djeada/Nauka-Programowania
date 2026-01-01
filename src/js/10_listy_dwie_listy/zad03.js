/*
ZAD-03 — Suma elementów dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i zwróć listę, w której element o indeksie `i` jest sumą elementów o indeksie `i` z obu list.
Jeśli któraś lista jest krótsza, brakujące elementy traktuj jako `0`.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: lista sum

### Przykład

**Wejście:**

```
[3, 1, 2, 5]
[2, 8, 6, 5]
```

**Wyjście:**

```
[5, 9, 8, 10]
```

*/

// Funkcja zwracajaca liste, ktorej elementy sa suma odpowiadajacych sobie elementow obu list
function sumaElementowList(lista1, lista2) {
  let wynik = [];
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    let element1 = lista1[i] || 0;
    let element2 = lista2[i] || 0;
    wynik.push(element1 + element2);
  }

  return wynik;
}

// Testy

function testSumaElementowList() {
  console.assert(
    sumaElementowList([3, 1, 2, 5], [2, 8, 6, 5]).toString() ===
      [5, 9, 8, 10].toString()
  );
  console.assert(
    sumaElementowList([3, 1, 2, 5], [2, 8, 6]).toString() ===
      [5, 9, 8, 5].toString()
  );
  console.assert(
    sumaElementowList([3, 1, 2], [2, 8, 6, 5]).toString() ===
      [5, 9, 8, 5].toString()
  );
  console.assert(
    sumaElementowList([3, 1, 2, 5], [2, 8, 6, 5, 1]).toString() ===
      [5, 9, 8, 10, 1].toString()
  );
}

testSumaElementowList();

