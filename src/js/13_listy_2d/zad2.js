/*
Tytuł: Macierz kwadratowa, z elementami będącymi iloczynem współrzędnych.

Treść: Dla otrzymanej liczby naturalnej n, stwórz macierz kwadratową o rozmiarze n x n, której każdy element jest iloczynem jego współrzędnych.

Dane wejściowe: Liczba naturalna n.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej liczby 3 powinna zostać zwrócona macierz: [[0, 0, 0], [0, 1, 2], [0, 2, 4]].
*/

function utworzMacierzKwadratowa(n) {
  const macierz = [];
  for (let i = 0; i < n; i++) {
    const wiersz = [];
    for (let j = 0; j < n; j++) {
      wiersz.push(i * j);
    }
    macierz.push(wiersz);
  }
  return macierz;
}

// test
function test() {
  const oczekiwana = [
    [0, 0, 0],
    [0, 1, 2],
    [0, 2, 4],
  ];
  const wynik = utworzMacierzKwadratowa(3);
  assert(
    wynik.length === oczekiwana.length,
    `Długości macierzy nie są równe. Oczekiwano: ${oczekiwana.length}, otrzymano: ${wynik.length}.`
  );
  for (let i = 0; i < wynik.length; i++) {
    assert(
      wynik[i].length === oczekiwana[i].length,
      `Długości wierszy nie są równe. Oczekiwano: ${oczekiwana[i].length}, otrzymano: ${wynik[i].length}.`
    );
    for (let j = 0; j < wynik[i].length; j++) {
      assert(
        wynik[i][j] === oczekiwana[i][j],
        `Element macierzy o indeksie (${i}, ${j}) nie jest taki sam jak w oczekiwanej macierzy. Oczekiwano: ${oczekiwana[i][j]}, otrzymano: ${wynik[i][j]}.`
      );
    }
  }
}
function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}
test();
