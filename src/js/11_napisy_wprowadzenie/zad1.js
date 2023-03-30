/*
Tytuł: Odwróć napis.

Treść: Zmień otrzymany napis, tak aby zapisany był on od tyłu.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: "barszcz", powinien zostać zwrócony napis: "zczsrab".
*/

function odwrocNapis(napis) {
  return napis.split("").reverse().join("");
}

function test() {
  let input = "barszcz";
  let expectedOutput = "zczsrab";
  let output = odwrocNapis(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

test();
