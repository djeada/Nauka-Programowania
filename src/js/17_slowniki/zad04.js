/*
ZAD-04 — Usuń pary ze słownika na podstawie wartości

**Poziom:** ★☆☆
**Tagi:** `dict`, `filtrowanie`

### Treść

Wczytaj słownik (`n` par: klucz-napis, wartość-liczba) oraz liczbę `k`. Usuń wszystkie pary, gdzie wartość == `k`. Wypisz wynikowy słownik.

### Wejście

* 1 linia: `n`
* następnie `n` linii: `klucz wartość`
* ostatnia linia: `k`

### Wyjście

* Słownik po usunięciu par

### Przykład

**Wejście:**

```
4
aaa 5
abc 1
xxx 5
cba 3
5
```

**Wyjście:**

```
{'abc': 1, 'cba': 3}
```

*/

function usunZeSlownika(slownik, liczba) {
  for (let key in slownik) {
    if (slownik[key] === liczba) {
      delete slownik[key];
    }
  }
  return slownik;
}

function testUsunZeSlownika() {
  const slownik1 = {
    aaa: 5,
    abc: 1,
    xxx: 5,
    cba: 3,
  };
  const wynik1 = usunZeSlownika(slownik1, 5);
  console.assert(wynik1["abc"] === 1, "Test 1 nie powiodl sie");
  console.assert(wynik1["cba"] === 3, "Test 2 nie powiodl sie");
  console.assert(Object.keys(wynik1).length === 2, "Test 3 nie powiodl sie");

  const slownik2 = {
    a: 10,
    b: 20,
    c: 30,
  };
  const wynik2 = usunZeSlownika(slownik2, 15);
  console.assert(Object.keys(wynik2).length === 3, "Test 4 nie powiodl sie");
}

testUsunZeSlownika();

