/*

Tytul: Naiwny test pierwszosci

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej sprawdzi, czy jest ona liczba pierwsza.

Dane wejsciowe: liczba naturalna

Dane wyjsciowe: wartosc logiczna

Przyklad:

Dla otrzymanej liczby 7, funkcja powinna zwrocic wartosc logiczna prawda. Dla otrzymanej liczby 2, funkcja powinna zwrocic wartosc logiczna prawda.
*/

// Funkcja zwracajaca wartosc logiczna, czy liczba jest pierwsza
function czyPierwsza(liczba) {
  if (liczba < 2) {
    return false;
  }
  for (var i = 2; i < liczba; i++) {
    if (liczba % i == 0) {
      return false;
    }
  }
  return true;
}

// Testy

function testCzyPierwsza() {
  console.assert(czyPierwsza(2) == true);
  console.assert(czyPierwsza(3) == true);
  console.assert(czyPierwsza(4) == false);
  console.assert(czyPierwsza(7) == true);
  console.assert(czyPierwsza(9) == false);
  console.assert(czyPierwsza(11) == true);
  console.assert(czyPierwsza(13) == true);
  console.assert(czyPierwsza(14) == false);
  console.assert(czyPierwsza(16) == false);
  console.assert(czyPierwsza(19) == true);
}

// Funkcja uruchamiajaca testy
function main() {
  testCzyPierwsza();
}

// Uruchomienie testow
main();

