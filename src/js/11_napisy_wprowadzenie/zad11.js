/*

Tytul: Srednia dlugosc slow w zdaniu.

Tresc: Otrzymasz napis reprezentujacy zdanie. Oblicz srednia dlugosc slow w zdaniu. Znaki interpunkcyjne nie sa uwzgledniane jako slowa.

Dane wejsciowe: Napis.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanego napisu: "Zepsuty rower.", powinna zostac zwrocona liczba: 6.
*/

function sredniaDlugoscSlow(napis) {
  let slowa = napis.split(/[^\w]+/);
  let sumaDlugosciSlow = 0;
  for (let i = 0; i < slowa.length; i++) {
    sumaDlugosciSlow += slowa[i].length;
  }
  let sredniaDlugosc = sumaDlugosciSlow / slowa.length;
  return Math.round(sredniaDlugosc);
}

// Test

function test() {
  let input = "Zepsuty rower.";
  let expectedOutput = 6;
  let output = sredniaDlugoscSlow(input);

  console.assert(
    output === expectedOutput,
    "Test nie powiodl sie dla " +
      input +
      ". Otrzymany wynik to " +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();

