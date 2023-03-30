/*
Tytul: Zerowanie macierzy.

Tresc: Otrzymujesz liste list liczb naturalnych reprezentujaca macierz. Jesli element macierzy jest rowny zero, zamien wszystkie elementy tej samej kolumny i wiersza na zera.

Dane wejsciowe: Lista list liczb naturalnych.

Dane wyjsciowe: Lista list liczb naturalnych.

Przyklad:

Dla otrzymanej macierzy: [[1,2,3], [4,0,6], [7,8,9]], powinna zostac zwrocona macierz: [[1,0,3], [0,0,0], [7,0,9]].
*/

function zerujMacierz(macierz) {
  const m = macierz.length;
  const n = macierz[0].length;
  const wierszeDoZerowania = new Set(); // przechowuje numery wierszy, ktore trzeba wyzerowac
  const kolumnyDoZerowania = new Set(); // przechowuje numery kolumn, ktore trzeba wyzerowac

  // znajdujemy numery wierszy i kolumn, ktore trzeba wyzerowac
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (macierz[i][j] === 0) {
        wierszeDoZerowania.add(i);
        kolumnyDoZerowania.add(j);
      }
    }
  }

  // wyzerowujemy wiersze i kolumny
  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (wierszeDoZerowania.has(i) || kolumnyDoZerowania.has(j)) {
        macierz[i][j] = 0;
      }
    }
  }

  return macierz;
}

// test
function test() {
  const macierz1 = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9],
  ];
  const wynik1 = [
    [1, 0, 3],
    [0, 0, 0],
    [7, 0, 9],
  ];
  const macierz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0],
  ];
  const wynik2 = [
    [1, 2, 0],
    [4, 5, 0],
    [0, 0, 0],
  ];
  console.assert(
    JSON.stringify(zerujMacierz(macierz1)) === JSON.stringify(wynik1),
    `Niepoprawny wynik dla macierzy ${macierz1}.`
  );
  console.assert(
    JSON.stringify(zerujMacierz(macierz2)) === JSON.stringify(wynik2),
    `Niepoprawny wynik dla macierzy ${macierz2}.`
  );
}

test();

