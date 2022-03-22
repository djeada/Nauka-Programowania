/*
Dla podanych dwoch napisow sprawdz czy sa swoimi anagramami.
Dwa napisy sa anagramami jesli jeden z nich mozna zbudowac
poprzez przestawienie znakow w drugim.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.anagramy = function (napis1, napis2) {
        if (napis1.length !== napis2.length)
            return false;
        var tab1 = Main.zamienNaTab(napis1);
        var tab2 = Main.zamienNaTab(napis2);
        for (var i = 0; i < tab1.length; i++) {
            var index = tab2.indexOf(tab1[i]);
            if (index === -1)
                return false;
            tab2[index] = -1;
        }
        return true;
    };
    Main.zamienNaTab = function (napis) {
        var tab = [];
        for (var i = 0; i < napis.length; i++) {
            tab.push(napis.charAt(i));
        }
        return tab;
    };
    Main.test1 = function () {
        var napis1 = "adam";
        var napis2 = "mada";
        if (!(Main.anagramy(napis1, napis2))) {
            throw new Error("Assertion error line 24: assert anagramy(napis1, napis2);");
        };
    };
    Main.test2 = function () {
        var napis1 = "adam";
        var napis2 = "ada";
        if (Main.anagramy(napis1, napis2)) {
            throw new Error("Assertion error line 30: assert !anagramy(napis1, napis2);");
        };
    };
    Main.main = function (args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
