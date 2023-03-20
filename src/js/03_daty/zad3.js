/*
Tytuł: Rok przestępny.

Treść: Napisz program, który dla pobranej liczby naturalnej będzie sprawdzał, czy dany rok jest przestępny.

Podpowiedź: Rok przestępny jest podzielny przez 4, ale nie jest podzielny przez 100, chyba że jest podzielny przez 400.

Dane wejściowe: Liczba naturalna.

Dane wyjściowe: Komunikat o tym, czy rok jest przestępny, czy też nie.

Przykład:

Dla pobranej liczby 2100, program powinien wypisać informację, że rok nie jest przestępny.
*/

// Pobieranie danych od użytkownika
const rok = parseInt(prompt("Podaj rok:"));

// Sprawdzenie, czy rok jest przestępny
if (rok % 4 === 0 && rok % 100 !== 0 || rok % 400 === 0) {
    console.log("Rok jest przestępny");
} else {
    console.log("Rok nie jest przestępny");
}