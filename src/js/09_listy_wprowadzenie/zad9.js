/*
Tytuł: Usuń duplikaty.

Treść: Otrzymujesz listę liczb naturalnych. Usuń z niej wszystkie duplikaty, tak aby każda liczba pozostała tylko raz.

Dane wejściowe: Lista liczb naturalnych.

Dane wyjściowe: Lista liczb naturalnych.

Przykład:

Dla otrzymanej listy: [3, 2, 1, 3, 2, 2], powinna zostać zwrócona lista: [3, 2, 1].

*/

function usunDuplikaty(lista) {
  var wynik = [];

  for (var i = 0; i < lista.length; i++) {
    if (wynik.indexOf(lista[i]) === -1) {
      wynik.push(lista[i]);
    }
  }

  return wynik;
}

// Testy
function assert(condition, message) {
  if (!condition) {
    throw new Error(message || "Assertion failed");
  }
}

function testUsunDuplikaty() {
  assert(usunDuplikaty([3, 2, 1, 3, 2, 2]).toString() === [3, 2, 1].toString());
  assert(
    usunDuplikaty([1, 2, 3, 4, 5, 6]).toString() ===
      [1, 2, 3, 4, 5, 6].toString()
  );
  assert(
    usunDuplikaty([6, 5, 4, 3, 2, 1]).toString() ===
      [6, 5, 4, 3, 2, 1].toString()
  );
}

function main() {
  testUsunDuplikaty();
}

main();
