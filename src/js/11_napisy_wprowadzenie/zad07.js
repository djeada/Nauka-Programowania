/*
Tytul: Zamien znaki na kody ASCII.

Tresc: Otrzymasz napis. Zmien wszystkie znaki w napisie na odpowiadajace im numery w tablicy ASCII. Zastap otrzymany napis napisem skladajacym sie z otrzymanych numerow, oddzielonych przecinkami.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanego napisu: "Robot", powinien zostac zwrocony napis: "82, 111, 98, 111, 116".
*/

function zamienNaKodyASCII(napis) {
  let wynik = "";
  for (let i = 0; i < napis.length; i++) {
    wynik += napis.charCodeAt(i);
    if (i !== napis.length - 1) {
      wynik += ", ";
    }
  }
  return wynik;
}

// Testy

function test() {
  let input = "Robot";
  let expectedOutput = "82, 111, 98, 111, 116";
  let output = zamienNaKodyASCII(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

