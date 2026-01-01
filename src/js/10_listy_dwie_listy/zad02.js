/*
ZAD-02 — Połączenie dwóch list

**Poziom:** ★☆☆
**Tagi:** `list`, `indeksy`, `concat`

### Treść

Wczytaj dwie listy liczb całkowitych i wykonaj niezależnie:

**a)** Połącz listy, doklejając drugą listę na koniec pierwszej.
**b)** W pierwszej liście **podmień** elementy o parzystych indeksach (0, 2, 4, …) elementami z drugiej listy o tych samych indeksach — o ile taki indeks istnieje w obu listach.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: wynik dla **a)** jako lista
* 2 linia: wynik dla **b)** jako lista

### Przykład

**Wejście:**

```
[1, 2, 3]
[4, 5, 6]
```

**Wyjście:**

```
[1, 2, 3, 4, 5, 6]
[4, 2, 6]
```

*/

function polaczListy(lista1, lista2) {
  var wynik = [];
  for (var i = 0; i < lista1.length; i++) {
    wynik.push(lista1[i]);
  }
  for (var j = 0; j < lista2.length; j++) {
    wynik.push(lista2[j]);
  }
  return wynik;
}

function polaczListy2(lista1, lista2) {
  var wynik = [];
  for (var i = 0; i < lista1.length || i < lista2.length; i++) {
    if (i % 2 === 0 && lista2[i] !== undefined) {
      wynik.push(lista2[i]);
    } else if (lista1[i] !== undefined) {
      wynik.push(lista1[i]);
    }
  }
  return wynik;
}

// Testy

function testPolaczListy() {
  console.assert(
    polaczListy([1, 2, 3], [4, 5, 6]).toString() ===
      [1, 2, 3, 4, 5, 6].toString()
  );
  console.assert(
    polaczListy([1, 2, 3], [4, 5, 6, 7, 8]).toString() ===
      [1, 2, 3, 4, 5, 6, 7, 8].toString()
  );
}

function testPolaczListy2() {
  console.assert(
    polaczListy2([1, 2, 3], [4, 5, 6]).toString() === [4, 2, 6].toString()
  );
  console.assert(
    polaczListy2([1, 2, 3], [4, 5, 6, 7, 8]).toString() === [4, 2, 6].toString()
  );
}

function main() {
  testPolaczListy();
  testPolaczListy2();
}

main();

