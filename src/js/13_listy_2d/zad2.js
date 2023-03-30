/*
Tytul: Macierz kwadratowa, z elementami bedacymi iloczynem wspolrzednych.

Tresc: Dla otrzymanej liczby naturalnej n, stworz macierz kwadratowa o rozmiarze n x n, ktorej kazdy element jest iloczynem jego wspolrzednych.

Dane wejsciowe: Liczba naturalna n.

Dane wyjsciowe: Lista list liczb naturalnych.

Przyklad:

Dla otrzymanej liczby 3 powinna zostac zwrocona macierz: [[0, 0, 0], [0, 1, 2], [0, 2, 4]].
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
  console.assert(
    wynik.length === oczekiwana.length,
    `Dlugosci macierzy nie sa rowne. Oczekiwano: ${oczekiwana.length}, otrzymano: ${wynik.length}.`
  );
  for (let i = 0; i < wynik.length; i++) {
    console.assert(
      wynik[i].length === oczekiwana[i].length,
      `Dlugosci wierszy nie sa rowne. Oczekiwano: ${oczekiwana[i].length}, otrzymano: ${wynik[i].length}.`
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

