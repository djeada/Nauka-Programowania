/*

Tytuł: Znalezienie anagramów słowa w zdaniu.

Treść: Napisz program, który otrzymuje napis reprezentujący zdanie oraz słowo. Twoim zadaniem jest znalezienie wszystkich anagramów otrzymanego słowa w zdaniu. Różnice między wielkimi i małymi literami powinny być zignorowane.

Dane wejściowe: Dwa napisy.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanych napisów: “Sroga kara.” oraz “arak”, powinna zostać zwrócona lista: [“kara”].
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
    'Test nie powiódł się dla "' +
      inputZdanie +
      '" i "' +
      inputSlowo +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedł pomyślnie");
}

test();
