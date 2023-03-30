/*
Tytuł: Konwersja listy na napis

Treść: Otrzymujesz listę liczb naturalnych. Zamie listę na napis.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Napis.

Przykład:

Dla otrzymanej listy: [2, 4, 7], powinien zostać zwrócony napis: “247”.
*/

function listaNaNapis(lista) {
  return lista.join("");
}

// Testy

function test() {
  let input = [2, 4, 7];
  let expectedOutput = "247";
  let output = listaNaNapis(input);

  console.assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

test();
