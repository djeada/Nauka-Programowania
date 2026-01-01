/*
ZAD-04 — Wspólny podciąg o największej długości (równe sumy)

**Poziom:** ★★★
**Tagi:** `list`, `prefix`, `hashmap`, `podciąg`

### Treść

Otrzymujesz dwie listy binarne `A` i `B` (zera i jedynki) o tej samej długości. Znajdź **maksymalną długość** podciągu (ciągłych elementów), dla którego suma elementów w podciągu z `A` jest równa sumie elementów w odpowiadającym podciągu z `B` (ten sam zakres indeksów).

### Wejście

* 1 linia: lista binarna `A`
* 2 linia: lista binarna `B` (tej samej długości)

### Wyjście

* 1 linia: maksymalna długość (liczba naturalna)

### Przykład

**Wejście:**

```
[0, 0, 1, 1, 1, 1]
[0, 1, 1, 0, 1, 0]
```

**Wyjście:**

```
5
```

*/

const wspolnyPodciagONajwiekszejSumie = (lista1, lista2) => {
  let max = 0;
  for (let i = 0; i < lista1.length; i++) {
    for (let j = i; j < lista1.length; j++) {
      let suma1 = 0;
      let suma2 = 0;
      for (let k = i; k <= j; k++) {
        suma1 += lista1[k];
        suma2 += lista2[k];
      }
      if (suma1 === suma2 && j - i + 1 > max) {
        max = j - i + 1;
      }
    }
  }
  return max;
};

// Testy
const lista1 = [0, 0, 1, 1, 1, 1];
const lista2 = [0, 1, 1, 0, 1, 0];
const wynik = 5;

console.assert(
  wspolnyPodciagONajwiekszejSumie(lista1, lista2) === wynik,
  "Test 1 nieudany"
);

