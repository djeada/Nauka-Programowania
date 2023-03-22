/*
Tytuł: N pierwszych liczb pierwszych.

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej N, wypisze N pierwszych liczb pierwszych.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: N liczb pierwszych.

Przykład:

Dla otrzymanej liczby 5 powinno zostać wypisane: 2, 3, 5, 7, 11.
*/

// Funkcja sprawdzająca czy liczba jest pierwsza
function czyLiczbaPierwsza(liczba) {
  if (liczba <= 1) {
    return false;
  }

  for (var i = 2; i * i <= liczba; i++) {
    if (liczba % i === 0) {
      return false;
    }
  }
  return true;
}

// Funkcja wypisująca N pierwszych liczb pierwszych
function wypiszNPierwszychLiczbPierwszych(N) {
  var liczbyPierwsze = [];
  var liczba = 2;

  while (liczbyPierwsze.length < N) {
    if (czyLiczbaPierwsza(liczba)) {
      liczbyPierwsze.push(liczba);
    }
    liczba++;
  }

  console.log(liczbyPierwsze.join(", "));
}

// Testy
console.log("Wypisz 2 pierwsze liczby pierwsze");
wypiszNPierwszychLiczbPierwszych(2);

console.log("\nWypisz 3 pierwsze liczby pierwsze");
wypiszNPierwszychLiczbPierwszych(3);

console.log("\nWypisz 4 pierwsze liczby pierwsze");
wypiszNPierwszychLiczbPierwszych(4);
