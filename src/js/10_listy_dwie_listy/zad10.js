/*
Tytuł: Znajdź medianę dwóch posortowanych list.

Treść: Otrzymujesz dwie posortowane listy liczb całkowitych równej długości. Znajdź ich medianę.

Dane wejściowe: Dwie listy liczb całkowitych o równej długości.

Dane wyjściowe: Liczba zmiennoprzecinkowa.

Przykład:

Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinno zostać zwrócone: 4.5.
*/

// Funkcja zwracająca medianę dwóch posortowanych list
function znajdzMediane(lista1, lista2) {
  let wynik = [];
  let maxLength = Math.max(lista1.length, lista2.length);

  for (let i = 0; i < maxLength; i++) {
    let element1 = lista1[i] || 0;
    let element2 = lista2[i] || 0;
    if (element1 !== element2) {
      wynik.push(element1);
      wynik.push(element2);
    }
  }

  return wynik;
}

// Testy

function testZnajdzMediane() {
  console.assert(znajdzMediane([2, 4, 7], [3, 5, 9]) === 4.5);
  console.assert(znajdzMediane([2, 4, 7], [3, 5, 9, 2]) === 4.5);
  console.assert(znajdzMediane([2, 4, 7], [3, 5, 9, 2, 4]) === 4.5);
  console.assert(znajdzMediane([2, 4, 7], [3, 5, 9, 2, 4, 7]) === 4.5);
}

testZnajdzMediane();
