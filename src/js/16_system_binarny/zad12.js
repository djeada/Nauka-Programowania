/*

Tytuł: Najdłuższy ciąg zer w liczbie binarnej.

Treść: Otrzymujesz dziesiętną reprezentację liczby naturalnej. Oblicz długość najdłuższego ciągu zer w jej reprezentacji binarnej.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej liczby 14, powinna zostać zwrócona liczba 1.
*/

// Funkcja obliczająca najdłuższy ciąg zer w liczbie binarnej
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

  assert(output === expectedOutput, "Test nie powiódł się");
  console.log("Test przeszedł pomyślnie");
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Assertion failed";
  }
}

test();
