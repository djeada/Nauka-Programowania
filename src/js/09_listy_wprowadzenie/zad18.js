/*
Tytul: Znalezienie indeksu najmniejszego elementu w posortowanej i przesunietej w prawo liscie.

Tresc: Dla otrzymanej listy liczb calkowitych, znajdz indeks najmniejszego elementu. Lista jest posortowana rosnaco, ale zostala przesunieta w prawo o okreslona liczbe miejsc. Przykladowo dla przesuniecia w prawo o 1, ostatni element trafia na pierwsze miejsce, a przedostatni na ostatnie miejsce itd.

Dane wejsciowe: Lista liczb calkowitych oraz liczba naturalna okreslajaca przesuniecie w prawo.

Dane wyjsciowe: Liczba calkowita.

Przyklad:

Dla otrzymanej listy: [7, 8, -1, 4, 5] zostanie zwrocona liczba: 2.
*/

// Funkcja znajdujaca indeks najmniejszego elementu w posortowanej i przesunietej w prawo liscie
function znajdzIndeksNajmniejszegoElementu(lista) {
  let indeksNajmniejszego = 0;

  for (let i = 1; i < lista.length; i++) {
    if (lista[i] < lista[indeksNajmniejszego]) {
      indeksNajmniejszego = i;
    }
  }

  return indeksNajmniejszego;
}

// Testy

function testZnajdzIndeksNajmniejszegoElementu() {
  console.assert(znajdzIndeksNajmniejszegoElementu([7, 8, -1, 4, 5]) === 2);
  console.assert(znajdzIndeksNajmniejszegoElementu([4, 5, 7, 8, -1]) === 4);
  console.assert(znajdzIndeksNajmniejszegoElementu([-1, 4, 5, 7, 8]) === 0);
}

testZnajdzIndeksNajmniejszegoElementu();

