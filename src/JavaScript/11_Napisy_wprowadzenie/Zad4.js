var Main = /** @class */ (function() {
    function Main() {}
    Main.naWielkieV1 = function(slowo) {
        return slowo.toUpperCase();
    };
    Main.test1 = function() {
        var napis = "pacZka!";
        var oczekiwane = "PACZKA!";
        var wynik = Main.naWielkieV1(napis);
        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
