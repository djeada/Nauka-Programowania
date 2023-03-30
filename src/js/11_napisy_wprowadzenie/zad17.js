/*
Tytul: Konwersja listy na napis

Tresc: Otrzymujesz liste liczb naturalnych. Zamie liste na napis.

Dane wejsciowe: Lista liczb naturalnych.

Dane wyjsciowe: Napis.

Przyklad:

Dla otrzymanej listy: [2, 4, 7], powinien zostac zwrocony napis: “247”.
*/

function listaNaNapis(lista) {
  return lista.join("");
}

// Testy

function test() {
  let input = [2, 4, 7];
  let expectedOutput = "247";
  let output = listaNaNapis(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

