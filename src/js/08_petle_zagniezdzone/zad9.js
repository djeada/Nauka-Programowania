/*
Tytul: N pierwszych liczb pierwszych.

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej N, wypisze N pierwszych liczb pierwszych.

Dane wejsciowe: Liczba naturalna.

Dane wyjsciowe: N liczb pierwszych.

Przyklad:

Dla otrzymanej liczby 5 powinno zostac wypisane: 2, 3, 5, 7, 11.
*/

// Funkcja sprawdzajaca czy liczba jest pierwsza
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

// Funkcja wypisujaca N pierwszych liczb pierwszych
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

