/*
Tytuł: Macierz z parami elementów odpowiadających sobie z dwóch list.

Treść: Dla otrzymanych dwóch list, stwórz dwukolumnową macierz, której pierwsza kolumna składa się z elementów pierwszej listy, a druga kolumna z elementów drugiej listy. Jeśli otrzymane listy nie są równej długości, zwróć pustą macierz.

Dane wejściowe: Dwie listy.

Dane wyjściowe: Lista list liczb naturalnych lub pusta macierz (w przypadku nierównych długości list).

Przykład:

Dla otrzymanych dwóch list: [3, 5, 2] oraz [2, 8, 1], powinna zostać zwrócona macierz: [[3, 2], [5, 8], [2, 1]
*/

function utworzMacierzZList(listA, listB) {
  const macierz = [];
  if (listA.length !== listB.length) {
    return macierz;
  }
  for (let i = 0; i < listA.length; i++) {
    macierz.push([listA[i], listB[i]]);
  }
  return macierz;
}

// test
function test() {
  const oczekiwana = [
    [3, 2],
    [5, 8],
    [2, 1],
  ];
  const wynik = utworzMacierzZList([3, 5, 2], [2, 8, 1]);
  assert(
    wynik.length === oczekiwana.length,
    `Długości macierzy nie są równe. Oczekiwano: ${oczekiwana.length}, otrzymano: ${wynik.length}.`
  );
  for (let i = 0; i < wynik.length; i++) {
    assert(
      wynik[i].length === oczekiwana[i].length,
      `Długości kolumn nie są równe. Oczekiwano: ${oczekiwana[i].length}, otrzymano: ${wynik[i].length}.`
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
