/*
Tytul: Zamien litery "a" na znaki zapytania.

Tresc: Otrzymasz napis. Zmien litery "a" na znaki zapytania.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanego napisu: "Latarnik", powinien zostac zwrocony napis: "L?t?rnik".
*/

function zamienLitery(napis) {
  return napis.replace(/a/g, "?");
}

// Testy

function test() {
  let input = "Latarnik";
  let expectedOutput = "L?t?rnik";
  let output = zamienLitery(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

