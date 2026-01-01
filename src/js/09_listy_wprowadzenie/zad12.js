/*
ZAD-12 — Rotacja w lewo / prawo

**Poziom:** ★★☆
**Tagi:** `listy`, `rotacja`, `modulo`

### Treść

Wczytaj listę liczb całkowitych, a następnie:

* `kierunek = 0` → rotacja w lewo,
* `kierunek = 1` → rotacja w prawo,

o `K` pozycji (gdzie `K ≥ 0`). Wypisz listę po rotacji, przecinkami bez spacji.

### Wejście

* 1. linia: `N` (`N ≥ 1`)
* kolejne `N` linii: liczby całkowite
* kolejna linia: `kierunek` (0 lub 1)
* ostatnia linia: `K` (`K ≥ 0`)

### Wyjście

Jedna linia: lista po rotacji, elementy oddzielone przecinkami.

### Przykład

**Wejście:**

```
7
5
27
6
2
1
10
8
0
2
```

**Wyjście:**

```
6,2,1,10,8,5,27
```

### Uwagi

* Zredukuj `K` przez `K % N`.

*/

// Funkcja rotujaca elementy listy o podana liczbe miejsc
function rotacjaListy(lista, kierunek, przesuniecie) {
  przesuniecie %= lista.length;

  if (kierunek === 1) {
    // Rotacja w prawo
    return lista.slice(-przesuniecie).concat(lista.slice(0, -przesuniecie));
  } else {
    // Rotacja w lewo
    return lista.slice(przesuniecie).concat(lista.slice(0, przesuniecie));
  }
}

// Testy

function testRotacjaListy() {
  const lista1 = [5, 27, 6, 2, 1, 10, 8];
  console.assert(
    JSON.stringify(rotacjaListy(lista1, 0, 2)) ===
      JSON.stringify([6, 2, 1, 10, 8, 5, 27])
  );
  console.assert(
    JSON.stringify(rotacjaListy(lista1, 1, 2)) ===
      JSON.stringify([10, 8, 5, 27, 6, 2, 1])
  );
}

testRotacjaListy();

