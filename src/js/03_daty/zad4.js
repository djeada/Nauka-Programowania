/*
Tytuł: Dzień tygodnia odpowiadający danej liczbie.

Treść: Napisz program, który dla pobranej liczby naturalnej będzie wypisywał dzień tygodnia odpowiadający tej liczbie. Jeśli otrzymano liczbę niedodatnią bądź dodatnią większą niż 7, program powinien wypisać komunikat informujący użytkownika, że liczba jest niepoprawna.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat o dniu tygodnia.

Przykład:

Dla pobranej liczby 2, program powinien wypisać napis "Wtorek".
*/

// Pobieranie danych od użytkownika
const dzien_tygodnia = parseInt(prompt("Podaj dzień tygodnia:"));

// Sprawdzenie, czy liczba jest poprawna
if (dzien_tygodnia > 0 && dzien_tygodnia < 8) {
    // Sprawdzenie, który dzień tygodnia odpowiada liczbie
    if (dzien_tygodnia === 1) {
        console.log("Poniedziałek");
    } else if (dzien_tygodnia === 2) {
        console.log("Wtorek");
    } else if (dzien_tygodnia === 3) {
        console.log("Środa");
    } else if (dzien_tygodnia === 4) {
        console.log("Czwartek");
    } else if (dzien_tygodnia === 5) {
        console.log("Piątek");
    } else if (dzien_tygodnia === 6) {
        console.log("Sobota");
    } else {
        console.log("Niedziela");
    }
} else {
    console.log("Liczba jest niepoprawna");
}