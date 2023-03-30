/*
Tytul: Macierz z parami elementow odpowiadajacych sobie z dwoch list.

Tresc: Dla otrzymanych dwoch list, stworz dwukolumnowa macierz, ktorej pierwsza kolumna sklada sie z elementow pierwszej listy, a druga kolumna z elementow drugiej listy. Jesli otrzymane listy nie sa rownej dlugosci, zwroc pusta macierz.

Dane wejsciowe: Dwie listy.

Dane wyjsciowe: Lista list liczb naturalnych lub pusta macierz (w przypadku nierownych dlugosci list).

Przyklad:

Dla otrzymanych dwoch list: [3, 5, 2] oraz [2, 8, 1], powinna zostac zwrocona macierz: [[3, 2], [5, 8], [2, 1]
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
  console.assert(
    wynik.length === oczekiwana.length,
    `Dlugosci macierzy nie sa rowne. Oczekiwano: ${oczekiwana.length}, otrzymano: ${wynik.length}.`
  );
  for (let i = 0; i < wynik.length; i++) {
    console.assert(
      wynik[i].length === oczekiwana[i].length,
      `Dlugosci kolumn nie sa rowne. Oczekiwano: ${oczekiwana[i].length}, otrzymano: ${wynik[i].length}.`
    );
    for (let j = 0; j < wynik[i].length; j++) {
      console.assert(
        wynik[i][j] === oczekiwana[i][j],
        `Element macierzy o indeksie (${i}, ${j}) nie jest taki sam jak w oczekiwanej macierzy. Oczekiwano: ${oczekiwana[i][j]}, otrzymano: ${wynik[i][j]}.`
      );
    }
  }
}

test();

