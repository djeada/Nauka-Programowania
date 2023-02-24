var Pair = /** @class */ (function() {
    function Pair(a, b) {
        this.first = a;
        this.second = b;
    }
    return Pair;
}());
sumaDwochV1 = function(lista, liczba) {
    var n = lista.length;
    for (var i = 0; i < n; i++) {
        {
            for (var j = i + 1; j < n; j++) {
                {
                    if (lista[j] + lista[i] === liczba) {
                        return (new Pair(i, j));
                    }
                };
            }
        };
    }
    return (new Pair(-1, -1));
};
test1 = function() {
    var lista = [1, 3, 4, 5, 2]
    var liczba = 5;
    var oczekiwane = new Pair(0, 2)
    var wynik = sumaDwochV1(lista, liczba);
    if (!(wynik.first == oczekiwane.first && wynik.second == oczekiwane.second)) {
        throw new Error(`Assertion error line 34: ${wynik.first} != ${oczekiwane.first} || ${wynik.second} != ${oczekiwane.second}`);
    }
};
test2 = function() {
    var lista = [2, -6, 10, 21, 8]
    var liczba = 7;
    var oczekiwane = new Pair(-1, -1)
    var wynik = sumaDwochV1(lista, liczba);
    if (!(wynik.first == oczekiwane.first && wynik.second == oczekiwane.second)) {
        throw new Error(`Assertion error line 34: ${wynik.first} != ${oczekiwane.first} || ${wynik.second} != ${oczekiwane.second}`);
    }
};
main = function(args) {
    test1();
    test2();
};

main(null);