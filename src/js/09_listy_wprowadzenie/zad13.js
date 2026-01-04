/*
ZAD-13 — Brakujący element w ciągu arytmetycznym

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `ciąg arytmetyczny`, `listy`

### Treść

Wczytaj `N` liczb naturalnych. Lista jest fragmentem ciągu arytmetycznego z **jednym brakującym elementem**. Znajdź i wypisz brakującą wartość.

### Wejście

* 1. linia: `N` (`N ≥ 2`)
* kolejne `N` linii: liczby naturalne

### Wyjście

Jedna liczba naturalna — brakujący element.

### Przykład

**Wejście:**

```
4
5
2
1
3
```

**Wyjście:**

```
4
```

*/

function znajdzBrakujacyElement(lista) {
  const n = lista.length + 1;
  const sumaKolejnychLiczb = (n * (n + 1)) / 2;
  const sumaListy = lista.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    0
  );
  return sumaKolejnychLiczb - sumaListy;
}

// Testy

function testZnajdzBrakujacyElement() {
  console.assert(znajdzBrakujacyElement([5, 2, 1, 3]) === 4);
  console.assert(znajdzBrakujacyElement([1, 3, 4, 5, 6]) === 2);
  console.assert(znajdzBrakujacyElement([1, 2, 4]) === 3);
  console.assert(znajdzBrakujacyElement([3, 5, 6, 7, 8]) === 4);
}

testZnajdzBrakujacyElement();

