/*
Otrzymujesz napis reprezentujacy zdanie. Znajdz wszystkie palindromy
w zdaniu. Roznice miedzy wielkimi i malymi literami powinny byc zignorowane.
*/

var Main = /** @class */ (function () {
    function Main() {
    }
    Main.czyPalindrom = function (napis) {
        var napis1 = napis.toLowerCase();
        var napis2 = napis.toLowerCase();
        napis2 = napis2.split("").reverse().join("");
        if (napis1 === napis2)
            return true;
        return false;
    }
    Main.rozdzielNaSlowa = function (napis) {
        var words = napis.split(/[\s,]+/);
        for (var i = 0; i < words.length; i++) {
            words[i] = words[i].replace(/[.,\/#!$%\^&\*;:{}=\-_`~()]/g, "");
        }        
        return words;
    }
    Main.palindromy = function (napis) {
        var words = Main.rozdzielNaSlowa(napis);
        var palindromy = [];
        for (var i = 0; i < words.length; i++) {
            if (Main.czyPalindrom(words[i]))
                palindromy.push(words[i]);
        }
        return palindromy;
    }
    Main.test1 = function () {
        var zdanie = "Tata zbaral kajak na wycieczke i uderzyl sie w oko.";
        var oczekiwane = ["kajak", "i", "w", "oko"];
        var words = Main.rozdzielNaSlowa(zdanie);
        var palindromy = Main.palindromy(zdanie);
        if (oczekiwane.length !== palindromy.length) {
            throw new Error("Assertion error line 24: assert anagramy(napis1, napis2);");
        }
        oczekiwane.sort();
        palindromy.sort();
        for (var i = 0; i < oczekiwane.length; i++) {
            if (oczekiwane[i] !== palindromy[i]) {
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
