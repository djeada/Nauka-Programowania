/*
Tytuł: Klepsydra o największej sumie.

Treść: Otrzymasz listę list liczb naturalnych. Znajdź w macierzy klepsydrę o największej sumie. Klepsydra składa się dokładnie z 7 elementów. Pierwsze trzy elementy są kolejnymi elementami dowolnego wiersza macierzy. Czwarty element znajduje się w tej samej kolumnie co drugi element i o jeden wiersz niżej. Ostatnie trzy elementy znajdują się w tych samych kolumnach co trzy pierwsze i o dwa wiersze niżej.

Podpowiedź: Następująca macierz:

      1 2 3
      4 5 6
      7 8 9

ma tylko jedną klepsydrę:

      1 2 3
        5
      7 8 9

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Liczba naturalna.

Przykład:

Dla otrzymanej macierzy: [[7, 4, 2, 0], [4, 8, 10, 8], [3, 6, 7, 6], [3, 9, 19, 14]], powinna zostać zwrócona liczba: 75.

*/

function najwiekszaSumaKlepsydry(macierz) {
  const n = macierz.length;
  let najwiekszaSuma = 0;

  for (let i = 0; i <= n - 3; i++) {
    for (let j = 0; j <= n - 3; j++) {
      const suma =
        macierz[i][j] +
        macierz[i][j + 1] +
        macierz[i][j + 2] +
        macierz[i + 1][j + 1] +
        macierz[i + 2][j] +
        macierz[i + 2][j + 1] +
        macierz[i + 2][j + 2];

      if (suma > najwiekszaSuma) {
        najwiekszaSuma = suma;
      }
    }
  }

  return najwiekszaSuma;
}

// test
function test() {
  const macierz = [
    [7, 4, 2, 0],
    [4, 8, 10, 8],
    [3, 6, 7, 6],
    [3, 9, 19, 14],
  ];
  const wynik = 75;
  assert(
    najwiekszaSumaKlepsydry(macierz) === wynik,
    `Niepoprawny wynik dla macierzy ${macierz}.`
  );
}
function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}
test();
