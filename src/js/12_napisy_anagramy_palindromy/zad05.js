/*

Tytul: Znalezienie anagramow slowa w zdaniu.

Tresc: Napisz program, ktory otrzymuje napis reprezentujacy zdanie oraz slowo. Twoim zadaniem jest znalezienie wszystkich anagramow otrzymanego slowa w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.

Dane wejsciowe: Dwa napisy.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla otrzymanych napisow: “Sroga kara.” oraz “arak”, powinna zostac zwrocona lista: [“kara”].
*/

function czyAnagramy(napis1, napis2) {
  if (napis1.length !== napis2.length) {
    return false;
  }

  const posortowanyNapis1 = napis1.split("").sort().join("").toLowerCase();
  const posortowanyNapis2 = napis2.split("").sort().join("").toLowerCase();

  return posortowanyNapis1 === posortowanyNapis2;
}

function znajdzAnagramy(zdanie, slowo) {
  const slowa = zdanie.split(" ");
  const anagramy = [];

  for (const slowoZdania of slowa) {
    if (czyAnagramy(slowoZdania, slowo)) {
      anagramy.push(slowoZdania);
    }
  }

  return anagramy;
}

// Test

function test() {
  const inputZdanie = "Sroga kara.";
  const inputSlowo = "arak";
  const expectedOutput = ["kara"];
  const output = znajdzAnagramy(inputZdanie, inputSlowo);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    'Test nie powiodl sie dla "' +
      inputZdanie +
      '" i "' +
      inputSlowo +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedl pomyslnie");
}

test();

