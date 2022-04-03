/*
Dla otrzymanego napisu, znajdz jego wszystkie permutacje.
*/

var Main = /** @class */ (function () { 
    function Main() { } 
    Main.permutacje = function (napis) {
        if (napis.length === 1)
            return [napis];
        var permutacje = [];
        for (var i = 0; i < napis.length; i++) {
            var znak = napis.charAt(i);
            var reszta = Main.permutacje(napis.substring(0, i) + napis.substring(i + 1));
            for (var j = 0; j < reszta.length; j++) {
                permutacje.push(znak + reszta[j]);
            }
        }
        return permutacje;
    }
    Main.test1 = function () {
        var napis = "adam";
        var oczekiwane = ["adam", "adma", "amad", "amda", "dama", "dama", "madam", "madam", "mada", "mada"];
        var wynik = Main.permutacje(napis);
        if (!(wynik.length === oczekiwane.length)) {
            throw new Error(`Assertion error line 24: ${wynik.length} === ${oczekiwane.length}`);
        }
        for (var i = 0; i < wynik.length; i++) {
            if (!(wynik[i] === oczekiwane[i])) {
                throw new Error(`Assertion error line 24: ${wynik[i]} === ${oczekiwane[i]}`);
            }
        }
    }
    Main.main = function (args) {
        Main.test1();
    }
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
