/*
Tytuł: Usuń spacje ze zdania.

Treść: Otrzymasz napis reprezentujący zdanie. Usuń spacje ze zdania.

Dane wejściowe: Napis.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanego napisu: "Ala ma kota", powinien zostać zwrócony napis: "Alamakota".
*/

function usunSpacje(napis) {
  return napis.replace(/\s+/g, "");
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = "Alamakota";
  let output = usunSpacje(input);

  console.assert(
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

test();
