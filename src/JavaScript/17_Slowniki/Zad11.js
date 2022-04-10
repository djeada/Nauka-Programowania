/*
Otrzymujesz slownik skladajacy sie z par napisow i liczb calkowitych.
a) Wypisz pary posortowane wzgledem napisow.
b) Wypisz pary posortowane wzgledem liczb.
*/
var Pair = /** @class */ (function() {
    function Pair(a, b) {
        this.first = a;
        this.second = b;
    }
    return Pair;
}());

sortujWzgledemNapisow = function(slownik) {
    var wynik = [];
    for (const key in slownik) {
        wynik.push(new Pair(key, slownik[key]));
    }

    wynik.sort(function(a, b) {
            if (a.first < b.first) {
                return -1;
            }
            if (a.first > b.first) {
                return 1;
            }
            return 0;
        }

    );
    return wynik;
};


sortujWzgledemWartosci = function(slownik) {
    var wynik = [];
    for (const key in slownik) {
        wynik.push(new Pair(key, slownik[key]));
    }

    wynik.sort(function(a, b) {
            if (a.second < b.second) {
                return -1;
            }
            if (a.second > b.second) {
                return 1;
            }
            return 0;
        }

    );
    return wynik;
}

test1 = function() {
    var slownik = {
        "c": 3,
        "x": 5,
        "a": -2,
        "b": 4
    };
    var oczekiwane = [new Pair("a", -2), new Pair("c", 3), new Pair("b", 4), new Pair("x", 5)];
    var wynik = sortujWzgledemWartosci(slownik);

    if (!(wynik.length == oczekiwane.length)) {
        throw new Error(`Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`);
    }

    for (var i = 0; i < wynik.length; i++) {
        if (!(wynik[i].first == oczekiwane[i].first && wynik[i].second == oczekiwane[i].second)) {
            throw new Error(`Assertion error line 38: ${wynik[i].first} != ${oczekiwane[i].first} || ${wynik[i].second} != ${oczekiwane[i].second}`);
        }
    }
};

test2 = function() {
    var slownik = {
        "c": 3,
        "x": 5,
        "a": -2,
        "b": 4
    };
    var oczekiwane = [new Pair("a", -2), new Pair("b", 4), new Pair("c", 3), new Pair("x", 5)];
    var wynik = sortujWzgledemNapisow(slownik);

    if (!(wynik.length == oczekiwane.length)) {
        throw new Error(`Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`);
    }

    for (var i = 0; i < wynik.length; i++) {
        if (!(wynik[i].first == oczekiwane[i].first && wynik[i].second == oczekiwane[i].second)) {
            throw new Error(`Assertion error line 38: ${wynik[i].first} != ${oczekiwane[i].first} || ${wynik[i].second} != ${oczekiwane[i].second}`);
        }
    }
}

main = function() {
    test1();
    test2();
}

main();