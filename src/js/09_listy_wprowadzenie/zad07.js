/*
ZAD-07 — Średnia dwóch największych liczb

**Poziom:** ★☆☆
**Tagi:** `listy`, `max`, `sortowanie`, `float`

### Treść

Wczytaj `N` liczb naturalnych (`N ≥ 2`). Znajdź największą i drugą największą wartość, a następnie wypisz ich średnią arytmetyczną jako liczbę zmiennoprzecinkową z dokładnością do **jednego** miejsca po przecinku.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba zmiennoprzecinkowa w formacie `%.1f`.

### Przykład

**Wejście:**

```
6
9
2
3
2
1
7
```

**Wyjście:**

```
8.0
```

*/

function liczbaMniejszaOdNajwiekszej(lista) {
  let max = lista[0];
  let secondMax = lista[0];
  for (let i = 1; i < lista.length; i++) {
    if (lista[i] > max) {
      secondMax = max;
      max = lista[i];
    } else if (lista[i] > secondMax) {
      secondMax = lista[i];
    }
  }
  return (max + secondMax) / 2;
}

// Testy

function testLiczbaMniejszaOdNajwiekszej() {
  console.assert(liczbaMniejszaOdNajwiekszej([9, 2, 3, 2, 1, 7]) === 8.0);
  console.assert(liczbaMniejszaOdNajwiekszej([1, 2, 3, 4, 5, 6]) === 5.5);
  console.assert(liczbaMniejszaOdNajwiekszej([6, 5, 4, 3, 2, 1]) === 3.5);
}

function main() {
  testLiczbaMniejszaOdNajwiekszej();
}

main();

