/*

Tytul: Najdluzszy ciag zer w liczbie binarnej.

Tresc: Otrzymujesz dziesietna reprezentacje liczby naturalnej. Oblicz dlugosc najdluzszego ciagu zer w jej reprezentacji binarnej.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej liczby 14, powinna zostac zwrocona liczba 1.
*/

// Funkcja obliczajaca najdluzszy ciag zer w liczbie binarnej
function najdluzszyCiagZer(liczba) {
  let binarna = liczba.toString(2);
  let najdluzszyCiag = 0;
  let aktualnyCiag = 0;
  for (let i = 0; i < binarna.length; i++) {
    if (binarna[i] === "0") {
      aktualnyCiag++;
    } else {
      if (aktualnyCiag > najdluzszyCiag) {
        najdluzszyCiag = aktualnyCiag;
      }
      aktualnyCiag = 0;
    }
  }
  return najdluzszyCiag;
}

// Testy
function test() {
  let input = 14;
  let expectedOutput = 1;
  let output = najdluzszyCiagZer(input);

  console.assert(output === expectedOutput, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

