/*

Tytuł: Wyszukiwanie liniowe rekurencyjnie.

Treść: Otrzymujesz listę liczb naturalnych oraz liczbę naturalną klucz. Przy użyciu rekurencji znajdź indeks odpowiadający pierwszemu wystąpieniu klucza w liście. Jeśli klucz nie występuje w liście, zwróć -1.

Dane wejściowe: Lista liczb naturalnych oraz liczba naturalna klucz.

Dane wyjściowe: Liczba całkowita.

Przykład:

Dla otrzymanej listy oraz liczby: [1, 2, 2] i 2, powinna zostać zwrócona liczba: 1.
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

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function test() {
  assert(wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 2) === 1, "Test 1 failed");
  assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 3) === -1,
    "Test 2 failed"
  );
  assert(wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 1) === 0, "Test 3 failed");
  assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 4) === -1,
    "Test 4 failed"
  );
  assert(
    wyszukiwanieLinioweRekurencyjnie([1, 2, 2], 0) === -1,
    "Test 5 failed"
  );
}

test();
