/*
Tytuł: Cyfry liczby

Treść: Napisz funkcję, która dla otrzymanej liczby obliczy sumę jej cyfr.

Dane wejściowe: liczba naturalna

Dane wyjściowe: liczba naturalna

Przykład:

Dla pobranej liczby 13231, funkcja powinna zwrócić liczbę 10.
*/

// Funkcja zwracająca sumę cyfr liczby
function sumaCyfrLiczby(liczba) {
  var suma = 0;
  var liczbaTekst = liczba.toString();
  for (var i = 0; i < liczbaTekst.length; i++) {
    suma += parseInt(liczbaTekst[i]);
  }
  return suma;
}

// Pobieranie danych od użytkownika i walidacja
var liczba = parseInt(prompt("Podaj liczbę:"));
while (isNaN(liczba)) {
  liczba = parseInt(prompt("Podaj poprawną liczbę:"));
}

// Wypisanie wyniku
console.log(sumaCyfrLiczby(liczba));
