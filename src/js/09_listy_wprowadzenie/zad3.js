/*
Tytuł: Pierwsze wystąpienie klucza.

Treść: Otrzymujesz listę liczb naturalnych oraz liczbę naturalną jako klucz. Znajdź indeks odpowiadający pierwszemu wystąpieniu klucza w liście. Jeśli klucz nie występuje w liście, zwróć -1.

Dane wejściowe: Lista liczb naturalnych oraz liczba naturalna jako klucz.

Dane wyjściowe: Liczba całkowita oznaczająca indeks pierwszego wystąpienia klucza w liście.

Przykład:

Dla otrzymanej listy [2, 9, -1, 3, 8] oraz klucza -1 powinno zostać zwrócone 2.
*/

function pierwszeWystapienieKlucza(lista, klucz) {
  for (let i = 0; i < lista.length; i++) {
    if (lista[i] === klucz) {
      return i;
    }
  }
  return -1;
}

// Testy

function testPierwszeWystapienieKlucza_pozytywne() {
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], -1) === 2);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 9) === 1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 2) === 0);
}

function testPierwszeWystapienieKlucza_negatywne() {
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 0) === -1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 10) === -1);
  console.assert(pierwszeWystapienieKlucza([2, 9, -1, 3, 8], 100) === -1);
}

function main() {
  testPierwszeWystapienieKlucza_pozytywne();
  testPierwszeWystapienieKlucza_negatywne();
}

main();
