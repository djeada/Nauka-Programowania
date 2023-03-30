/*

Tytuł: Mnożenie wektorowe.	

Treść: Treść: Otrzymujesz dwie listy liczb całkowitych reprezentujące dwa wektory trójwymiarowej przestrzeni euklidesowej. Zaimplementuj mnożenie wektorowe (zdefiniowane jedynie dla wektorów 3-wymiarowej przestrzeni euklidesowej).

Dane wejściowe: Dwie listy liczb całkowitych o długości 3.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanych list [1, 2, 3] oraz [3, 1, 2], powinno zostać zwrócone: 5.
*/

// Funkcja mnożąca wektory
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
