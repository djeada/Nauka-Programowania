/*
Tytuł:Wypisz pionowo słowa, z których składa się zdanie.

Treść: Otrzymasz napis reprezentujący zdanie. Podziel zdanie na słowa składowe. Wypisz pionowo słowa, z których składa się zdanie. Znaki interpunkcyjne nie są uwzględniane jako słowa.

Dane wejściowe: Napis.

Dane wyjściowe: Kilka napisów.

Przykład:

Dla otrzymanego napisu: "Ala ma kota", powinno zostać wypisane: "Ala", "ma", "kota".
*/

function wypiszSłowa(napis) {
  let słowa = napis.split(/[^\w]+/);
  for (let i = 0; i < słowa.length; i++) {
    if (słowa[i] !== "") {
      console.log(słowa[i]);
    }
  }
}

// Test

function test() {
  let input = "Ala ma kota";
  let expectedOutput = ["Ala", "ma", "kota"];
  let output = [];
  console.log = function (text) {
    output.push(text);
  };
  wypiszSłowa(input);

  assert(
    output.length === expectedOutput.length &&
      output.every((element, index) => element === expectedOutput[index]),
    "Test nie powiódł się"
  );
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}

test();
