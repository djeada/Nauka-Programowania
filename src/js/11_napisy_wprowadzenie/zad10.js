/*
Tytul: Znajdz najdluzsze/najkrotsze slowo w zdaniu.

Tresc: Otrzymasz napis reprezentujacy zdanie. Znajdz:

a) najdluzsze slowo w zdaniu,

b) najkrotsze slowo w zdaniu.

Jesli wiecej niz jedno slowo ma ekstremalna dlugosc, zwroc to slowo sposrod nich, ktore wystepuje w zdaniu jako pierwsze. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.

Dane wejsciowe: Napis.

Dane wyjsciowe:

a) Napis.

b) Napis.

Przyklad:

a) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "Kaczka".

b) Dla otrzymanego napisu: "Kaczka lubi wiosne.", powinno zostac zwrocone: "lubi".
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
  let input = "Kaczka lubi wiosne.";
  let expectedOutput = ["Kaczka", "lubi"];
  let output = znajdzNajdluzszeISkrotszeSlowo(input);

  console.assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiodl sie"
  );
  console.log("Test przeszedl pomyslnie");
}

test();

