/*
Tytul: Minimum oraz maksimum.

Tresc: Otrzymujesz liste liczb calkowitych. Znajdz najwiekszy i najmniejszy element tej listy i zwroc je jako dwie osobne liczby calkowite.

Dane wejsciowe: Lista liczb calkowitych.

Dane wyjsciowe: Dwie liczby calkowite oznaczajace najwiekszy i najmniejszy element z listy.

Przyklad:

Dla otrzymanej listy [4, -7, 8, 5, 6, -9, 10, 2, -8] powinny zostac zwrocone liczby 10 oraz -9.
*/

// Funkcja zwracajaca najwiekszy i najmniejszy element listy
function znajdzMinMax(lista) {
  var min = lista[0];
  var max = lista[0];

  for (var i = 1; i < lista.length; i++) {
    if (lista[i] < min) {
      min = lista[i];
    }
    if (lista[i] > max) {
      max = lista[i];
    }
  }

  return [min, max];
}

// Testy

function testujZnajdzMinMax() {
  var test1 = [4, -7, 8, 5, 6, -9, 10, 2, -8];
  var wynik1 = [-9, 10];
  console.assert(
    JSON.stringify(znajdzMinMax(test1)) === JSON.stringify(wynik1)
  );

  var test2 = [1, 1, 1, 1, 1, 1, 1, 1, 1];
  var wynik2 = [1, 1];
  console.assert(
    JSON.stringify(znajdzMinMax(test2)) === JSON.stringify(wynik2)
  );

  var test3 = [10, -10, 100, -100, 1000, -1000];
  var wynik3 = [-1000, 1000];
  console.assert(
    JSON.stringify(znajdzMinMax(test3)) === JSON.stringify(wynik3)
  );
}

testujZnajdzMinMax();

