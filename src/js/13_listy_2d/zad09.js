/*
Tytul: Klepsydra o najwiekszej sumie.

Tresc: Otrzymasz liste list liczb naturalnych. Znajdz w macierzy klepsydre o najwiekszej sumie. Klepsydra sklada sie dokladnie z 7 elementow. Pierwsze trzy elementy sa kolejnymi elementami dowolnego wiersza macierzy. Czwarty element znajduje sie w tej samej kolumnie co drugi element i o jeden wiersz nizej. Ostatnie trzy elementy znajduja sie w tych samych kolumnach co trzy pierwsze i o dwa wiersze nizej.

Podpowiedz: Nastepujaca macierz:

      1 2 3
      4 5 6
      7 8 9

ma tylko jedna klepsydre:

      1 2 3
        5
      7 8 9

Dane wejsciowe: Lista list liczb naturalnych.

Dane wyjsciowe: Liczba naturalna.

Przyklad:

Dla otrzymanej macierzy: [[7, 4, 2, 0], [4, 8, 10, 8], [3, 6, 7, 6], [3, 9, 19, 14]], powinna zostac zwrocona liczba: 75.

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
  console.assert(
    najwiekszaSumaKlepsydry(macierz) === wynik,
    `Niepoprawny wynik dla macierzy ${macierz}.`
  );
}

test();

