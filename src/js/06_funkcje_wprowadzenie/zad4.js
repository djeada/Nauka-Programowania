/*

Tytuł: Maks i min

Napisz funkcję, która:

a) Dla otrzymanych dwóch liczb zwróci mniejszą.

b) Dla otrzymanych dwóch liczb zwróci większą.

c) Dla otrzymanych trzech liczb zwróci najmniejszą.

d) Dla otrzymanych trzech liczb zwróci największą.

Dane wejściowe:

a) Dwie liczby naturalne.

b) Dwie liczby naturalne.

c) Trzy liczby naturalne.

d) Trzy liczby naturalne.

Dane wyjściowe: Liczba naturalna dla wszystkich podpunktów.

Przykład:

a) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrócić liczbę 1.

b) Dla otrzymanych liczb 3 i 1, funkcja powinna zwrócić liczbę 3.

c) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrócić liczbę 1.

d) Dla otrzymanych liczb 3, 2 i 1, funkcja powinna zwrócić liczbę 3.
*/

// Funkcja zwracająca mniejszą liczbę
function zwracajMniejszaLiczbe(liczba_a, liczba_b) {
    if (liczba_a < liczba_b) {
        return liczba_a;
    } else {
        return liczba_b;
    }
}

// Funkcja zwracająca większą liczbę
function zwracajWiekszaLiczbe(liczba_a, liczba_b) {
    if (liczba_a > liczba_b) {
        return liczba_a;
    } else {
        return liczba_b;
    }
}

// Funkcja zwracająca najmniejszą liczbę
function zwracajNajmniejszaLiczbe(liczba_a, liczba_b, liczba_c) {
    if (liczba_a < liczba_b && liczba_a < liczba_c) {
        return liczba_a;
    } else if (liczba_b < liczba_a && liczba_b < liczba_c) {
        return liczba_b;
    } else {
        return liczba_c;
    }
}

// Funkcja zwracająca największą liczbę
function zwracajNajwiekszaLiczbe(liczba_a, liczba_b, liczba_c) {
    if (liczba_a > liczba_b && liczba_a > liczba_c) {
        return liczba_a;
    } else if (liczba_b > liczba_a && liczba_b > liczba_c) {
        return liczba_b;
    } else {
        return liczba_c;
    }
}

// Pobieranie danych od użytkownika
var liczba_a = prompt('Podaj pierwszą liczbę: ');
var liczba_b = prompt('Podaj drugą liczbę: ');
var liczba_c = prompt('Podaj trzecią liczbę: ');

// Wyświetlanie wyników
console.log('Mniejsza liczba to: ' + zwracajMniejszaLiczbe(liczba_a, liczba_b));
console.log('Większa liczba to: ' + zwracajWiekszaLiczbe(liczba_a, liczba_b));
console.log('Najmniejsza liczba to: ' + zwracajNajmniejszaLiczbe(liczba_a, liczba_b, liczba_c));
console.log('Największa liczba to: ' + zwracajNajwiekszaLiczbe(liczba_a, liczba_b, liczba_c));