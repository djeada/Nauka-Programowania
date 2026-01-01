/*
ZAD-08 — Najdłuższy wspólny przedrostek

**Poziom:** ★★★
**Tagi:** `string`, `prefix`, `list`

### Treść

Otrzymujesz listę napisów (w kolejnych liniach). Znajdź najdłuższy przedrostek wspólny dla wszystkich.

### Wejście

* 1 linia: `n` — liczba napisów
* kolejne `n` linii: napisy

### Wyjście

* 1 linia: najdłuższy wspólny przedrostek (może być pusty)

### Przykład

**Wejście:**

```
3
Remolada
Remux
Remmy
```

**Wyjście:**

```
Rem
```

*/

function najdluzszyWspolnyPrzedrostek(listaNapisow) {
  if (listaNapisow.length === 0) {
    return "";
  }

  let przedrostek = listaNapisow[0];

  for (let i = 1; i < listaNapisow.length; i++) {
    while (listaNapisow[i].indexOf(przedrostek) !== 0) {
      przedrostek = przedrostek.substring(0, przedrostek.length - 1);
      if (przedrostek === "") {
        return "";
      }
    }
  }

  return przedrostek;
}

function testNajdluzszyWspolnyPrzedrostek() {
  const lista1 = ["Remolada", "Remux", "Remmy"];
  const wynik1 = "Rem";
  const lista2 = ["piesek", "kotek", "myszka"];
  const wynik2 = "";

  console.assert(
    najdluzszyWspolnyPrzedrostek(lista1) === wynik1,
    "Test 1 nieudany"
  );
  console.assert(
    najdluzszyWspolnyPrzedrostek(lista2) === wynik2,
    "Test 2 nieudany"
  );
}

testNajdluzszyWspolnyPrzedrostek();

