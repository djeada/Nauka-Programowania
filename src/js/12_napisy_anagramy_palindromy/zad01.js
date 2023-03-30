/*

Tytul: Sprawdzenie, czy slowo jest palindromem.

Tresc: Napisz program, ktory sprawdzi, czy slowo jest palindromem. Palindromem jest slowo, ktore brzmi tak samo czytane od lewej do prawej i od prawej do lewej.

Dane wejsciowe: Napis.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla otrzymanego napisu: “kajak”, powinna zostac zwrocona wartosc logiczna: Prawda.
*/

function czyPalindrom(napis) {
  let napisOdwrocony = napis.split("").reverse().join("");
  return napis === napisOdwrocony;
}

// Test

function test() {
  let input = "kajak";
  let expectedOutput = true;
  let output = czyPalindrom(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

