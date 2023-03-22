/*
Tytuł: Zamień wszystkie małe litery na duże.

Treść: Otrzymasz napis. Zmień wszystkie małe litery na duże.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: "Rumcajs", powinien zostać zwrócony napis: "RUMCAJS".
*/

function zamienNaDuze(napis) {
  return napis.toUpperCase();
}

// Testy

function test() {
  let input = "Rumcajs";
  let expectedOutput = "RUMCAJS";
  let output = zamienNaDuze(input);

  assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

test();
