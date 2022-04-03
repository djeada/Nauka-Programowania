var Main = (function() {
    function Main() {}
    Main.usunSpacjeV1 = function(zdanie) {
        return zdanie.replace(new RegExp("\\s", 'g'), "");
    };
    Main.test1 = function(args) {
        var zdanie = "lezy jezy na wierzy";
        var oczekiwane = "lezyjezynawierzy";
        var wynik = Main.usunSpacjeV1(zdanie);

        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.test2 = function(args) {
        zdanie = "d";
        oczekiwane = "d";
        wynik = Main.usunSpacjeV1(zdanie);

        if (!(wynik === oczekiwane)) {
            throw new Error(`Assertion error line 24: ${wynik} === ${oczekiwane}`);
        }
    };
    Main.main = function(args) {
        Main.test1();
        Main.test2();
    };
    return Main;
}());
Main["__class"] = "Main";
Main.main(null);
