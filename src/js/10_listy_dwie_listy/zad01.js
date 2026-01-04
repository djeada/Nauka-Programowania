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

function wypiszElementyNaPrzemian(lista1, lista2) {
  const wynik = [];
  const maxLength = Math.max(lista1.length, lista2.length);
  
  for (let i = 0; i < maxLength; i++) {
    if (i < lista1.length) {
      wynik.push(lista1[i]);
    }
    if (i < lista2.length) {
      wynik.push(lista2[i]);
    }
  }
  
  console.log(wynik.join(","));
}

// Pobieranie danych od uzytkownika
const lista1 = JSON.parse(prompt("Podaj liste 1:"));
const lista2 = JSON.parse(prompt("Podaj liste 2:"));

// Wywolanie funkcji
wypiszElementyNaPrzemian(lista1, lista2);

