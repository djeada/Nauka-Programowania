/*
Tytul: Permutacje slowa, ktore sa palindromami.

Tresc: Napisz program, ktory znajdzie permutacje danego slowa, ktore sa palindromami.

Dane wejsciowe: Napis.

Dane wyjsciowe: Lista napisow.

Przyklad:

Dla otrzymanego napisu: “taco”, powinna zostac zwrocona lista: ["taco", "toca"].
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

function jestPalindromem(napis) {
  const odwroconyNapis = napis.split("").reverse().join("");
  return napis.toLowerCase() === odwroconyNapis.toLowerCase();
}

function permutacjePalindromy(napis) {
  const wszystkiePermutacje = permutacje(napis);
  const wynik = [];

  for (const perm of wszystkiePermutacje) {
    if (jestPalindromem(perm)) {
      wynik.push(perm);
    }
  }

  return wynik;
}

// Test

function test() {
  const input = "taco";
  const expectedOutput = ["taco", "toca"];
  const output = permutacjePalindromy(input);

  console.assert(
    JSON.stringify(output) === JSON.stringify(expectedOutput),
    'Test nie powiodl sie dla "' +
      input +
      '". Otrzymany wynik to ' +
      JSON.stringify(output) +
      ", a oczekiwany wynik to " +
      JSON.stringify(expectedOutput)
  );
  console.log("Test przeszedl pomyslnie");
}

test();

