/*
ZAD-01 — Podmiana słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `string`, `replace`, `substring`

### Treść

Masz trzy napisy:

1. Zdanie (tekst do modyfikacji),
2. Słowo A (podnapis do znalezienia),
3. Słowo B (podnapis zastępujący).

Zamień **wszystkie wystąpienia** słowa/podnapisu **A** na **B** w podanym zdaniu.

> Uwaga: A może być częścią innych słów — zamiana dotyczy **każdego wystąpienia podnapisu**.

### Wejście

* 1 linia: zdanie `S`
* 2 linia: napis `A`
* 3 linia: napis `B`

### Wyjście

* 1 linia: zdanie po zamianie

### Przykład

**Wejście:**

```
Lezy jezy na wiezy
zy
rzy
```

**Wyjście:**

```
Lerzy jerzy na wierzy
```

*/

function podmianaSlowa(zdanie, slowoA, slowoB) {
  return zdanie.split(slowoA).join(slowoB);
}

function testPodmianaSlowa() {
  const zdanie = "Lezy jezy na wiezy";
  const slowoA = "zy";
  const slowoB = "rzy";
  const wynik = "Lerzy jerzy na wierzy";
  console.assert(
    podmianaSlowa(zdanie, slowoA, slowoB) === wynik,
    "Test nieudany"
  );
}

testPodmianaSlowa();

