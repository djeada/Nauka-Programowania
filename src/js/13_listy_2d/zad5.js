/*
Tytuł: Sprawdzanie czy macierz jest "magiczna".

Treść: Otrzymujesz macierz kwadratową. Sprawdź, czy jest ona kwadratem magicznym.

Podpowiedź: Kwadrat magiczny składa się z powtarzających się dodatnich liczb naturalnych. Suma elementów w każdym wierszu, w każdej kolumnie oraz na każdej przekątnej jest taka sama.

Dane wejściowe: Lista list liczb naturalnych.

Dane wyjściowe: Wartość logiczna.

Przykład:

Dla otrzymanej macierzy: [[6, 7, 2], [1, 5, 9], [8, 3, 4]], powinna zostać zwrócona wartość logiczna: Prawda.
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
  assert(
    czyKwadratMagiczny(macierz1) === wynik1,
    `Macierz ${macierz1} nie jest kwadratem magicznym, a powinna być.`
  );
  assert(
    czyKwadratMagiczny(macierz2) === wynik2,
    `Macierz ${macierz2} jest kwadratem magicznym, a nie powinna być.`
  );
}

function assert(condition, message) {
  if (!condition) {
    throw message || "Wystąpił błąd";
  }
}
test();
