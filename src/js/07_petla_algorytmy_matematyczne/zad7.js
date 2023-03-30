/*

Tytul: Pierwiastek metoda Newtona

Tresc: Napisz funkcje, ktora dla otrzymanej liczby naturalnej zwroci jej pierwiastek.

Dane wejsciowe: liczba naturalna

Dane wyjsciowe: liczba naturalna

Przyklad:

Dla otrzymanej liczby 16, funkcja powinna zwrocic liczbe 4.
*/

// Funkcja zwracajaca pierwiastek z liczby
function pierwiastekLiczby(liczba) {
  var pierwiastek = liczba;
  while (pierwiastek * pierwiastek > liczba) {
    pierwiastek = (pierwiastek + liczba / pierwiastek) / 2;
  }
  return pierwiastek;
}

// Testy
function testPierwiastekLiczby() {
  console.assert(
    pierwiastekLiczby(4) === 2,
    "Niepoprawny pierwiastek z liczby 4"
  );
  console.assert(
    pierwiastekLiczby(9) === 3,
    "Niepoprawny pierwiastek z liczby 9"
  );
  console.assert(
    Math.abs(pierwiastekLiczby(2) - 1.41421356) < 0.0001,
    "Niepoprawny pierwiastek z liczby 2"
  );
}

testPierwiastekLiczby();

