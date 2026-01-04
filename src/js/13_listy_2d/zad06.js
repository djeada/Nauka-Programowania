/*
ZAD-06 — Scalanie przedziałów

**Poziom:** ★★☆
**Tagi:** `sortowanie`, `przedziały`, `algorytmy`

### Treść

Wczytaj `n` przedziałów `[a_i, b_i]` (a_i ≤ b_i). Scal przedziały nachodzące na siebie i wypisz wynik w kolejności rosnącej po początku.

### Wejście

* 1. linia: `n`
* następnie `n` linii: `a_i b_i`

### Wyjście

* Każdy scalony przedział w osobnej linii: `a b`

### Przykład

**Wejście:**

```
7
23 67
23 53
45 88
77 88
10 22
11 12
42 45
```

**Wyjście:**

```
10 22
23 88
```

### Uwagi

* Przedziały uznajemy za nachodzące, gdy `next_start <= current_end`.

*/

function scalPrzedzialy(przedzialy) {
  przedzialy.sort((a, b) => a[0] - b[0]); // sortujemy przedzialy po poczatku

  const wynik = [przedzialy[0]]; // dodajemy pierwszy przedzial
  let ostatniPrzedzial = przedzialy[0];

  for (let i = 1; i < przedzialy.length; i++) {
    const aktualnyPrzedzial = przedzialy[i];
    if (aktualnyPrzedzial[0] <= ostatniPrzedzial[1]) {
      // przedzialy nachodza na siebie
      ostatniPrzedzial[1] = Math.max(ostatniPrzedzial[1], aktualnyPrzedzial[1]); // przedzialy sie nakladaja, laczymy je w jeden
    } else {
      // przedzialy nie nachodza na siebie
      wynik.push(aktualnyPrzedzial); // dodajemy przedzial do wyniku
      ostatniPrzedzial = aktualnyPrzedzial;
    }
  }

  return wynik;
}

// test
function test() {
  const przedzialy1 = [
    [23, 67],
    [23, 53],
    [45, 88],
    [77, 88],
    [10, 22],
    [11, 12],
    [42, 45],
  ];
  const wynik1 = [
    [10, 22],
    [23, 88],
  ];
  const przedzialy2 = [
    [1, 2],
    [3, 4],
    [5, 6],
  ];
  const wynik2 = [
    [1, 2],
    [3, 4],
    [5, 6],
  ];
  const przedzialy3 = [
    [1, 3],
    [2, 4],
    [5, 6],
  ];
  const wynik3 = [
    [1, 4],
    [5, 6],
  ];
  console.assert(
    JSON.stringify(scalPrzedzialy(przedzialy1)) === JSON.stringify(wynik1),
    `Niepoprawny wynik dla przedzialow ${przedzialy1}.`
  );
  console.assert(
    JSON.stringify(scalPrzedzialy(przedzialy2)) === JSON.stringify(wynik2),
    `Niepoprawny wynik dla przedzialow ${przedzialy2}.`
  );
  console.assert(
    JSON.stringify(scalPrzedzialy(przedzialy3)) === JSON.stringify(wynik3),
    `Niepoprawny wynik dla przedzialow ${przedzialy3}.`
  );
}

test();

