/*
ZAD-08 — Usuń klucz

**Poziom:** ★☆☆
**Tagi:** `listy`, `remove`, `wyszukiwanie`

### Treść

Wczytaj listę liczb całkowitych oraz `klucz`. Usuń **pierwsze** wystąpienie `klucz` (jeśli istnieje). Następnie wypisz listę po modyfikacji w jednej linii, elementy oddzielone przecinkami.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* ostatnia linia: `klucz` (liczba całkowita)

### Wyjście

Jedna linia: lista po usunięciu, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
5
6
2
1
4
27
4
```

**Wyjście:**

```
6,2,1,27
```

### Uwagi

* Jeśli `klucz` nie występuje, wypisz listę bez zmian.

*/

function usunKlucz(lista, klucz) {
  let wynik = [];
  let czyZnaleziono = false;
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === klucz && !czyZnaleziono) {
      czyZnaleziono = true;
    } else {
      wynik.push(lista[i]);
    }
  }
  return wynik;
}

// Testy

function testUsunKlucz() {
  console.assert(
    usunKlucz([6, 2, 1, 4, 27], 4).toString() === [6, 2, 1, 27].toString()
  );
  console.assert(
    usunKlucz([6, 2, 1, 4, 27], 6).toString() === [2, 1, 4, 27].toString()
  );
  console.assert(
    usunKlucz([6, 2, 1, 4, 27], 27).toString() === [6, 2, 1, 4].toString()
  );
}

function main() {
  testUsunKlucz();
}

main();

