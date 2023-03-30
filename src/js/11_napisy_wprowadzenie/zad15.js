/*
Tytuł: Słowa ze zdania jako osobne elementy listy.

Treść: Otrzymujesz napis reprezentujący zdanie. Zwróć listę słów zdania. Znaki interpunkcyjne nie są liczone jako słowa.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “Ala ma kota”, powinna zostać zwrócona lista: [“Ala”, “ma”, “kota”].
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
    'Test nie powiódł się dla "' +
      input +
      '". Otrzymany wynik to [' +
      output +
      "], a oczekiwany wynik to [" +
      expectedOutput +
      "]"
  );
  console.log("Test przeszedł pomyślnie");
}

test();
