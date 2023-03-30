/*
Tytuł: Zamień litery "a" na znaki zapytania.

Treść: Otrzymasz napis. Zmień litery "a" na znaki zapytania.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: "Latarnik", powinien zostać zwrócony napis: "L?t?rnik".
*/

function zamienLitery(napis) {
  return napis.replace(/a/g, "?");
}

// Testy

function test() {
  let input = "Latarnik";
  let expectedOutput = "L?t?rnik";
  let output = zamienLitery(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

test();
