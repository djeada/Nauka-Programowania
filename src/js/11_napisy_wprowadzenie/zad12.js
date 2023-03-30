/*
Tytul: Usun spacje ze zdania.

Tresc: Otrzymasz napis reprezentujacy zdanie. Usun spacje ze zdania.

Dane wejsciowe: Napis.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanego napisu: "Ala ma kota", powinien zostac zwrocony napis: "Alamakota".
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

