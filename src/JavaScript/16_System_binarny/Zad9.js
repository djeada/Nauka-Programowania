/*
Otrzymujesz napis. Przy uzyciu operatorow bitowych:
a) Zamien wielkie litery na male litery.
b) Zamien male litery na wielkie litery.
c) Zamien male litery na wielkie litery i wielkie litery na male litery.
*/

wielkieNaMale = function(slowo) {
    var wynik = "";

    for (const litera of slowo)
        wynik += String.fromCharCode(litera.charCodeAt() | ' '.charCodeAt());

    return wynik;
}


maleNaWielkie = function(slowo) {
    var wynik = "";

    for (const litera of slowo)
        wynik += String.fromCharCode(litera.charCodeAt() & '_'.charCodeAt());

    return wynik;
}


odwrocWielkoscLiter = function(slowo) {
    var wynik = "";

    for (const litera of slowo) {

        if (litera >= 'a' && litera <= 'z')
            wynik += String.fromCharCode(litera.charCodeAt() ^ ' '.charCodeAt());

        else if (litera >= 'A' && litera <= 'Z')
            wynik += String.fromCharCode(litera.charCodeAt() ^ ' '.charCodeAt());

        else
            wynik += litera;
    }

    return wynik;
}


test1 = function() {
    var slowo = "KURCZAKU";
    var oczekiwane = "kurczaku";
    var wynik = wielkieNaMale(slowo);
    if (oczekiwane !== wynik) {
        throw new Error(`Assertion error line 25: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


test2 = function() {
    var slowo = "piesek";
    var oczekiwane = "PIESEK";
    var wynik = maleNaWielkie(slowo);

    if (oczekiwane !== wynik) {
        throw new Error(`Assertion error line 35: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


test3 = function() {
    var slowo = "wszedl Kotek na PloteK i mrUga";
    var oczekiwane = "WSZEDL kOTEK NA pLOTEk I MRuGA";
    var wynik = odwrocWielkoscLiter(slowo);

    if (oczekiwane !== wynik) {
        throw new Error(`Assertion error line 45: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


main = function() {
    test1();
    test2();
    test3();
}

main();