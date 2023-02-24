/*
Otrzymujesz tekst w postaci napisu. Znajdz wszystkie slowa, w ktorych te same
znaki wystepuja ta sama liczbe razy. Inaczej, znajdz wszystkie anagramy w
tekscie. Zignoruj roznice miedzy malymi i wielkimi literami. Pamietaj, slowa
skladaja sie wylacznie z liter.
*/

var Pair = /** @class */ (function() {
    function Pair(a, b) {
        this.first = a;
        this.second = b;
    }
    Pair.prototype.equals = function(other) {
        return this.first === other.first && this.second === other.second;
    }
    return Pair;
}());

budujSlownik = function(napis) {
    histogram = {};
    for (const znak of napis) {
        if (histogram[znak] === undefined) {
            histogram[znak] = 1;
        } else {
            histogram[znak]++;
        }
    }
    return histogram;
}

rozdzielSlowa = function(napis) {
    wynik = [];
    for (const slowo of napis.split(" ")) {
        slowoBezZnakow = slowo.replace(/[^a-z]/gi, "");
        slowoBezZnakow = slowoBezZnakow.toLowerCase();
        if (wynik.includes(slowoBezZnakow)) {
            continue;
        } else {
            wynik.push(slowoBezZnakow);
        }
    }
    return wynik;
}

anagramy = function(napis) {
    slowa = rozdzielSlowa(napis);
    wynik = [];
    for (const slowo of slowa) {
        for (const slowo2 of slowa) {
            if (slowo === slowo2 || wynik.some(e => e.first === slowo2 && e.second === slowo)) {
                continue;
            }
            histogram1 = budujSlownik(slowo)
            histogram2 = budujSlownik(slowo2)
            if (Object.keys(histogram1).length !== Object.keys(histogram2).length) {
                continue;
            }
            flaga = true;
            for (const znak in histogram1) {
                if (histogram1[znak] !== histogram2[znak]) {
                    flaga = false;
                    break;
                }
            }
            if (flaga) {
                wynik.push(new Pair(slowo, slowo2));
            }
        }
    }
    return wynik;
}

test1 = function() {
    var napis = "To absurd, ze tyran Brudas, ten straszliwy bandzior " +
        "sprawuje rzady w tym kraju. " +
        "Burza nad galeria i alergia na narty to zadna zbrodnia, " +
        "jak bandzior i jego arbuz.";
    var oczekiwane = [
        new Pair("absurd", "brudas"),
        new Pair("tyran", "narty"),
        new Pair("bandzior", "zbrodnia"),
        new Pair("burza", "arbuz"),
        new Pair("galeria", "alergia")
    ];

    var wynik = anagramy(napis);
    wynik.sort(function(a, b) {
        if (a.first < b.first) {
            return -1;
        } else if (a.first > b.first) {
            return 1;
        } else {
            return 0;
        }
    });
    oczekiwane.sort(function(a, b) {
        if (a.first < b.first) {
            return -1;
        } else if (a.first > b.first) {
            return 1;
        } else {
            return 0;
        }
    });

    if (!(wynik.length == oczekiwane.length)) {
        throw new Error(`Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (!(wynik[i].first == oczekiwane[i].first && wynik[i].second == oczekiwane[i].second)) {
            throw new Error(`Assertion error line 38: ${wynik[i].first} != ${oczekiwane[i].first} || ${wynik[i].second} != ${oczekiwane[i].second}`);
        }
    }
}

test2 = function() {
    var napis = "I love the way sometimes the letters of an anagram " +
        "rearrange themselves in my " +
        "head with no effort, whereas sometimes I have to write " +
        "them out in a circle to work it out.";
    var oczekiwane = [];

    var wynik = anagramy(napis);
    wynik.sort(function(a, b) {
        if (a.first < b.first) {
            return -1;
        } else if (a.first > b.first) {
            return 1;
        } else {
            return 0;
        }
    });
    oczekiwane.sort(function(a, b) {
        if (a.first < b.first) {
            return -1;
        } else if (a.first > b.first) {
            return 1;
        } else {
            return 0;
        }
    });

    if (!(wynik.length == oczekiwane.length)) {
        throw new Error(`Assertion error line 54: ${wynik.length} != ${oczekiwane.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (!(wynik[i].first == oczekiwane[i].first && wynik[i].second == oczekiwane[i].second)) {
            throw new Error(`Assertion error line 58: ${wynik[i].first} != ${oczekiwane[i].first} || ${wynik[i].second} != ${oczekiwane[i].second}`);
        }
    }
}

main = function() {
    test1();
    test2();
}

main();