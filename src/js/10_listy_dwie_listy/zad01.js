/*
ZAD-01 — Wypisanie elementów dwóch list na przemian

**Poziom:** ★☆☆
**Tagi:** `list`, `iteracja`

### Treść

Wczytaj dwie listy liczb całkowitych i wypisz ich elementy **na przemian**:
pierwszy z listy 1, pierwszy z listy 2, drugi z listy 1, drugi z listy 2, itd.

Jeśli listy mają różne długości, po wyczerpaniu krótszej listy dopisz pozostałe elementy dłuższej listy w tej samej kolejności.

### Wejście

* 1 linia: lista 1
* 2 linia: lista 2

### Wyjście

* 1 linia: elementy obu list wypisane na przemian, oddzielone przecinkami **bez spacji**

### Przykład

**Wejście:**

```
[5, 3, 7, 2]
[1, -2, 3]
```

**Wyjście:**

```
5,1,3,-2,7,3,2
```

*/

// Funkcja wypisujaca elementy dwoch list na przemian
function wypiszElementyNaPrzemian(lista1, lista2) {
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    if (i < lista1.length) {
      console.log(lista1[i]);
    }
    if (i < lista2.length) {
      console.log(lista2[i]);
    }
  }
}

// Testy
console.log("Test dla list [5, 3, 7, 2] oraz [1, -2, 3]:");
wypiszElementyNaPrzemian([5, 3, 7, 2], [1, -2, 3]);

