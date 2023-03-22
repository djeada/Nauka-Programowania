/*

Tytuł: Trójkąt Pascala.

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej wypisze trójkąt Pascala o wysokości równej tej liczbie.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat.

Przykład:

Dla otrzymanej liczby 3 powinno zostać wypisane:

  1
  11
  121

*/

// Funkcja wypisująca trójkąt Pascala o wysokości równej liczbie
function rysujTrojkatPascala(wysokosc) {
  var trojkat = [];

  for (var i = 0; i < wysokosc; i++) {
    trojkat[i] = new Array(i + 1);

    for (var j = 0; j <= i; j++) {
      if (j == 0 || j == i) {
        trojkat[i][j] = 1;
      } else {
        trojkat[i][j] = trojkat[i - 1][j - 1] + trojkat[i - 1][j];
      }
    }
  }

  for (i = 0; i < wysokosc; i++) {
    var wiersz = "";
    for (j = 0; j <= i; j++) {
      wiersz += trojkat[i][j] + " ";
    }
    console.log(wiersz);
  }
}

// Testy
console.log("Rysuj trójkąt Pascala o wysokości 2");
rysujTrojkatPascala(2);

console.log("\nRysuj trójkąt Pascala o wysokości 3");
rysujTrojkatPascala(3);

console.log("\nRysuj trójkąt Pascala o wysokości 4");
rysujTrojkatPascala(4);
