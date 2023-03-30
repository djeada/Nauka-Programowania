/*

Tytul: Czy liczba jest palindromem?

Tresc: Otrzymujesz dziesietna reprezentacje liczby naturalnej. Sprawdz, czy reprezentacja binarna otrzymanej liczby jest palindromem.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla otrzymanej liczby 26, powinna zostac zwrocona wartosc logiczna: Prawda.*/

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

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

