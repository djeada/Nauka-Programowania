/*
Otrzymujesz liczbe naturalna, podstawe systemu liczbowego w ktorym
zapisana jest otrzymana liczba oraz podstawe systemu na ktory ma
zostac dokonana konwersja. Zwroc reprezentacje otrzymanej liczby
w nowym systemie.
*/

naDziesietny = function(liczba, staraPodstawa) {
    var reprezentacjaDziesietna = 0;

    for (var i = liczba.length - 1; i >= 0; i--) {

        if (liczba[i] >= 'A' && liczba[i] < 'Z')
            reprezentacjaDziesietna +=
            (liczba[i] - 'A' + 10) * Math.pow(staraPodstawa, (liczba.length - 1 - i));

        else
            reprezentacjaDziesietna +=
            (liczba[i] - '0') * Math.pow(staraPodstawa, (liczba.length - 1 - i));
    }

    return reprezentacjaDziesietna;
}


zmianaPodstawy = function(liczba, staraPodstawa, nowaPodstawa) {
    if (staraPodstawa > (10 + 'Z' - 'A'))
        throw new Error("Podstawa systemu nie moze byc wieksza niz 36");

    var reprezentacjaDziesietna = naDziesietny(liczba, staraPodstawa);
    liczba = "";
    podstawa = nowaPodstawa;

    while (reprezentacjaDziesietna > 0) {
        var reszta = reprezentacjaDziesietna % podstawa;
        reprezentacjaDziesietna /= podstawa;

        var nowyZnak = '0' + reszta;

        if (nowyZnak > '9')
            nowyZnak = 'A' + (nowyZnak - '9') - 1;

        liczba += nowyZnak;
    }

    return liczba.split("").reverse().join("");
}


test1 = function() {
    var liczba = "4301";
    var oczekiwane = "1003031";
    var wynik = zmianaPodstawy(liczba, 10, 4);

    if (wynik != oczekiwane)
        throw new Error(`Assertion error line 57: ${wynik} != ${oczekiwane}`);
}


main = function() {
    test1();
}