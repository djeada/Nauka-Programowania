/*
Tytuł: Ile dni minęło od początku roku?	

Treść: Dla trzech pobranych liczb: reprezentujących datę wypisz, ile dni minęło od początku roku. Pierwsza liczba jest dniem, druga miesiącem, trzecia rokiem. 

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Liczba naturalna.

Przykład: Dla pobranych liczb: 14, 2 oraz 1482, powinna zostać zwrócona liczba 45.
*/

// Pobieranie danych od użytkownika
const dzien = parseInt(prompt("Podaj dzień:"));
const miesiac = parseInt(prompt("Podaj miesiąc:"));
const rok = parseInt(prompt("Podaj rok:"));

// Sprawdzenie, czy liczby są poprawne
if (dzien > 0 && miesiac > 0 && rok > 0) {
    // Sprawdzenie, czy miesiąc to poprawny
    if (miesiac < 13) {
        // Sprawdzenie, czy rok jest przestępny
        if (rok % 4 === 0 && rok % 100 !== 0 || rok % 400 === 0) {
            // Sprawdzenie, czy dzień jest poprawny
            if (dzien < 30 || (dzien === 30 && miesiac !== 2) || (dzien === 29 && miesiac === 2)) {
                // Sprawdzenie, czy miesiąc to styczeń
                if (miesiac === 1) {
                    console.log(dzien);
                }
                // Sprawdzenie, czy miesiąc to luty
                else if (miesiac === 2) {
                    console.log(dzien + 31);
                }
                // Sprawdzenie, czy miesiąc to marzec
                else if (miesiac === 3) {
                    console.log(dzien + 31 + 29);
                }
                // Sprawdzenie, czy miesiąc to kwiecień
                else if (miesiac === 4) {
                    console.log(dzien + 31 + 29 + 31);
                }
                // Sprawdzenie, czy miesiąc to maj
                else if (miesiac === 5) {
                    console.log(dzien + 31 + 29 + 31 + 30);
                }
                // Sprawdzenie, czy miesiąc to czerwiec
                else if (miesiac === 6) {
                    console.log(dzien + 31 + 29 + 31 + 30 + 31);
                }
                // Sprawdzenie, czy miesiąc to lipiec
                else if (miesiac === 7) {
                    console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30);
                }
                // Sprawdzenie, czy miesiąc to sierpień
                else if (miesiac === 8) {
                    console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 +
                        31);
                }
                // Sprawdzenie, czy miesiąc to wrzesień
                else if (miesiac === 9) {
                    console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 +
                        31 + 31);
                }
                // Sprawdzenie, czy miesiąc to październik
                else if (miesiac === 10) {
                    console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 +
                        31 + 31 + 30);
                }
                // Sprawdzenie, czy miesiąc to listopad
                else if (miesiac === 11) {
                    console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 +
                        31 + 31 + 30 + 31);
                }
                // Sprawdzenie, czy miesiąc to grudzień
                else if (miesiac === 12) {
                    console.log(dzien + 31 + 29 + 31 + 30 + 31 + 30 +
                        31 + 31 + 30 + 31 + 30);
                }
            } else {
                console.log("Liczba jest niepoprawna");
            }
        }
        // Sprawdzenie, czy rok nie jest przestępny
        else {
            // Sprawdzenie, czy dzień jest poprawny
            if (dzien < 30 || (dzien === 30 && miesiac !== 2) || (dzien === 28 && miesiac === 2)) {
                // Sprawdzenie, czy miesiąc to styczeń
                if (miesiac === 1) {
                    console.log(dzien);
                }
                // Sprawdzenie, czy miesiąc to luty
                else if (miesiac === 2) {
                    console.log(dzien + 31);
                }
                // Sprawdzenie, czy miesiąc to marzec
                else if (miesiac === 3) {
                    console.log(dzien + 31 + 28);
                }
                // Sprawdzenie, czy miesiąc to kwiecień
                else if (miesiac === 4) {
                    console.log(dzien + 31 + 28 + 31);
                }
                // Sprawdzenie, czy miesiąc to maj
                else if (miesiac === 5) {
                    console.log(dzien + 31 + 28 + 31 + 30);
                }
                // Sprawdzenie, czy miesiąc to czerwiec
                else if (miesiac === 6) {
                    console.log(dzien + 31 + 28 + 31 + 30 + 31);
                }
                // Sprawdzenie, czy miesiąc to lipiec
                else if (miesiac === 7) {
                    console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30);
                }
                // Sprawdzenie, czy miesiąc to sierpień
                else if (miesiac === 8) {
                    console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 +
                        31);
                }
                // Sprawdzenie, czy miesiąc to wrzesień
                else if (miesiac === 9) {
                    console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 +
                        31 + 31);
                }
                // Sprawdzanie, czy miesiąc to październik
                else if (miesiac === 10) {
                    console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 +
                        31 + 31 + 30);
                }
                // Sprawdzenie, czy miesiąc to listopad
                else if (miesiac === 11) {
                    console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 +
                        31 + 31 + 30 + 31);
                }
                // Sprawdzenie, czy miesiąc to grudzień
                else if (miesiac === 12) {
                    console.log(dzien + 31 + 28 + 31 + 30 + 31 + 30 +
                        31 + 31 + 30 + 31 + 30);
                }
            } else {
                console.log("Liczba jest niepoprawna");
            }
        }
    } else {
        console.log("Liczba jest niepoprawna");
    }
}