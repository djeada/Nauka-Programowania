/*
Tytuł: Zamień znaki na kody ASCII.

Treść: Otrzymasz napis. Zmień wszystkie znaki w napisie na odpowiadające im numery w tablicy ASCII. Zastąp otrzymany napis napisem składającym się z otrzymanych numerów, oddzielonych przecinkami.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: "Robot", powinien zostać zwrócony napis: "82, 111, 98, 111, 116".
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

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

test();
