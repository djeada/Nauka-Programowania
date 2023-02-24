/*
Otrzymujesz liste par. Pierwszym elementem pary jest napis reprezentujacy
imie i nazwisko pracownika, drugim zysk z transakcji jaka dany pracownik
przeprowadzil. Znajdz pracownika, ktory przyniosl firmie najwiecej zysku.
*/

wypelnijSlownik = function(lista, slownik) {
    for (var rekord of lista) {
        if (slownik[rekord.first] === undefined) {
            slownik[rekord.first] = rekord.second;
        } else {
            slownik[rekord.first] += rekord.second;
        }
    }
}

znajdzMaxZysk = function(slownik) {
    var najlepszyPracownik;
    var maxZysk = -1;

    for (var it in slownik) {
        if (slownik[it] > maxZysk) {
            najlepszyPracownik = it;
            maxZysk = slownik[it];
        }
    }

    return najlepszyPracownik;
}


pracownik = function(lista) {
    if (lista.length === 0)
        return "";

    var slownik = {};
    wypelnijSlownik(lista, slownik);

    return znajdzMaxZysk(slownik);
}


test1 = function() {
    var lista = [{
        first: "Jan",
        second: 10
    }, {
        first: "Piotr",
        second: 20
    }, {
        first: "Piotr",
        second: 30
    }, {
        first: "Piotr",
        second: 40
    }];
    var oczekiwane = "Piotr";
    var wynik = pracownik(lista);
    if (oczekiwane !== wynik) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


test2 = function() {
    var lista = [{
        first: "Jan",
        second: 10
    }, {
        first: "Piotr",
        second: 20
    }, {
        first: "Piotr",
        second: 30
    }, {
        first: "Piotr",
        second: 40
    }];
    var oczekiwane = "Piotr";
    var wynik = pracownik(lista);
    if (oczekiwane !== wynik) {
        throw new Error(`Assertion error line 79: oczekiwane: ${oczekiwane}, obliczone: ${wynik}`);
    }
}


main = function() {
    test1();
    test2();
}

main();