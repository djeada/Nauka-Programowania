/*

Tytuł: Sprawdzenie, czy słowo jest palindromem.

Treść: Napisz program, który sprawdzi, czy słowo jest palindromem. Palindromem jest słowo, które brzmi tak samo czytane od lewej do prawej i od prawej do lewej.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanego napisu: “kajak”, powinna zostać zwrócona wartość logiczna: Prawda.
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

  assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

test();
