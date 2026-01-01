/*
ZAD-18 — Odwróć słowa w zdaniu

**Poziom:** ★★☆
**Tagi:** `split`, `string`, `pętle`

### Treść

Wczytaj zdanie i odwróć litery **w każdym słowie osobno**, zachowując kolejność słów.

### Wejście

* 1. linia: zdanie

### Wyjście

* 1. linia: zdanie z odwróconymi słowami

### Przykład

**Wejście:**

```
Ala ma kota
```

**Wyjście:**

```
alA am atok
```

*/

function rozbijNaSlowa(napis) {
  return napis.split(/[^\w]+/);
}

function odwrocSlowo(slowo) {
  return slowo.split("").reverse().join("");
}

function odwrocSlowa(napis) {
  let slowa = rozbijNaSlowa(napis);
  let wynik = [];
  for (let i = 0; i < slowa.length; i++) {
    if (slowa[i] !== "") {
      wynik.push(odwrocSlowo(slowa[i]));
    }
  }
  return wynik.join(" ");
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = "ala mak otak";
  let output = odwrocSlowa(input);

  console.assert(
    output === expectedOutput,
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to "' +
      output +
      '", a oczekiwany wynik to "' +
      expectedOutput +
      '"'
  );
  console.log("Test przeszedl pomyslnie");
}

test();

