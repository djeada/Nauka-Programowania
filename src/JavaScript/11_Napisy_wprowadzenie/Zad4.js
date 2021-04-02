var Main = /** @class */ (function() {
    function Main() {}
    Main.naWielkieV1 = function(slowo) {
        return slowo.toUpperCase();
    };
    Main.test1 = function() {
        var napis = "pacZka!";
        var wynik = "PACZKA!";
        if (!(Main.naWielkieV1(napis) === wynik)) {
            throw new Error("Assertion error line 9: assert naWielkieV1(napis).equals(wynik);");
        };
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
