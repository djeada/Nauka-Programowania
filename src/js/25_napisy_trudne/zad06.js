/*
ZAD-06 — Rotacje napisów

**Poziom:** ★★★
**Tagi:** `string`, `rotation`, `substring`

### Treść

Otrzymujesz dwa napisy `A` i `B`. Sprawdź, czy jeden z nich jest **rotacją** drugiego (mają tę samą długość i da się uzyskać jeden przez przesunięcie cykliczne drugiego).

### Wejście

* 1 linia: napis `A`
* 2 linia: napis `B`

### Wyjście

* 1 linia: `Prawda` albo `Fałsz`

### Przykład

**Wejście:**

```
malpka
pkamal
```

**Wyjście:**

```
Prawda
```

*/

function czyRotacja(napis1, napis2) {
  if (napis1.length !== napis2.length) {
    return false;
  }
  const napisPodwojony = napis1 + napis1;
  return napisPodwojony.includes(napis2);
}

function testCzyRotacja() {
  const napis1 = "malpka";
  const napis2 = "pkamal";
  const napis3 = "malpak";
  console.assert(czyRotacja(napis1, napis2) === true, "Test 1 nieudany");
  console.assert(czyRotacja(napis1, napis3) === false, "Test 2 nieudany");
}

testCzyRotacja();

