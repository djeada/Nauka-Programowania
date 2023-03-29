/*
Tytuł: Zerowanie macierzy.

Treść: Otrzymujesz listę list liczb naturalnych reprezentującą macierz. Jeśli element macierzy jest równy zero, zamień wszystkie elementy tej samej kolumny i wiersza na zera.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Lista list liczb naturalnych.

Przykład:

Dla otrzymanej macierzy: [[1,2,3], [4,0,6], [7,8,9]], powinna zostać zwrócona macierz: [[1,0,3], [0,0,0], [7,0,9]].
*/

function zerujMacierz(macierz) {
  const m = macierz.length;
  const n = macierz[0].length;
  const wierszeDoZerowania = new Set(); // przechowuje numery wierszy, które trzeba wyzerować
  const kolumnyDoZerowania = new Set(); // przechowuje numery kolumn, które trzeba wyzerować

  // znajdujemy numery wierszy i kolumn, które trzeba wyzerować
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
  assert(
    JSON.stringify(zerujMacierz(macierz1)) === JSON.stringify(wynik1),
    `Niepoprawny wynik dla macierzy ${macierz1}.`
  );
  assert(
    JSON.stringify(zerujMacierz(macierz2)) === JSON.stringify(wynik2),
    `Niepoprawny wynik dla macierzy ${macierz2}.`
  );
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}
test();
