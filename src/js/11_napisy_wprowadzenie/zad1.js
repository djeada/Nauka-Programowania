/*
Tytul: Odwroc napis.

Tresc: Zmien otrzymany napis, tak aby zapisany byl on od tylu.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanego napisu: "barszcz", powinien zostac zwrocony napis: "zczsrab".
*/

function odwrocNapis(napis) {
  return napis.split("").reverse().join("");
}

function test() {
  let input = "barszcz";
  let expectedOutput = "zczsrab";
  let output = odwrocNapis(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

