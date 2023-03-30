/*

Tytul: Wyszukiwanie liniowe rekurencyjnie.

Tresc: Otrzymujesz liste liczb naturalnych oraz liczbe naturalna klucz. Przy uzyciu rekurencji znajdz indeks odpowiadajacy pierwszemu wystapieniu klucza w liscie. Jesli klucz nie wystepuje w liscie, zwroc -1.

Dane wejsciowe: Lista liczb naturalnych oraz liczba naturalna klucz.

Dane wyjsciowe: Liczba calkowita.

Przyklad:

Dla otrzymanej listy oraz liczby: [1, 2, 2] i 2, powinna zostac zwrocona liczba: 1.
*/

function wyszukiwanieLinioweRekurencyjnie(lista, klucz) {
  if (lista.length === 0) {
    return -1;
  }
  if (lista[0] === klucz) {
    return 0;
  }
  var wynik = wyszukiwanieLinioweRekurencyjnie(lista.slice(1), klucz);
  if (wynik === -1) {
    return -1;
  }
  return wynik + 1;
}

function test() {
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 2) === 1,
    "Test 1 failed"
  );
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 3) === -1,
    "Test 2 failed"
  );
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 1) === 0,
    "Test 3 failed"
  );
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 4) === -1,
    "Test 4 failed"
  );
  console.assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 0) === -1,
    "Test 5 failed"
  );
}

test();

