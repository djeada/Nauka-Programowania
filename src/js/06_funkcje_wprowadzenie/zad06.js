/*
Tytul: Cyfry liczby

Tresc: Napisz funkcje, ktora dla otrzymanej liczby obliczy sume jej cyfr.

Dane wejsciowe: liczba naturalna

Dane wyjsciowe: liczba naturalna

Przyklad:

Dla pobranej liczby 13231, funkcja powinna zwrocic liczbe 10.
*/

// Funkcja zwracajaca sume cyfr liczby
function sumaCyfrLiczby(liczba) {
  var suma = 0;
  var liczbaTekst = liczba.toString();
  for (var i = 0; i < liczbaTekst.length; i++) {
    suma += parseInt(liczbaTekst[i]);
  }
  return suma;
}

// Pobieranie danych od uzytkownika i walidacja
var liczba = parseInt(prompt("Podaj liczbe:"));
while (isNaN(liczba)) {
  liczba = parseInt(prompt("Podaj poprawna liczbe:"));
}

// Wypisanie wyniku
console.log(sumaCyfrLiczby(liczba));

