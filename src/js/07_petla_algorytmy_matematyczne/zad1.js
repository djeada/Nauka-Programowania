/*
Tytuł: Średnia z n liczb

Treść: Napisz funkcję, która dla otrzymanej liczby n, poprosi użytkownika o podanie n liczb i zwróci ich średnią arytmetyczną.

Dane wejściowe: liczba naturalna n oraz n liczb

Dane wyjściowe: liczba naturalna

Przykład:

Dla pobranych liczb 2, 4 i 6, funkcja powinna zwrócić liczbę 4.
*/

// Funkcja zwracająca średnią arytmetyczną n liczb
function sredniaArytmetycznaNLiczb(liczba) {
    var suma = 0;
    for (var i = 0; i < liczba; i++) {
        var liczba = parseInt(prompt("Podaj liczbę:"));
        suma += liczba;
    }
    return suma / liczba;
}

// Pobieranie danych od użytkownika
var liczba = parseInt(prompt("Podaj liczbę:"));

// Wypisanie wyniku
console.log(sredniaArytmetycznaNLiczb(liczba));