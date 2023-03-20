/*

Tytuł: Pierwiastek metodą Newtona

Treść: Napisz funkcję, która dla otrzymanej liczby naturalnej zwróci jej pierwiastek.

Dane wejściowe: liczba naturalna

Dane wyjściowe: liczba naturalna

Przykład:

Dla otrzymanej liczby 16, funkcja powinna zwrócić liczbę 4.
*/

// Funkcja zwracająca pierwiastek z liczby
function pierwiastekLiczby(liczba) {
    var pierwiastek = liczba;
    while (pierwiastek * pierwiastek > liczba) {
        pierwiastek = (pierwiastek + liczba / pierwiastek) / 2;
    }
    return pierwiastek;
}

// Testy
function assert(condition, message) {
    if (!condition) {
        throw new Error(message || "Assertion failed");
    }
}