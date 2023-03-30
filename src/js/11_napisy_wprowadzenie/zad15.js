/*
Tytul: Slowa ze zdania jako osobne elementy listy.

Tresc: Otrzymujesz napis reprezentujacy zdanie. Zwroc liste slow zdania. Znaki interpunkcyjne nie sa liczone jako slowa.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla otrzymanego napisu: “Ala ma kota”, powinna zostac zwrocona lista: [“Ala”, “ma”, “kota”].
*/

function slowaZeZdania(zdanie) {
  let slowa = zdanie.split(" ");
  let wynik = [];
  for (let i = 0; i < slowa.length; i++) {
    let slowo = slowa[i].replace(/[^\w]/g, "");
    if (slowo) {
      wynik.push(slowo);
    }
  }
  return wynik;
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = ["Ala", "ma", "kota"];
  let output = slowaZeZdania(input);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to [' +
      output +
      "], a oczekiwany wynik to [" +
      expectedOutput +
      "]"
  );
  console.log("Test przeszedl pomyslnie");
}

test();

