/*
ZAD-02 — Usuń podnapis

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Dostajesz dwa napisy:

1. Napis główny,
2. Podnapis do usunięcia.

Usuń **wszystkie wystąpienia** podnapisu z napisu głównego.

### Wejście

* 1 linia: napis `S`
* 2 linia: napis `T` (do usunięcia)

### Wyjście

* 1 linia: wynikowy napis po usunięciu wszystkich wystąpień

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
```

**Wyjście:**

```
Le je na wie
```

*/

function usunPodnapis(napis, podnapis) {
  return napis.split(podnapis).join("");
}

function testUsunPodnapis() {
  const napis = "Lezy jezy na wiezy";
  const podnapis = "zy";
  const wynik = "Le je na wie";
  console.assert(usunPodnapis(napis, podnapis) === wynik, "Test nieudany");
}

testUsunPodnapis();

