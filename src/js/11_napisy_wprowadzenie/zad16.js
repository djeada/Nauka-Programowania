/*
Tytul: Odleglosc Hamminga.

Tresc: Otrzymujesz dwa napisy o rownej dlugosci. Oblicz odleglosc Hamminga miedzy dwoma otrzymanymi napisami. Odleglosc Hamminga to miara odmiennosci dwoch napisow o takiej samej dlugosci, zdefiniowana jako liczba pozycji, na ktorych napisy maja rozne znaki.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanych napisow: “adam” i “axam”, powinna zostac zwrocona liczba: 1.
*/

function odlegloscHamminga(napis1, napis2) {
  let odleglosc = 0;
  for (let i = 0; i < napis1.length; i++) {
    if (napis1[i] !== napis2[i]) {
      odleglosc++;
    }
  }
  return odleglosc;
}

// Test

function test() {
  let input1 = "adam";
  let input2 = "axam";
  let expectedOutput = 1;
  let output = odlegloscHamminga(input1, input2);

  console.assert(
    output === expectedOutput,
    'Test nie powiodl sie dla "' +
      input1 +
      '" i "' +
      input2 +
      '". Otrzymany wynik to ' +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();

