/*
Tytul: Odwroc slowa w zdaniu.

Tresc: Otrzymujesz napis reprezentujacy zdanie. Zamien slowa zdania na te same napisy zapisane wspak. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "ala mak otak".
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

