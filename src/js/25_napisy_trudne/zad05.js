/*
ZAD-05 — Usuń powtórzenia sąsiadujących znaków

**Poziom:** ★★★
**Tagi:** `string`, `compress`, `run-length`

### Treść

Otrzymujesz napis. Usuń powtórzenia znaków występujących **bezpośrednio obok siebie**, pozostawiając jedno wystąpienie z każdej „serii”.

### Wejście

* 1 linia: napis `S`

### Wyjście

* 1 linia: napis po redukcji sąsiadów

### Przykład

**Wejście:**

```
AAAAAAAAAABBBBBBBBA
```

**Wyjście:**

```
ABA
```

*/

function usunSasiedniePowtorzenia(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    if (napis[i] !== napis[i + 1]) {
      wynik += napis[i];
    }
  }
  return wynik;
}

function testUsunSasiedniePowtorzenia() {
  const napis = "AAAAAAAAAABBBBBBBBA";
  const wynik = "ABA";
  console.assert(usunSasiedniePowtorzenia(napis) === wynik, "Test nieudany");
}

testUsunSasiedniePowtorzenia();

