/*
Tytuł: Znajdź najdłuższe/najkrótsze słowo w zdaniu.

Treść: Otrzymasz napis reprezentujący zdanie. Znajdź:

a) najdłuższe słowo w zdaniu,

b) najkrótsze słowo w zdaniu.

Jeśli więcej niż jedno słowo ma ekstremalną długość, zwróć to słowo spośród nich, które występuje w zdaniu jako pierwsze. Znaki interpunkcyjne nie są uwzględniane jako słowa.

Dane wejściowe: Napis.

Dane wyjściowe:

a) Napis.

b) Napis.

Przykład:

a) Dla otrzymanego napisu: "Kaczka lubi wiosnę.", powinno zostać zwrócone: "Kaczka".

b) Dla otrzymanego napisu: "Kaczka lubi wiosnę.", powinno zostać zwrócone: "lubi".
*/

function znajdzEkstremalneSlowo(napis, ekstremum) {
  let slowa = napis.split(/[^\w]+/);
  let slowoEkstremalne = slowa[0];
  for (let i = 0; i < slowa.length; i++) {
    if (slowa[i].length === ekstremum) {
      slowoEkstremalne = slowa[i];
      break;
    }
  }
  return slowoEkstremalne;
}

function znajdzNajdluzszeISkrotszeSlowo(napis) {
  let slowa = napis.split(/[^\w]+/);
  let najdluzszeSlowo = slowa[0];
  let najkrotszeSlowo = slowa[0];
  for (let i = 0; i < slowa.length; i++) {
    let slowo = slowa[i];
    if (slowo.length > najdluzszeSlowo.length) {
      najdluzszeSlowo = slowo;
    }
    if (slowo.length < najkrotszeSlowo.length) {
      najkrotszeSlowo = slowo;
    }
  }
  najdluzszeSlowo = znajdzEkstremalneSlowo(napis, najdluzszeSlowo.length);
  najkrotszeSlowo = znajdzEkstremalneSlowo(napis, najkrotszeSlowo.length);
  return [najdluzszeSlowo, najkrotszeSlowo];
}

// Test

function test() {
  let input = "Kaczka lubi wiosnę.";
  let expectedOutput = ["Kaczka", "lubi"];
  let output = znajdzNajdluzszeISkrotszeSlowo(input);

  console.assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiódł się"
  );
  console.log("Test przeszedł pomyślnie");
}

test();
