/*
Zbuduj prosta baze danych dla biblioteki oparta o slownik w ktorym kluczami sa
imiona czytelnikow, a wartosciami listy wypozyczonych ksiazek.
Baza danych powinna umozliwiac:
a) Dodanie wypozyczonej ksiazki do danego czytelnika.
b) Zwrocenie wypozyczonej ksiazki przez czytelnika.
c) Wypisanie aktualnej listy wypozyczonych ksiazek dla danego czytelnika.
*/

dodajKsiazke = function(lista, uzytkownik, ksiazka) {
    if (lista[uzytkownik] !== undefined) {

        if (lista[uzytkownik].indexOf(ksiazka) == -1)
            lista[uzytkownik].push(ksiazka);

        else
            console.log("Uzytkownik juz wypozyczyl ta ksiazke.");
    } else {
        var ksiazki = [ksiazka];
        lista[uzytkownik] = ksiazki;
    }
}

usunKsiazke = function(lista, uzytkownik, ksiazka) {
    if (lista[uzytkownik] === undefined) {
        console.log("Podany uzytkownik nie znajduje sie w liscie.");
        return;
    }

    if (lista[uzytkownik].indexOf(ksiazka) != -1)
        lista[uzytkownik].splice(lista[uzytkownik].indexOf(ksiazka), 1);

    else
        console.log("Uzytkownik nie wypozyczyl tej ksiazki.");
}

wyswietlKsiazki = function(lista, uzytkownik) {
    if (lista[uzytkownik] === undefined) {
        console.log("Podany uzytkownik nie znajduje sie w liscie.");
        return;
    }

    console.log("Uzytkownik " + uzytkownik + " wypozyczyl nastepujace ksiazki: ");

    for (var ksiazka of lista[uzytkownik])
        console.log(ksiazka);
}


wyswietlWszystkieKsiazki = function(lista) {
    for (var it = lista.begin(); it != lista.end(); it++) {
        wyswietlKsiazki(lista, it.key);
        console.log();
    }
}

testDodajKsiazke = function() {
    var lista = {}

    dodajKsiazke(lista, "Jan Kowalski", "W pustyni i w puszczy");
    oczekiwane = 1
    wynik = lista["Jan Kowalski"].length
    if (wynik != oczekiwane)
        throw new Error(`Assertion error line 164: ${wynik} != ${oczekiwane}`);

    dodajKsiazke(lista, "Jan Kowalski", "W pustyni i w puszczy");
    oczekiwane = 1
    wynik = lista["Jan Kowalski"].length

    if (wynik != oczekiwane)
        throw new Error(`Assertion error line 169: ${wynik} != ${oczekiwane}`);

    dodajKsiazke(lista, "Jan Kowalski", "Wladca Pierscieni");
    oczekiwane = 2
    wynik = lista["Jan Kowalski"].length
    if (wynik != oczekiwane)
        throw new Error(`Assertion error line 174: ${wynik} != ${oczekiwane}`);
}


testUsunKsiazke = function() {
    var lista = {}

    dodajKsiazke(lista, "Jan Kowalski", "W pustyni i w puszczy");
    dodajKsiazke(lista, "Jan Kowalski", "Wladca Pierscieni");
    usunKsiazke(lista, "Jan Kowalski", "W pustyni i w puszczy");
    oczekiwane = 1
    wynik = lista["Jan Kowalski"].length
    if (wynik != oczekiwane)
        throw new Error(`Assertion error line 184: ${wynik} != ${oczekiwane}`);

    usunKsiazke(lista, "Jan Kowalski", "Wladca Pierscieni");
    oczekiwane = 0
    wynik = lista["Jan Kowalski"].length
    if (wynik != oczekiwane)
        throw new Error(`Assertion error line 189: ${wynik} != ${oczekiwane}`);
}


main = function() {
    testDodajKsiazke();
    testUsunKsiazke();
}

main();