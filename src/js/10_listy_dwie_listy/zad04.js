/*

Tytul: Mnozenie wektorowe.	

Tresc: Tresc: Otrzymujesz dwie listy liczb calkowitych reprezentujace dwa wektory trojwymiarowej przestrzeni euklidesowej. Zaimplementuj mnozenie wektorowe (zdefiniowane jedynie dla wektorow 3-wymiarowej przestrzeni euklidesowej).

Dane wejsciowe: Dwie listy liczb calkowitych o dlugosci 3.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanych list [1, 2, 3] oraz [3, 1, 2], powinno zostac zwrocone: 5.
*/

// Funkcja mnozaca wektory
function mnozWektory(lista1, lista2) {
  let wynik = 0;
  for (let i = 0; i < 3; i++) {
    wynik += lista1[i] * lista2[i];
  }
  return wynik;
}

// Testy

function testMnozWektory() {
  console.assert(mnozWektory([1, 2, 3], [3, 1, 2]) === 5);
  console.assert(mnozWektory([1, 2, 3], [3, 1, 2, 5]) === 5);
}

function main() {
  testMnozWektory();
}

main();

