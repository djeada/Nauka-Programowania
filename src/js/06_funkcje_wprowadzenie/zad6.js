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
    var liczba = liczba.toString();
    for (var i = 0; i < liczba.length; i++) {
        suma += parseInt(liczba[i]);
    }
    return suma;
}

// Pobieranie danych od użytkownika
var liczba = parseInt(prompt("Podaj liczbę:"));

// Wypisanie wyniku
console.log(sumaCyfrLiczby(liczba));