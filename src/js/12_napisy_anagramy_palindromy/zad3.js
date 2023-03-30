/*
Tytul: Sprawdzenie, czy dwa slowa sa anagramami.

Tresc: Napisz program, ktory dla podanych dwoch napisow sprawdzi, czy sa anagramami. Dwa napisy sa anagramami, jesli jeden z nich mozna zbudowac poprzez przestawienie znakow w drugim.

Dane wejsciowe: Napis.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla otrzymanego napisu: “ula” oraz “lua”, powinna zostac zwrocona wartosc logiczna: Prawda.
*/

function czyAnagramy(napis1, napis2) {
  if (napis1.length !== napis2.length) {
    return false;
  }

  const posortowanyNapis1 = napis1.split("").sort().join("");
  const posortowanyNapis2 = napis2.split("").sort().join("");

  return posortowanyNapis1 === posortowanyNapis2;
}

// Test

function test() {
  const input1 = "ula";
  const input2 = "lua";
  const expectedOutput = true;
  const output = czyAnagramy(input1, input2);

  console.assert(
    output === expectedOutput,
    'Test nie powiodl sie dla "' +
      input1 +
      '" i "' +
      input2 +
      '". Otrzymany wynik to ' +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedl pomyslnie");
}

test();

