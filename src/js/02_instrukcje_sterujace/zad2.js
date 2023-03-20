/*
Tytuł: Porównanie ze zmienną.

Treść: Pobierz od użytkownika dwie liczby naturalne i sprawdź, czy są one identyczne. Wypisz odpowiedni komunikat.

Dane wejściowe: Dwie liczby naturalne.

Dane wyjściowe: Komunikat.

Przykład:

Dla pobranych liczb: 7 i 4, powinien zostać wypisany komunikat, że liczby są różne.
*/

// Pobieranie danych od użytkownika
const liczba_a = parseInt(prompt("Podaj pierwszą liczbę:"));
const liczba_b = parseInt(prompt("Podaj drugą liczbę:"));

// Porównanie ze zmienną
if (liczba_a === liczba_b) {
    console.log("Liczby są identyczne");
} else {
    console.log("Liczby są różne");
}