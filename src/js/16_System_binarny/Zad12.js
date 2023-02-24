/*
Otrzymujesz dziesietna reprezentacje liczby naturalnej.
Oblicz dlugosc najdluzszego ciagu zer w jej binarnej reprezentacji.
*/

najdluzszyCiagZer = function(liczba) {
    if (liczba == 0)
        return 1;

    var wynik = 0;
    var pom = 0;

    while (liczba != 0) {
        var reszta = liczba % 2;
        liczba /= 2;
        if (reszta == 1) {
            wynik = Math.max(wynik, pom);
            pom = 0;
        } else
            pom++;
    }
    return Math.max(wynik, pom);
}


test1 = function() {
    var liczba = 111;
    var oczekiwane = 1;
    var wynik = najdluzszyCiagZer(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 129: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


test2 = function() {
    var liczba = 8219;
    var oczekiwane = 8;
    var wynik = najdluzszyCiagZer(liczba);

    if (wynik !== oczekiwane) {
        throw new Error(`Assertion error line 139: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


main = function(args) {
    test1();
    test2();
}

main(null);