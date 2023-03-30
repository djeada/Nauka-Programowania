/*
Tytul: Podnies a do b.	

Tresc: Napisz funkcje, ktora dla otrzymanych dwoch liczb obliczy ile wynosi a podniesione do b, przy pomocy petli.

Dane wejsciowe: dwie liczby naturalne

Dane wyjsciowe: liczba naturalna

Przyklad:

Dla pobranych liczb 3 i 5, funkcja powinna zwrocic liczbe 243.
*/

// Funkcja zwracajaca a podniesione do b
function podniesDoPotegi(a, b) {
  var wynik = 1;
  for (var i = 0; i < b; i++) {
    wynik *= a;
  }
  return wynik;
}

// Testy

function testPotega() {
  console.assert(podniesDoPotegi(2, 3) == 8);
  console.assert(podniesDoPotegi(3, 2) == 9);
  console.assert(podniesDoPotegi(4, 4) == 256);
  console.assert(podniesDoPotegi(5, 3) == 125);
  console.assert(podniesDoPotegi(6, 0) == 1);
  console.assert(podniesDoPotegi(7, 1) == 7);
  console.assert(podniesDoPotegi(0, 2) == 0);
}

// Funkcja uruchamiajaca testy
function main() {
  testPotega();
}

// Uruchomienie testow
main();

