/*

Tytul: Wypisanie elementow macierzy spiralnie.

Tresc: Otrzymujesz liste list liczb naturalnych. Zbierz elementy otrzymanej macierzy spiralnie i zapisz je w liscie.

Dane wejsciowe: Lista list liczb naturalnych.

Dane wyjsciowe: Lista.

Przyklad:

Dla otrzymanej macierzy: [[1,2,3], [4,5,6], [7,8,9]], powinna zostac zwrocona lista: [1, 2, 3, 6, 9, 8, 7, 4, 5].
*/

function spiralnie(macierz) {
  const wynik = [];
  let m = macierz.length;
  let n = macierz[0].length;
  let k = 0; // indeks ostatniego wiersza nieprzetworzonego
  let l = 0; // indeks ostatniej kolumny nieprzetworzonej

  while (k < m && l < n) {
    // wypisujemy pierwszy wiersz od pozostalych nieprzetworzonych
    for (let i = l; i < n; i++) {
      wynik.push(macierz[k][i]);
    }
    k++;

    // wypisujemy ostatnia kolumne od pozostalych nieprzetworzonych
    for (let i = k; i < m; i++) {
      wynik.push(macierz[i][n - 1]);
    }
    n--;

    // wypisujemy ostatni wiersz od pozostalych nieprzetworzonych, jesli jeszcze nie wypisalismy wszystkich elementow
    if (k < m) {
      for (let i = n - 1; i >= l; i--) {
        wynik.push(macierz[m - 1][i]);
      }
      m--;
    }

    // wypisujemy pierwsza kolumne od pozostalych nieprzetworzonych, jesli jeszcze nie wypisalismy wszystkich elementow
    if (l < n) {
      for (let i = m - 1; i >= k; i--) {
        wynik.push(macierz[i][l]);
      }
      l++;
    }
  }

  return wynik;
}

// test
function test() {
  const macierz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  const wynik1 = [1, 2, 3, 6, 9, 8, 7, 4, 5];
  const macierz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
  ];
  const wynik2 = [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8];
  console.assert(
    JSON.stringify(spiralnie(macierz1)) === JSON.stringify(wynik1),
    `Niepoprawny wynik dla macierzy ${macierz1}.`
  );
  console.assert(
    JSON.stringify(spiralnie(macierz2)) === JSON.stringify(wynik2),
    `Niepoprawny wynik dla macierzy ${macierz2}.`
  );
}

test();

