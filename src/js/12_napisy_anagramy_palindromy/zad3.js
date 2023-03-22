/*
Tytuł: Sprawdzenie, czy dwa słowa są anagramami.

Treść: Napisz program, który dla podanych dwóch napisów sprawdzi, czy są anagramami. Dwa napisy są anagramami, jeśli jeden z nich można zbudować poprzez przestawienie znaków w drugim.

Dane wejściowe: Napis.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanego napisu: “ula” oraz “lua”, powinna zostać zwrócona wartość logiczna: Prawda.
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

  assert(
    output === expectedOutput,
    'Test nie powiódł się dla "' +
      input1 +
      '" i "' +
      input2 +
      '". Otrzymany wynik to ' +
      output +
      ", a oczekiwany wynik to " +
      expectedOutput
  );
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}
test();
