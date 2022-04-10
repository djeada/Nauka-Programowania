var Pair = /** @class */ (function() {
    function Pair(a, b) {
        this.first = a;
        this.second = b;
    }
    return Pair;
}());
znajdzParyV1 = function(lista, suma) {
    var oczekiwane = ([]);
    for (var i = 0; i < lista.length; i++) {
        {
            for (var j = i + 1; j < lista.length; j++) {
                {
                    if (lista[i] + lista[j] === suma) {
                        oczekiwane.push(new Pair(lista[i], lista[j]));
                    }
                };
            }
        };
    }
    return oczekiwane;
};

test1 = function() {
    var lista = [0, 4, 5, 6, 2, 9, 2, 3]
    var suma = 5;
    var oczekiwane = [new Pair(0, 5), new Pair(2, 3), new Pair(2, 3)]
    var wynik = znajdzParyV1(lista, suma);
    if (!(wynik.length == oczekiwane.length)) {
        throw new Error(`Assertion error line 34: ${wynik.length} != ${oczekiwane.length}`);
    }
    for (var i = 0; i < wynik.length; i++) {
        if (!(wynik[i].first == oczekiwane[i].first && wynik[i].second == oczekiwane[i].second)) {
            throw new Error(`Assertion error line 38: ${wynik[i].first} != ${oczekiwane[i].first} || ${wynik[i].second} != ${oczekiwane[i].second}`);
        }
    }
};
main = function(args) {
    test1();
};

main(null);