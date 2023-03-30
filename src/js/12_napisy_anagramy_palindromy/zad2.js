/*

Tytuł: Znalezienie wszystkich permutacji słowa.

Treść: Napisz program, który dla otrzymanego napisu znajdzie jego wszystkie permutacje.

Dane wejściowe: Napis.

Dane wyjściowe: Lista napisów.

Przykład:

Dla otrzymanego napisu: “abc”, powinna zostać zwrócona lista: [“abc”, “bac”, “cab”, “acb”, “bca”, “cba”].
*/

function permutacje(napis) {
  if (napis.length === 1) {
    return [napis];
  }

  const wynik = [];
  for (let i = 0; i < napis.length; i++) {
    const pierwszyZnak = napis[i];
    const resztaNapisu = napis.slice(0, i) + napis.slice(i + 1);
    const permutacjeReszty = permutacje(resztaNapisu);

    for (const perm of permutacjeReszty) {
      wynik.push(pierwszyZnak + perm);
    }
  }

  return wynik;
}

// Test

function test() {
  const input = "abc";
  const expectedOutput = ["abc", "acb", "bac", "bca", "cab", "cba"];
  const output = permutacje(input);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    'Test nie powiódł się dla "' +
      input +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedł pomyślnie");
}

test();
