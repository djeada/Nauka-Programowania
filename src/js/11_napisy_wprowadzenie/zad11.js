/*

Tytuł: Średnia długość słów w zdaniu.

Treść: Otrzymasz napis reprezentujący zdanie. Oblicz średnią długość słów w zdaniu. Znaki interpunkcyjne nie są uwzględniane jako słowa.

Dane wejściowe: Napis.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanego napisu: "Zepsuty rower.", powinna zostać zwrócona liczba: 6.
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

  assert(
    output === expectedOutput,
    "Test nie powiódł się dla " +
      input +
      ". Otrzymany wynik to " +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

test();
