/*
Tytuł: Hasło.

Treść: Napisz dwie funkcje:

* Pierwsza funkcja powinna prosić użytkownika o podanie nazwy użytkownika i hasła, a następnie zwrócić te dane.
* Druga funkcja powinna otrzymać dane od pierwszej funkcji i ponownie prosić użytkownika o podanie nazwy użytkownika i hasła. Prośba o podanie danych powinna być umieszczona w pętli. Warunkiem zakończenia pętli jest podanie przez użytkownika danych identycznych z tymi przekazanymi przez pierwszą funkcję.

Dane wejściowe: dwie nazwy użytkownika i hasła (napisy)

Dane wyjściowe: komunikat
*/

// Funkcja prosi o podanie nazwy użytkownika i hasła, a następnie zwraca te dane
const pobierzDaneUzytkownika = () => {
    const nazwaUzytkownika = prompt("Podaj nazwę użytkownika:");
    const haslo = prompt("Podaj hasło:");
    return {
        nazwaUzytkownika,
        haslo
    };
};

// Funkcja otrzymuje dane od pierwszej funkcji i ponownie prosi o podanie nazwy użytkownika i hasła
const sprawdzDaneUzytkownika = (poprawneDane) => {
    let daneUzytkownika;
    do {
        daneUzytkownika = pobierzDaneUzytkownika();
    } while (daneUzytkownika.nazwaUzytkownika !== poprawneDane.nazwaUzytkownika || daneUzytkownika.haslo !== poprawneDane.haslo);

    console.log("Poprawne dane użytkownika");
};

// Główna funkcja programu
const main = () => {
    const poprawneDane = pobierzDaneUzytkownika();
    sprawdzDaneUzytkownika(poprawneDane);
};

// Uruchom program
main();