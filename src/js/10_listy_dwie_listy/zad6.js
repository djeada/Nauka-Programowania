/*

Tytuł: Znalezienie elementów wspólnych dwóch list.

Treść: Otrzymujesz dwie listy liczb całkowitych. Znajdź elementy występujące zarówno w pierwszej, jak i w drugiej liście.

Dane wejściowe: Dwie listy liczb całkowitych.

Dane wyjściowe: Lista liczb całkowitych.

Przykład:

Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] zostanie zwrócona lista: [2, 4].

*/

// Funkcja zwracająca listę elementów występujących zarówno w pierwszej, jak i w drugiej liście
function znajdzElementyWspolne(lista1, lista2) {
  let wynik = [];
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    let element1 = lista1[i] || 0;
    let element2 = lista2[i] || 0;
    if (element1 === element2) {
      wynik.push(element1);
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

function testZnajdzElementyWspolne() {
  assert(
    znajdzElementyWspolne([9, 2, 5, 4], [4, 2, 1]).toString() ===
      [2, 4].toString()
  );
  assert(
    znajdzElementyWspolne([9, 2, 5, 4], [4, 2, 1, 9]).toString() ===
      [2, 4, 9].toString()
  );
  assert(
    znajdzElementyWspolne([9, 2, 5, 4], [4, 2, 1, 9, 5]).toString() ===
      [2, 4, 5, 9].toString()
  );
  assert(
    znajdzElementyWspolne([9, 2, 5, 4], [4, 2, 1, 9, 5, 2]).toString() ===
      [2, 4, 5, 9].toString()
  );
}

testZnajdzElementyWspolne();
