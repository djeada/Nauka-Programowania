/*
ZAD-09 — Znaki występujące co najmniej dwa razy

**Poziom:** ★☆☆
**Tagi:** `dict`, `string`

### Treść

Wczytaj napis. Wypisz napis złożony z **unikalnych** znaków, które występują co najmniej 2 razy, w kolejności pierwszego pojawienia się w wejściu.

### Wejście

* 1 linia: napis

### Wyjście

* 1 linia: wynikowy napis

### Przykład

**Wejście:**

```
aaabbbccc
```

**Wyjście:**

```
abc
```

*/

function powtarzajaceSieZnaki(napis) {
  const znaki = {};
  let powtarzajaceSie = "";
  for (let i = 0; i < napis.length; i++) {
    const znak = napis[i];
    if (!znaki[znak]) {
      znaki[znak] = 1;
    } else {
      znaki[znak]++;
    }
  }
  for (const znak in znaki) {
    if (znaki[znak] >= 2) {
      powtarzajaceSie += znak;
    }
  }
  return powtarzajaceSie;
}

function testPowtarzajaceSieZnaki() {
  const napis1 = "aaabbbccc";
  const wynik1 = powtarzajaceSieZnaki(napis1);
  console.assert(wynik1 === "abc", "Test 1 nie powiodl sie");

  const napis2 = "abcd";
  const wynik2 = powtarzajaceSieZnaki(napis2);
  console.assert(wynik2 === "", "Test 2 nie powiodl sie");

  const napis3 = "Ala ma kota, a kot ma Ale.";
  const wynik3 = powtarzajaceSieZnaki(napis3);
  console.assert(wynik3 === "aekmt", "Test 3 nie powiodl sie");
}

testPowtarzajaceSieZnaki();

