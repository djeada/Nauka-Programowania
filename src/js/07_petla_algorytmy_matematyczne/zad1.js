/*
Tytul: Srednia z n liczb

Tresc: Napisz funkcje, ktora dla otrzymanej liczby n, poprosi uzytkownika o podanie n liczb i zwroci ich srednia arytmetyczna.

Dane wejsciowe: liczba naturalna n oraz n liczb

Dane wyjsciowe: liczba naturalna

Przyklad:

Dla pobranych liczb 2, 4 i 6, funkcja powinna zwrocic liczbe 4.
*/

// Funkcja zwracajaca srednia arytmetyczna n liczb
function sredniaArytmetycznaNLiczb(n) {
  var suma = 0;
  for (var i = 0; i < n; i++) {
    var liczba = parseInt(prompt("Podaj liczbe:"));
    suma += liczba;
  }
  return suma / n;
}

// Pobieranie danych od uzytkownika
var n = parseInt(prompt("Podaj liczbe liczb:"));

// Wypisanie wyniku
console.log(sredniaArytmetycznaNLiczb(n));

