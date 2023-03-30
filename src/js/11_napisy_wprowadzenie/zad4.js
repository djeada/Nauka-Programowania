/*
Tytul: Zamien wszystkie male litery na duze.

Tresc: Otrzymasz napis. Zmien wszystkie male litery na duze.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanego napisu: "Rumcajs", powinien zostac zwrocony napis: "RUMCAJS".
*/

function zamienNaDuze(napis) {
  return napis.toUpperCase();
}

// Testy

function test() {
  let input = "Rumcajs";
  let expectedOutput = "RUMCAJS";
  let output = zamienNaDuze(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

