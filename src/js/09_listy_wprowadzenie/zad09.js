/*
ZAD-09 — Usuń duplikaty (z zachowaniem kolejności)

**Poziom:** ★☆☆
**Tagi:** `listy`, `duplikaty`, `set`

### Treść

Wczytaj listę liczb naturalnych i usuń duplikaty tak, aby każda liczba występowała tylko raz — **zachowując kolejność pierwszego wystąpienia**.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna linia: lista bez duplikatów, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
6
3
2
1
3
2
2
```

**Wyjście:**

```
3,2,1
```

*/

function usunDuplikaty(lista) {
  var wynik = [];

  for (var i = 0; i < lista.length; i++) {
    if (wynik.indexOf(lista[i]) === -1) {
      wynik.push(lista[i]);
    }
  }

  return wynik;
}

// Testy

function testUsunDuplikaty() {
  console.assert(
    usunDuplikaty([3, 2, 1, 3, 2, 2]).toString() === [3, 2, 1].toString()
  );
  console.assert(
    usunDuplikaty([1, 2, 3, 4, 5, 6]).toString() ===
      [1, 2, 3, 4, 5, 6].toString()
  );
  console.assert(
    usunDuplikaty([6, 5, 4, 3, 2, 1]).toString() ===
      [6, 5, 4, 3, 2, 1].toString()
  );
}

function main() {
  testUsunDuplikaty();
}

main();

