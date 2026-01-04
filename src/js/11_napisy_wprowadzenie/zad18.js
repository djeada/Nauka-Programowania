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

// Funkcja odwraca litery w słowie
// Złożoność czasowa: O(k), gdzie k to długość słowa
// Złożoność pamięciowa: O(k)
function odwrocSlowo(slowo) {
  return slowo.split("").reverse().join("");
}

// Funkcja odwraca każde słowo w zdaniu osobno, zachowując kolejność słów
// Złożoność czasowa: O(n), gdzie n to długość napisu
// Złożoność pamięciowa: O(n)
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
  let expectedOutput = "alA am atok";
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

