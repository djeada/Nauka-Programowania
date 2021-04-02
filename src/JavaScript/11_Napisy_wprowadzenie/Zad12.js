var Main = (function() {
    function Main() {}
    Main.usunSpacjeV1 = function(zdanie) {
        return zdanie.replace(new RegExp("\\s", 'g'), "");
    };
    Main.main = function(args) {
        var zdanie = "lezy jezy na wierzy";
        var wynik = "lezyjezynawierzy";
        if (!(Main.usunSpacjeV1(zdanie) === wynik)) {
            throw new Error("Assertion error line 9: assert usunSpacjeV1(zdanie).equals(wynik);");
        };
        zdanie = "d";
        wynik = "d";
        if (!(Main.usunSpacjeV1(zdanie) === wynik)) {
            throw new Error("Assertion error line 12: assert usunSpacjeV1(zdanie).equals(wynik);");
        };
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
