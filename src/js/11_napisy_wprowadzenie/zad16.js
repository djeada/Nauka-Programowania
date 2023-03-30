/*
Tytuł: Odległość Hamminga.

Treść: Otrzymujesz dwa napisy o równej długości. Oblicz odległość Hamminga między dwoma otrzymanymi napisami. Odległość Hamminga to miara odmienności dwóch napisów o takiej samej długości, zdefiniowana jako liczba pozycji, na których napisy mają różne znaki.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych napisów: “adam” i “axam”, powinna zostać zwrócona liczba: 1.
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
    'Test nie powiódł się dla "' +
      input1 +
      '" i "' +
      input2 +
      '". Otrzymany wynik to ' +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedł pomyślnie");
}

test();
