/*
ZAD-08 — Połącz posortowane listy w posortowaną listę bez duplikatów

**Poziom:** ★★☆
**Tagi:** `list`, `merge`, `sort`

### Treść

Wczytaj dwie listy liczb całkowitych, każda **posortowana rosnąco**. Połącz je w jedną listę:

* wynik ma być posortowany rosnąco,
* wynik ma zawierać **unikalne** elementy (bez duplikatów).

### Wejście

* 1 linia: lista 1 (posortowana rosnąco)
* 2 linia: lista 2 (posortowana rosnąco)

### Wyjście

* 1 linia: jedna posortowana lista bez duplikatów

### Przykład

**Wejście:**

```
[2, 4, 7]
[3, 5, 9]
```

**Wyjście:**

```
[2, 3, 4, 5, 7, 9]
```

*/

// Funkcja zwracajaca liste elementow, ktore nie sa czescia wspolna obu list
function polaczPosortowaneListy(lista1, lista2) {
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

function testPolaczPosortowaneListy() {
  console.assert(
    polaczPosortowaneListy([2, 4, 7], [3, 5, 9]).toString() ===
      [2, 3, 4, 7, 9].toString()
  );
  console.assert(
    polaczPosortowaneListy([2, 4, 7], [3, 5, 9, 2]).toString() ===
      [2, 3, 4, 7, 9].toString()
  );
  console.assert(
    polaczPosortowaneListy([2, 4, 7], [3, 5, 9, 2, 4]).toString() ===
      [2, 3, 4, 7, 9].toString()
  );
  console.assert(
    polaczPosortowaneListy([2, 4, 7], [3, 5, 9, 2, 4, 7]).toString() ===
      [2, 3, 4, 7, 9].toString()
  );
}

testPolaczPosortowaneListy();

