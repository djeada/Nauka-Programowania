/*
Znajdz permutacje danego slowa bedace palindromami.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
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
    Main.czyPalindrom = function (napis) {
        var odwroc = Main.odwrocNapis(napis);
        return (odwroc === napis);
    }
    Main.odwrocNapis = function (napis) {
        if (napis.length === 1)
            return napis;
        return Main.odwrocNapis(napis.substring(1)) + napis.charAt(0);
    }
    Main.permutacjePalindomiczne = function (napis) {
        var permutacje = Main.permutacje(napis);
        var wynik = new Set();
        for (var i = 0; i < permutacje.length; i++) {
            if (Main.czyPalindrom(permutacje[i])) {
                wynik.add(permutacje[i]);
            }
        }
        return Array.from(wynik);
    }
    Main.test1 = function () {
        var napis = "adamm";
        var oczekiwane = ["madam", "amdma"];
        var wynik = Main.permutacjePalindomiczne(napis);
        if (wynik.length !== oczekiwane.length) {
            throw new Error(`Assertion error line 29: ${wynik.length} != ${oczekiwane.length}`);
        }
        oczekiwane.sort();
        wynik.sort();
        for (var i = 0; i < oczekiwane.length; i++) {
            if (wynik[i] !== oczekiwane[i]) {
                throw new Error(`Assertion error line 29: ${wynik[i]} != ${oczekiwane[i]}`);
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
