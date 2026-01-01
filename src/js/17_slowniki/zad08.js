/*
ZAD-08 — Najczęstsza litera w zdaniu

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj zdanie. Zignoruj spacje i znaki interpunkcyjne. Znajdź literę występującą najczęściej.
Jeśli jest kilka, wybierz tę, która **pojawia się jako pierwsza w zdaniu**.

### Wejście

* 1 linia: zdanie

### Wyjście

* 1 znak

### Przykład

**Wejście:**

```
lezy jerzy na wiezy
```

**Wyjście:**

```
e
```

*/

function najczestszaLitera(zdanie) {
  const litery = {};
  let maxCzestosc = 0;
  let najczestszaLitera = "";
  for (let i = 0; i < zdanie.length; i++) {
    const litera = zdanie[i];
    if (litera === " ") {
      continue;
    }
    if (!litery[litera]) {
      litery[litera] = 0;
    }
    litery[litera]++;
    if (litery[litera] > maxCzestosc) {
      maxCzestosc = litery[litera];
      najczestszaLitera = litera;
    }
  }
  return najczestszaLitera;
}

function testNajczestszaLitera() {
  const zdanie1 = "lezy jerzy na wiezy";
  const wynik1 = najczestszaLitera(zdanie1);
  console.assert(wynik1 === "e", "Test 1 nie powiodl sie");

  const zdanie2 = "Ala ma kota";
  const wynik2 = najczestszaLitera(zdanie2);
  console.assert(wynik2 === "a", "Test 2 nie powiodl sie");
}

testNajczestszaLitera();

