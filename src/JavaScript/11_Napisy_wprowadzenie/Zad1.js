var Main = /** @class */ (function() {
    function Main() {}
    Main.odwrocNapisV1 = function(slowo) {
        var rozdziel = slowo.split("");
        var odwroc = rozdziel.reverse();
        return odwroc.join("");
    };
    Main.odwrocNapisV2 = function(slowo) {
        if (slowo === "")
            return "";

        else
            return Main.odwrocNapisV2(slowo.substring(1)) + slowo.charAt(0);
    };
    Main.test1 = function() {
        var napis = "adam";
        var wynik = "mada";
        if (!(Main.odwrocNapisV1(napis) === wynik)) {
            throw new Error("Assertion error line 24: assert odwrocNapisV1(napis).equals(wynik);");
        };
    };
    Main.test2 = function() {
        var napis = "adam";
        var wynik = "mada";
        if (!(Main.odwrocNapisV2(napis) === wynik)) {
            throw new Error("Assertion error line 30: assert odwrocNapisV2(napis).equals(wynik);");
        };
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
