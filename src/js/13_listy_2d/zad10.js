/*

Tytul: Obroc macierz o 90 stopni.

Tresc: Otrzymujesz macierz skladajaca sie z liczb naturalnych. Obroc ja o 90 stopni. Tzn. zamien miejscami ostatnia kolumne z ostatnim wierszem, przedostatnia kolumne z przedostatnim wierszem itd.

Dane wejsciowe: Macierz skladajaca sie z liczb naturalnych.

Dane wyjsciowe: Macierz skladajaca sie z liczb naturalnych.

Przyklad:

Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostac zwrocona macierz: [[7,4,1], [8,5,2], [9,6,3]].
*/
function obrocMacierz(macierz) {
  const n = macierz.length;

  // odwroc kolejnosc kolumn
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n / 2; j++) {
      const temp = macierz[i][j];
      macierz[i][j] = macierz[i][n - j - 1];
      macierz[i][n - j - 1] = temp;
    }
  }

  // zamien wiersze z kolumnami
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      const temp = macierz[i][j];
      macierz[i][j] = macierz[j][i];
      macierz[j][i] = temp;
    }
  }

  return macierz;
}

// test
function test() {
  const macierz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  const wynik = [
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3],
  ];
  const wynikTestowy = obrocMacierz(macierz);
  let czyPoprawny = true;
  for (let i = 0; i < wynik.length; i++) {
    for (let j = 0; j < wynik[i].length; j++) {
      if (wynik[i][j] !== wynikTestowy[i][j]) {
        czyPoprawny = false;
        break;
      }
    }
  }
  if (czyPoprawny) {
    console.log("Test przeszedl pomyslnie");
  } else {
    console.error("Niepoprawny wynik dla macierzy ", macierz);
  }
}

test();

