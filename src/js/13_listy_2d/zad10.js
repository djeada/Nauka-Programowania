/*

Tytuł: Obróć macierz o 90 stopni.

Treść: Otrzymujesz macierz składającą się z liczb naturalnych. Obróć ją o 90 stopni. Tzn. zamień miejscami ostatnią kolumnę z ostatnim wierszem, przedostatnią kolumnę z przedostatnim wierszem itd.

Dane wejściowe: Macierz składająca się z liczb naturalnych.

Dane wyjściowe: Macierz składająca się z liczb naturalnych.

Przykład:

Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostać zwrócona macierz: [[7,4,1], [8,5,2], [9,6,3]].
*/
function obrocMacierz(macierz) {
  const n = macierz.length;

  // odwróć kolejność kolumn
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n / 2; j++) {
      const temp = macierz[i][j];
      macierz[i][j] = macierz[i][n - j - 1];
      macierz[i][n - j - 1] = temp;
    }
  }

  // zamień wiersze z kolumnami
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
    console.log("Test przeszedł pomyślnie");
  } else {
    console.error("Niepoprawny wynik dla macierzy ", macierz);
  }
}

test();
