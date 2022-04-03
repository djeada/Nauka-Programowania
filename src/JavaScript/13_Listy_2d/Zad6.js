/*
Otrzymujesz liste par liczb. Liczby w parze reprezentuja poczatek i koniec
przedzialu. Niektore przedzialy moga na siebie nachodzic. W takim przypadku
polacz je ze soba i zwroc liste niepokrywajacych sie przedzialow.
*/

var Pair = /** @class */ (function () {
    function Pair(a, b) {
        this.first = a;
        this.second = b;
    }
    return Pair;
}());

var Main = /** @class */ (function () { 
    function Main() { }
    Main.polaczPrzedzialy = function (lista) {
        lista.sort(function (a, b) {
            // first compare by first element
            // if equal, compare by second element
            if (a.first < b.first)
                return -1;
            if (a.first > b.first)
                return 1;
            if (a.second < b.second)
                return -1;
            return 1;
        });
        var pocz = lista[0].first;
        var koniec = lista[0].second;
        lista.splice(0, 1);
        var wynik = new Array();
        for (var _i = 0, lista_1 = lista; _i < lista_1.length; _i++) {
            var para = lista_1[_i];
            if (koniec >= para.first) {
                if (koniec < para.second)
                    koniec = para.second;
            }
            else {
                wynik.push(new Pair(pocz, koniec));
                pocz = para.first;
                koniec = para.second;
            }
        }
        wynik.push(new Pair(pocz, koniec));
        return wynik;
    };
    Main.test1 = function () {
        var lista = [new Pair(23, 67), new Pair(23, 53), new Pair(45, 88), new Pair(77, 88), new Pair(10, 22), new Pair(11, 12), new Pair(42, 45)];
        var oczekiwane = [new Pair(10, 22), new Pair(23, 88)];
        var wynik = Main.polaczPrzedzialy(lista);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (wynik[i].first !== oczekiwane[i].first) {
                throw new Error(`Assertion error line 29: ${wynik[i].first} != ${oczekiwane[i].first}`);
            }
            if (wynik[i].second !== oczekiwane[i].second) {
                throw new Error(`Assertion error line 29: ${wynik[i].second} != ${oczekiwane[i].second}`);
            }
        }
    };
    Main.main = function (args) {
        Main.test1();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
