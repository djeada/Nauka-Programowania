/*

Tytul: Roznica miedzy dwoma listami.

Tresc: Dla otrzymanych dwoch list liczb calkowitych, znajdz elementy, ktore nie sa czescia wspolna obu list.

Dane wejsciowe: Dwie listy liczb calkowitych.

Dane wyjsciowe: Lista liczb calkowitych.

Przyklad:

Dla otrzymanych list [9, 2, 5, 4] oraz [4, 2, 1] powinna zostac zwrocona lista: [9, 5, 1].
*/

// Funkcja zwracajaca liste elementow, ktore nie sa czescia wspolna obu list
function znajdzRoznice(lista1, lista2) {
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

function testZnajdzRoznice() {
  console.assert(
    znajdzRoznice([9, 2, 5, 4], [4, 2, 1]).toString() === [9, 5, 1].toString()
  );
  console.assert(
    znajdzRoznice([9, 2, 5, 4], [4, 2, 1, 9]).toString() === [5, 1].toString()
  );
  console.assert(
    znajdzRoznice([9, 2, 5, 4], [4, 2, 1, 9, 5]).toString() === [1].toString()
  );
  console.assert(
    znajdzRoznice([9, 2, 5, 4], [4, 2, 1, 9, 5, 2]).toString() ===
      [1].toString()
  );
}

testZnajdzRoznice();

