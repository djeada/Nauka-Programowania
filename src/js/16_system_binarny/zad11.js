/*

Tytuł: Czy liczba jest palindromem?

Treść: Otrzymujesz dziesiętną reprezentację liczby naturalnej. Sprawdź, czy reprezentacja binarna otrzymanej liczby jest palindromem.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanej liczby 26, powinna zostać zwrócona wartość logiczna: Prawda.*/

function czyPalindrom(liczba) {
  let lewyBit = 1;
  let prawyBit = 1 << 30;

  while (lewyBit < prawyBit) {
    if ((liczba & lewyBit) !== (liczba & prawyBit) >>> 30) {
      return false;
    }
    lewyBit <<= 1;
    prawyBit >>>= 1;
  }

  return true;
}

// Testy
function test() {
  let input = 26;
  let expectedOutput = true;
  let output = czyPalindrom(input);

  assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

test();
