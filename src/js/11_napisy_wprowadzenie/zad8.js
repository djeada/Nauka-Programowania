/*
Tytul:Wypisz pionowo slowa, z ktorych sklada sie zdanie.

Tresc: Otrzymasz napis reprezentujacy zdanie. Podziel zdanie na slowa skladowe. Wypisz pionowo slowa, z ktorych sklada sie zdanie. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.

Dane wejsciowe: Napis.

Dane wyjsciowe: Kilka napisow.

Przyklad:

Dla otrzymanego napisu: "Ala ma kota", powinno zostac wypisane: "Ala", "ma", "kota".
*/

function wypiszSlowa(napis) {
  let slowa = napis.split(/[^\w]+/);
  for (let i = 0; i < slowa.length; i++) {
    if (slowa[i] !== "") {
      console.log(slowa[i]);
    }
  }
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = ["Ala", "ma", "kota"];
  let output = [];
  console.log = function (text) {
    output.push(text);
  };
  wypiszSlowa(input);

  console.assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiodl sie"
  );
  console.log("Test przeszedl pomyslnie");
}

test();

