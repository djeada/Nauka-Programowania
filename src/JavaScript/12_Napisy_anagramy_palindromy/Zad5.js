/*
Otrzymujesz napis reprezentujacy zdanie oraz slowo. Znajdz wszystkie
anagramy  otrzymanego slowa w zdaniu. Roznice miedzy wielkimi i malymi
literami powinny byc zignorowane.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.czyAnagram = function (napis1, napis2) {
        if (napis1.length !== napis2.length)
            return false;
        var tab1 = Main.zamienNaTab(napis1);
        var tab2 = Main.zamienNaTab(napis2);
        for (var i = 0; i < tab1.length; i++) {
            var index = tab2.indexOf(tab1[i]);
            if (index === -1)
                return false;
            tab2.splice(index, 1);
        }
        return true;
    }
    Main.zamienNaTab = function (napis) {
        var tab = [];
        for (var i = 0; i < napis.length; i++) {
            tab.push(napis[i]);
        }
        return tab;
    }
    Main.rozdzielNaSlowa = function (napis) {
        var words = napis.split(/[\s,]+/);
        for (var i = 0; i < words.length; i++) {
            words[i] = words[i].replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "");
        }        
        return words;
    }
    Main.anagramy = function (napis, slowo) {
        var words = Main.rozdzielNaSlowa(napis);
        var anagramy = [];
        for (var i = 0; i < words.length; i++) {
            if (Main.czyAnagram(words[i], slowo))
                anagramy.push(words[i]);
        }
        return anagramy;
    }
    Main.test1 = function () {
        var zdanie = "Za jego nikczemne uczynki, spotakla go wysoce sroga kara."
        var slowo = "arak";
        var oczekiwane = ["kara"];
        var anagramy = Main.anagramy(zdanie, slowo);
        if (oczekiwane.length !== anagramy.length) {
            throw new Error("Assertion error line 24: assert anagramy(napis1, napis2);");
        }
        oczekiwane.sort();
        anagramy.sort();
        for (var i = 0; i < oczekiwane.length; i++) {
            if (oczekiwane[i] !== anagramy[i]) {
                throw new Error("Assertion error line 24: assert anagramy(napis1, napis2);");
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
