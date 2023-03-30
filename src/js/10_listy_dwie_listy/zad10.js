/*
Tytul: Znajdz mediane dwoch posortowanych list.

Tresc: Otrzymujesz dwie posortowane listy liczb calkowitych rownej dlugosci. Znajdz ich mediane.

Dane wejsciowe: Dwie listy liczb calkowitych o rownej dlugosci.

Dane wyjsciowe: Liczba zmiennoprzecinkowa.

Przyklad:

Dla otrzymanych list [2, 4, 7] oraz [3, 5, 9] powinno zostac zwrocone: 4.5.
*/

// Funkcja zwracajaca mediane dwoch posortowanych list
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

