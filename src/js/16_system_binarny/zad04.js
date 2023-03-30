/*

Tytul: Liczba zer i jedynek w reprezentacji binarnej.

Tresc: Otrzymujesz reprezentacje dziesietna liczby naturalnej.

a) Oblicz, ile zer zawiera binarna reprezentacja otrzymanej liczby.

b) Oblicz, ile jedynek zawiera binarna reprezentacja otrzymanej liczby.

Dane wejsciowe: Liczba naturalna w obu podpunktach.

Dane wyjsciowe: Liczba naturalna w obu podpunktach.

Przyklad:

a) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 0.
 
b) Dla otrzymanej liczby: 3, powinna zostac zwrocona liczba: 2.
*/

// Funkcja obliczajaca ilosc zer w reprezentacji binarnej liczby
function iloscZerLiczby(liczba) {
  let binarna = liczba.toString(2);
  let iloscZer = 0;
  for (let i = 0; i < binarna.length; i++) {
    if (binarna[i] === "0") {
      iloscZer++;
    }
  }
  return iloscZer;
}

// Funkcja obliczajaca ilosc jedynek w reprezentacji binarnej liczby
function iloscJedynekLiczby(liczba) {
  let binarna = liczba.toString(2);
  let iloscJedynek = 0;
  for (let i = 0; i < binarna.length; i++) {
    if (binarna[i] === "1") {
      iloscJedynek++;
    }
  }
  return iloscJedynek;
}

// Testy
function test() {
  let input = 3;
  let expectedOutput1 = 0;
  let expectedOutput2 = 2;
  let output1 = iloscZerLiczby(input);
  let output2 = iloscJedynekLiczby(input);

  console.assert(output1 === expectedOutput1, "Test nie powiodl sie");
  console.assert(output2 === expectedOutput2, "Test nie powiodl sie");
  console.log("Test przeszedl pomyslnie");
}

test();

