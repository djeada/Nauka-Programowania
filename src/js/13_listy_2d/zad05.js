/*
Tytul: Sprawdzanie czy macierz jest "magiczna".

Tresc: Otrzymujesz macierz kwadratowa. Sprawdz, czy jest ona kwadratem magicznym.

Podpowiedz: Kwadrat magiczny sklada sie z powtarzajacych sie dodatnich liczb naturalnych. Suma elementow w kazdym wierszu, w kazdej kolumnie oraz na kazdej przekatnej jest taka sama.

Dane wejsciowe: Lista list liczb naturalnych.

Dane wyjsciowe: Wartosc logiczna.

Przyklad:

Dla otrzymanej macierzy: [[6, 7, 2], [1, 5, 9], [8, 3, 4]], powinna zostac zwrocona wartosc logiczna: Prawda.
*/

function czyKwadratMagiczny(macierz) {
  const n = macierz.length;
  const sumaOczekiwana = (n * (n * n + 1)) / 2;
  let sumaWiersza,
    sumaKolumny,
    sumaPrzekatnej1 = 0,
    sumaPrzekatnej2 = 0;
  for (let i = 0; i < n; i++) {
    sumaWiersza = 0;
    sumaKolumny = 0;
    for (let j = 0; j < n; j++) {
      sumaWiersza += macierz[i][j];
      sumaKolumny += macierz[j][i];
      if (i === j) {
        sumaPrzekatnej1 += macierz[i][j];
      }
      if (i + j === n - 1) {
        sumaPrzekatnej2 += macierz[i][j];
      }
    }
    if (sumaWiersza !== sumaOczekiwana || sumaKolumny !== sumaOczekiwana) {
      return false;
    }
  }
  if (
    sumaPrzekatnej1 !== sumaOczekiwana ||
    sumaPrzekatnej2 !== sumaOczekiwana
  ) {
    return false;
  }
  return true;
}

// test
function test() {
  const macierz1 = [
    [6, 7, 2],
    [1, 5, 9],
    [8, 3, 4],
  ];
  const wynik1 = true;
  const macierz2 = [
    [6, 7, 2],
    [1, 5, 9],
    [8, 3, 3],
  ];
  const wynik2 = false;
  console.assert(
    czyKwadratMagiczny(macierz1) === wynik1,
    `Macierz ${macierz1} nie jest kwadratem magicznym, a powinna byc.`
  );
  console.assert(
    czyKwadratMagiczny(macierz2) === wynik2,
    `Macierz ${macierz2} jest kwadratem magicznym, a nie powinna byc.`
  );
}

test();

