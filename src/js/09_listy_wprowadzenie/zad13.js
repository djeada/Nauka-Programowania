/*

Tytul: Znalezienie brakujacego elementu w liscie.

Tresc: Dla dostarczonej listy, skladajacej sie z nieuporzadkowanych kolejnych (oprocz jednego) elementow ciagu arytmetycznego, znajdz brakujacy element.

Dane wejsciowe: Lista zawierajaca liczby naturalne.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej listy: [5, 2, 1, 3] zostanie zwrocona liczba: 4.
*/

// Funkcja znajdujaca brakujacy element w ciagu arytmetycznym
function znajdzBrakujacyElement(lista) {
  const n = lista.length + 1;
  const sumaKolejnychLiczb = (n * (n + 1)) / 2;
  const sumaListy = lista.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    0
  );
  return sumaKolejnychLiczb - sumaListy;
}

// Testy

function testZnajdzBrakujacyElement() {
  console.assert(znajdzBrakujacyElement([5, 2, 1, 3]) === 4);
  console.assert(znajdzBrakujacyElement([1, 3, 4, 5, 6]) === 2);
  console.assert(znajdzBrakujacyElement([1, 2, 4]) === 3);
  console.assert(znajdzBrakujacyElement([3, 5, 6, 7, 8]) === 4);
}

testZnajdzBrakujacyElement();

